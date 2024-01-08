
import os
import json
import random
import names
import time
from collections import Counter

# rec_year = input("Recruiting Class Year: ")
print("Recommended Amount: 3000-3600")
players_to_create = int(input("Player Amount: "))
output_file_name = "results.json"
output_file_path = os.path.join(os.path.dirname(__file__), output_file_name)
def attr_gen_calc():
    players_created = 0
# Initial Randomization
    while True:
        x = {
                "year": 2022, 
                "durability": random.randint(55,120),
                "potential": random.randint(55,120),
                "height": random.randint(63,70),
                "weight": random.randint(180,320),
                "speed": random.randint(40,100),
                "evasion": random.randint(40,100),
                "strength": random.randint(40,100),
                "armStrength": random.randint(40,100),
                "accuracy": random.randint(40,100),
                "passIq": random.randint(40,100),
                "catching": random.randint(40,100),
                "routeRunning": random.randint(40,100),
                "ballSecurity": random.randint(40,100),
                "ballCarrierVision": random.randint(40,100),
                "runBlocking": random.randint(50,100),
                "passBlocking": random.randint(50,100),
                "tackling": random.randint(40,100),
                "manCoverage": random.randint(40,100),
                "zoneCoverage": random.randint(40,100),
                "blockShedding": random.randint(40,100),
                "pursuit": random.randint(40,100),
                "defensiveIq": random.randint(40,100),
                "kickPower": random.randint(40,100),
                "kickAccuracy": random.randint(40,100),
                "puntPower": random.randint(40,100),
                "puntAccuracy": random.randint(40,100)
            }
        
# Positon Calculations
        QB_Calc = ((2.75*(x["armStrength"] + x["accuracy"] + x["passIq"])) + (x["speed"] + x["evasion"] + x["ballCarrierVision"]))/6
        RB_Calc = (2.5*(x["speed"] + x["evasion"] + x["strength"]) + 1.5*(x["routeRunning"] + x["ballSecurity"] + x["catching"] +  x["ballCarrierVision"]) + (x["passBlocking"]+x["runBlocking"]))/8
        WR_Calc = (2.75*(x["routeRunning"] + x["catching"]) + 1.4*(x["speed"]) +1.1*(x["evasion"] + x["ballCarrierVision"]))/5
        TE_Calc = (2.5*(x["passBlocking"] + x["runBlocking"] + x["routeRunning"]) + (x["strength"] + x["speed"]))/5
        OL_Calc = (2*(x["passBlocking"]+ x["runBlocking"]) + 1.25*(x["strength"]))/3
        DL_Calc = (1.75*(x['blockShedding'] + x['tackling'] + x['pursuit']) + 2*(x["defensiveIq"] + x["strength"]))/5
        LB_Calc = ((x['blockShedding'] + x['defensiveIq'] + x['tackling'] + x['pursuit'] + x['manCoverage'] + x['zoneCoverage']))/3.25
        CB_Calc = (2.6*(x["manCoverage"] + x["zoneCoverage"]) + 1.25*(x['defensiveIq'] + x["tackling"]) + 1.75*(x["speed"]))/5
        S_Calc = (3*(x['defensiveIq'] + x['tackling']) + 2.2*(x['manCoverage'] + x['zoneCoverage']) + 1.25*(x['speed'] + x['strength'] + x['evasion']))/7
        K_Calc = ((x['kickAccuracy'] + x['kickPower'] + x['puntAccuracy'] + x['puntPower']))/2.25
# QB
        if(QB_Calc >= RB_Calc and QB_Calc >= WR_Calc and QB_Calc >= TE_Calc and QB_Calc >= OL_Calc and QB_Calc >= DL_Calc and QB_Calc >= LB_Calc and QB_Calc  >= CB_Calc and QB_Calc >= S_Calc and QB_Calc >= K_Calc):
            y = "QB"
# WR
        elif(WR_Calc > RB_Calc and WR_Calc > TE_Calc and WR_Calc > OL_Calc and WR_Calc > DL_Calc and WR_Calc > LB_Calc and WR_Calc > CB_Calc and WR_Calc > S_Calc and WR_Calc > K_Calc):
            y = "WR"
            x["speed"] = random.randint(65,110)
# RB
        elif(RB_Calc > TE_Calc and RB_Calc > OL_Calc and RB_Calc > DL_Calc and RB_Calc > LB_Calc and RB_Calc > CB_Calc and RB_Calc > S_Calc and RB_Calc > K_Calc): 
            y = "RB"
# TE
        elif(TE_Calc > OL_Calc and TE_Calc > DL_Calc and TE_Calc > LB_Calc and TE_Calc > CB_Calc and TE_Calc > S_Calc and TE_Calc > K_Calc): 
            y= "TE"
