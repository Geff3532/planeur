from ogn.client import AprsClient
from ogn.parser import parse,ParseError
from acs_class import dic,import_glider

table = import_glider()

def process_beacon(raw_message):
    try:
        if raw_message[0] != '#':
            
            beacon = parse(raw_message)
        
            #try:
                #receiver = dic[beacon['receiver_name']] 
            #except:
            receiver = dic['LFYR']
            glide = table[beacon['address']]
            
            if abs(receiver['altitude'] - beacon['altitude']) < 100 and beacon['ground_speed'] < 30 and glide.get_flying():
                
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
                
        print(raw_message)
        
    except ParseError as e:
        print('Error, {}'.format(e.message))
        
    except NotImplementedError as e:
        print('{}: {}'.format(e, raw_message))

acs_filter = 'p'
for ogn_id in table.keys():
    acs_filter += '/FLR'+ogn_id

client = AprsClient(aprs_user='ACS',aprs_filter=acs_filter)
client.connect()

try:
    client.run(callback=process_beacon, autoreconnect=True)
    
except KeyboardInterrupt:
    
    print('\nStop ogn gateway')
    client.disconnect()