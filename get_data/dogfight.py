from ogn.client import AprsClient
from ogn.parser import parse,ParseError
from acs_class import dic,import_glider,update_kill
import math
import pyautogui as pg
import time
import json

table = import_glider()

def distance(long1,lat1,long2,lat2):
    return 60*1.852*math.sqrt(abs(lat1-lat2)**2+abs(long1-long2)**2)

def send_message(message):
    pg.write(message)
    pg.press('enter')

def process_beacon(raw_message):
    try:
        if raw_message[0] != '#':
            
            beacon = parse(raw_message)
            receiver = dic['****'] # code oaci 
            glide = table[beacon['address']]
            
            if glide.get_flying() and ((abs(receiver['altitude'] - beacon['altitude']) < 100 and beacon['ground_speed'] < 30) or (glide.get_ground_speed() == 0 and beacon['ground_speed'] == 0) ) :
                
                glide.set_flying(False)
                glide.set_stop(beacon['timestamp'])
                glide.set_fly_end(True)
                
            if abs(receiver['altitude'] - beacon['altitude']) > 100 and beacon['ground_speed'] > 30 and glide.get_flying() == False:
                
                glide.set_flying(True)
                glide.set_start(beacon['timestamp'])   
                
            glide.update(beacon['latitude'],beacon['longitude'],beacon['altitude'],beacon['ground_speed'],beacon['climb_rate'],beacon['turn_rate'],beacon['track'])
            
            if glide.get_flying():
                glide.update_sql()
                
            if glide.get_fly_end():
                glide.update_sql()
                glide.clean()
                
            if glide.get_flying() and glide.get_altitude() > 300 + receiver['altitude'] and glide.get_killed() == None:
                liste_cible = []
                for cible in table.values():
                    if cible.get_flying():
                        d = distance(glide.get_longitude(), glide.get_latitude(), cible.get_longitude(), cible.get_latitude())
                        if cible.get_altitude() > 300 + receiver['altitude'] and  d < 1 and abs(glide.get_altitude()-cible.get_altitude()) < 150 and cible.get_id_vol() != glide.get_id_vol() and cible.get_killed() == None:
                            liste_cible.append(cible)
                if len(liste_cible) > 0:
                    for cible in liste_cible:
                        x = abs(glide.get_longitude()-cible.get_longitude())
                        y = abs(glide.get_latitude()-cible.get_latitude())
                        if x == 0:
                            track = 0
                        else:
                            track = 180*math.atan(y/x)/math.pi
                        if cible.get_longitude() < glide.get_longitude() and cible.get_latitude() > glide.get_latitude():
                            track += 90
                        elif cible.get_longitude() < glide.get_longitude() and cible.get_latitude() < glide.get_latitude():
                            track += 180
                        elif cible.get_longitude() > glide.get_longitude() and cible.get_latitude() < glide.get_latitude():
                            track += 270
                        glide_track = glide.get_track()
                        if track-5 <= glide_track and glide_track <= track+5:
                            message = f"{glide.get_reg()[-2:]} a descendu {cible.get_reg()} à {time.strftime('%Hh%M le %d-%m-%Y')}"
                            json_ = {"glide":[glide.get_reg(),glide.get_longitude(),glide.get_latitude(),glide.get_altitude(),glide.get_track(),glide.get_ground_speed(),glide.get_climb_rate(),glide.get_turn_rate()],
                                     "cible":[cible.get_reg(),cible.get_longitude(),cible.get_latitude(),cible.get_altitude(),cible.get_track(),cible.get_ground_speed(),cible.get_climb_rate(),cible.get_turn_rate()]}
                            update_kill(message,json.dumps(json_))
                            glide.kill()
                            cible.killed()
                
        print(raw_message)
        
    except ParseError as e:
        print('Error, {}'.format(e.message))
        
    except NotImplementedError as e:
        print('{}: {}'.format(e, raw_message))

acs_filter = 'p'
for ogn_id in table.keys():
    acs_filter += '/FLR'+ogn_id

client = AprsClient(aprs_user='**',aprs_filter=acs_filter) # a completer
client.connect()

try:
    client.run(callback=process_beacon, autoreconnect=True)
    
except KeyboardInterrupt:
    
    print('\nStop ogn gateway')
    client.disconnect()
