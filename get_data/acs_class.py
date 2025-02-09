import mysql.connector as mysql
import datetime
import random
import math
import numpy as np
import time

def update_kill(message,json):
    db = mysql.connect(host="localhost",user='root',password='',db='test')
    cursor = db.cursor()
    cursor.execute(("INSERT INTO dogfight (message,json) VALUES (%s,%s)"),(message,json))
    db.commit()
    cursor.close()
    
def import_glider():
    db = mysql.connect(host="localhost",user='root',password='',db='test')
    cursor = db.cursor()
    #date = datetime.date.today()
    cursor.execute(("SELECT * FROM acs"))
    table = cursor.fetchall()
    cursor.close()
    liste_glide = {}
    for glide in table:
        ogn = glide[1].replace('FLR','')
        liste_glide[ogn] = Glider(glide[0], glide[2])
    return liste_glide

dic = {
       '****': {"altitude":12,"position":[**,**]},
       '****': {"altitude":878,"position":[9.316,*.583]},
       '****': {"altitude":125,"position":[**.3176,*.695]}
       }  # code oaci proche et basé

class Glider:
    
    "Classe utilisé pour les planeurs"
    def __init__(self,reg,info):
        self.__id_vol = None
        self.__reg = reg
        self.__info = info
        self.__flying = False
        self.__start = None
        self.__stop = None
        self.__altitude = None
        self.__max_alt = 0
        self.__latitude = None
        self.__longitude = None
        self.__fly_end = False
        self.__ground_speed = None
        self.__climb_rate = None
        self.__turn_rate = None
        self.__track = None 
        self.__avg_turn_rate = None
        self.__save_turn_rate = []
        self.__spirale = None
        self.__comment = None
        self.__dogfight = []
        self.__kill = 0
        self.__killed = None
    
    def clean(self):
        self.__id_vol = None
        self.__flying = False
        self.__start = None
        self.__stop = None
        self.__altitude = None
        self.__max_alt = 0
        self.__latitude = None
        self.__longitude = None
        self.__fly_end = False
        self.__ground_speed = None
        self.__climb_rate = None
        self.__turn_rate = None
        self.__track = None 
        self.__avg_turn_rate = None
        self.__save_turn_rate = []
        self.__spirale = None
        self.__comment = None
        self.__dogfight = []
        self.__kill = 0
        self.__killed = None
        
    def kill(self):
        self.__kill += 1
        
    def killed(self):
        self.__killed = time.time() + 120
        
    def __conv_turn_rate(self,rate,speed):
        x = rate*speed*math.pi/(180*9.81*3.6)
        x = math.atan(x)
        return x*180/math.pi
        
    def __generate_id(self):
        id_vol = ""
        for i in range(11):
            id_vol += str(random.randint(0, 9))
        id_vol = int(id_vol)
        db = mysql.connect(host="localhost",user='root',password='',db='test')
        cursor = db.cursor() 
        cursor.execute( ('SELECT id FROM acs_planche WHERE acs_planche.id = %s'),(id_vol,) )
        table = cursor.fetchall()
        cursor.close()
        if len(table) == 0:
            self.set_id_vol(id_vol)
        else:
            self.__generate_id()
        return id_vol
    
    def __make_avg_rate(self):
        
        #determiner inclinaison moyenne
        if len(self.__save_turn_rate) == 0: return None
        T = np.array([abs(i) for i in self.__save_turn_rate])
        moy = np.mean(T)
        s = np.std(T)/np.sqrt(len(T))
        R = []
        for i in T:
            if abs(i-moy)/s < 1.96:
                R.append(i)
        if len(R) == 0: return None
        self.__avg_turn_rate = float(sum(R)/len(R))
        
        #determiner sens de la spirale
        gauche = len([i for i in self.__save_turn_rate if i < 0])
        total = len(self.__save_turn_rate)
        taux = int(gauche*100/total)
        self.__spirale = f"{taux}% spirale gauche/{100-taux}% spirale droite"
        
        return None
        
        
    def update(self,latitude,longitude,altitude,ground_speed,climb_rate,turn_rate,track):
        self.__latitude = latitude
        self.__longitude = longitude
        self.__altitude = altitude
        if self.__max_alt < altitude:
            self.__max_alt = altitude
        self.__ground_speed = ground_speed
        self.__climb_rate = climb_rate
        self.__turn_rate = self.__conv_turn_rate(turn_rate,ground_speed)
        self.__track = track
        if abs(self.__turn_rate) > 5: self.__save_turn_rate.append(self.__turn_rate)
        
        self.__dogfight.append([latitude,longitude,altitude,ground_speed,climb_rate,turn_rate,track])
        if len(self.__dogfight) > 5: self.__dogfight.pop(0)
        
        if  self.__killed != None and time.time() > self.__killed:
            self.__killed = None
        
        
            
    def update_sql(self):
        db = mysql.connect(host="localhost",user='root',password='',db='test')
        cursor = db.cursor()
        if self.__id_vol == None:
            date = datetime.date.today()
            cursor.execute(("INSERT INTO acs_planche (id,Reg,Type,Day,Start,Stop) VALUES (%s,%s,%s,%s,%s,%s)"),
                       (self.__generate_id(),self.__reg,self.__info,date,self.__start,self.__stop))
        else:
            cursor.execute( ("UPDATE acs_planche SET Start=%s,Stop=%s,Latitude=%s,Longitude=%s,Altitude=%s,Max_alt=%s,Ground_speed=%s,Climb_rate=%s,Turn_rate=%s,Track=%s,Avg_turn=%s,Spirale=%s,Kills=%s  WHERE `acs_planche`.`id` = %s"),
                       (self.__start,self.__stop,self.__latitude,self.__longitude,self.__altitude,self.__max_alt,self.__ground_speed,self.__climb_rate,abs(self.__turn_rate),self.__track,self.__avg_turn_rate,self.__spirale,self.__kill,self.__id_vol) )
        db.commit()
        cursor.close()
        
            
    #GETTERS
    
    def get_id_vol(self):
        return self.__id_vol
    
    def get_reg(self):
        return self.__reg
    
    def get_info(self):
        return self.__info
    
    def get_flying(self):
        return self.__flying
    
    def get_start(self):
        return self.__start
    
    def get_stop(self):
        return self.__stop
    
    def get_altitude(self):
        return self.__altitude
    
    def get_max_altitude(self):
        return self.__max_alt
    
    def get_latitude(self):
        return self.__latitude
    
    def get_longitude(self):
        return self.__longitude
    
    def get_fly_end(self):
        return self.__fly_end
    
    def get_ground_speed(self):
        return self.__ground_speed
    
    def get_climb_rate(self):
        return self.__climb_rate
    
    def get_turn_rate(self):
        return self.__turn_rate
    
    def get_track(self):
        return self.__track
    
    def get_dogfight(self):
        return self.__dogfight
    
    def get_killed(self):
        return self.__killed

    #SETTERS
    
    def set_id_vol(self,new):
        if self.__id_vol == None:
            self.__id_vol = new
            return self.__id_vol
        else:
            return False
    
    def set_flying(self,new):
        self.__flying = new
        return self.__flying
    
    def set_start(self,new):
        #new.replace(tzinfo=datetime.tzinfo('Europe/London'))
        #france = datetime.tzinfo('Europe/Paris')
        #new = france.fromutc(new)
        new = new.replace(hour=new.hour+2)
        self.__start = new
        return self.__start
    
    def set_stop(self,new):
        #new.replace(tzinfo=datetime.tzinfo('Europe/London'))
        #france = datetime.tzinfo('Europe/Paris')
        #new = france.fromutc(new)
        new = new.replace(hour=new.hour+2)
        self.__stop = new
        return self.__stop
    
    def set_fly_end(self,new):
        self.__fly_end = new
        if self.__fly_end:
            self.__make_avg_rate()
        return self.__fly_end