# OL
        elif(OL_Calc > DL_Calc and OL_Calc > LB_Calc and OL_Calc > CB_Calc and OL_Calc > S_Calc and OL_Calc > K_Calc):
            x["manCoverage"] = random.randint(20,60)
            x["zoneCoverage"] = random.randint(20,60)
            x["blockShedding"] = random.randint(20,60)
            x["pursuit"] = random.randint(20,60)
            x["armStrength"] = random.randint(20,60)
            x["accuracy"] = random.randint(20,60)
            x["kickPower"] = random.randint(20,60)
            x["puntPower"] = random.randint(20,60)
            x["tackling"] = random.randint(20,60)
            x["speed"] = random.randint(20,60)
            y="OL"
        elif(DL_Calc > LB_Calc and DL_Calc > CB_Calc and DL_Calc > S_Calc and DL_Calc > K_Calc): 
            x["manCoverage"] = random.randint(20,60)
            x["zoneCoverage"] = random.randint(20,60)
            x["passBlocking"] = random.randint(20,60)
            x["pursuit"] = random.randint(20,60)
            x["armStrength"] = random.randint(20,60)
            x["accuracy"] = random.randint(20,60)
            x["kickPower"] = random.randint(20,60)
            x["puntPower"] = random.randint(20,60)
            x["runBlocking"] = random.randint(20,60)
            x["speed"] = random.randint(20,60)
            y="DL"
        elif(LB_Calc> CB_Calc and LB_Calc > S_Calc and LB_Calc > K_Calc):
            y = "LB"
        elif(CB_Calc > S_Calc and CB_Calc > K_Calc):
            y="CB"
        elif(S_Calc > K_Calc):
            y= "S"
        else:
            y="K"
            
        if(players_created == players_to_create):
            print("Player Created")
            break
        else:        
            players_created = players_created +1
             
    pos_and_attr = (x,y,players_created)
    return pos_and_attr

def priority_avatar_gen():
    priority = {
        "playingTime": random.randint(0,10),
        "proximityToHome": random.randint(0,10),
        "prestige": random.randint(0,10),
        "stadiumAtmosphere": random.randint(0,10),
        "facilities": random.randint(0,10),
        "collegeLife": random.randint(0,10),
        "academics": random.randint(0,10),
        "nil": random.randint(0,10)
    }
    skinColor_list = ["Pale", "Light", "Tanned", "Brown", "Dark brown", "Black"]
    hairColor_list = ["Black", "Dark brown", "Brown", "Auburn", "Blonde", "Golden blonde", "Platinum", "Red", "Grey"]
    hair_list = ["Bald", "Balding", "Buzz cut", "Buzz cut indent", "Short flat", "Short round", "Short curly", "Short wavy", "Frizzle", "Mullet", "Short dreads", "Long dreads", "Very long dreads", "Afro", "Big and wavy", "Bob #1", "Bob #2", "Bun", "Curly", "Wavy", "Shoulder length", "Long #1", "Long #2", "Long #3"]
    facialHair_list = ["None", "Light beard", "Medium beard", "Majestic beard", "Moustache", "Fancy moustache"]
    eye_list = ["default", "Happy", "Side", "Wide-eyed"]
    eyebrow_list = ["Defaul", "Default (natural)", "Angry", "Angry (natural)", "Excited", "Excited (natral)", "Bushy", "Unibrow"]
    mouth_list = ["Happy", "Serious", "Smile", "Twinkle"]
    avatar = {
        "skinColor": random.choice(skinColor_list),
        "hairColor": random.choice(hairColor_list),
        "hair": random.choice(hair_list),
        "facialHair": random.choice(facialHair_list),
        "eye": random.choice(eye_list),
        "eyebrow": random.choice(eyebrow_list),
        "mouth": random.choice(mouth_list)
    }
    
    data = (avatar, priority)
    return data
types = ["HS", "JUCO"]
archtypes = ["a", "b"]
avatars = ["a", "b"]
priorities = ["a", "b"]

data_list = []
# JSON File Writing
for i in range(players_to_create):
    avatar_priority = priority_avatar_gen()
    positionAttributes = attr_gen_calc()
    rating_gen = round(random.uniform(.5,1), 4)
    zip_code = ''.join(str(random.randint(0, 9)) for _ in range(5))
    json_data = {
        "rating": rating_gen,
        "type": random.choice(types),
        "position": positionAttributes[1],
        "firstName": names.get_first_name(gender="male"), 
        "lastName": names.get_last_name(),
        "homeZipcode": zip_code,
        "archtype": random.choice(archtypes),
        "avatar": avatar_priority[0],
        "attributes": positionAttributes[0],
        "priority": avatar_priority[1]
    }
    data_list.append(json_data)
        
print(str(positionAttributes[2]) + " Players Succesfully Created")
        # print(f"{i} {positionAttributes[1]}")

with open(output_file_path, "w") as output_file:
        json.dump(data_list, output_file, indent=2)

