
import os
import json
import random
import names
import time
from collections import Counter

# rec_year = input("Recruiting Class Year: ")
# players_to_create = input("Player Amount: ")
output_file_name = "results.json"
output_file_path = os.path.join(os.path.dirname(__file__), output_file_name)

def attr_gen_calc():
# Initial Randomization
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
    QB_Calc = ((3.25*(x["armStrength"] + x["accuracy"] + x["passIq"])) + (x["speed"] + x["evasion"] + x["ballCarrierVision"]))/6
    RB_Calc = (4*(x["speed"] + x["evasion"] + x["strength"]) + (x["routeRunning"] + x["ballSecurity"] + x["catching"] +  x["ballCarrierVision"]) + (x["passBlocking"]+x["runBlocking"]))/8
    WR_Calc = (3*(x["routeRunning"] + x["catching"]) + 1.5*(x["evasion"] + x["ballCarrierVision"] + x["speed"]))/5
    TE_Calc = (2.75*(x["passBlocking"] + x["runBlocking"] + x["routeRunning"]) + 1.5*(x["strength"] + x["speed"]))/5
    OL_Calc = (2.5*(x["passBlocking"]+ x["runBlocking"]) + 1.25*(x["strength"]))/3

# QB
    if(QB_Calc >= RB_Calc and QB_Calc >= WR_Calc and QB_Calc >= TE_Calc and QB_Calc >= OL_Calc):
        y = "QB"
        # QB_Calc = str(QB_Calc)
        # print(QB_Calc +" " + y)

# WR
    elif(WR_Calc > RB_Calc and WR_Calc > TE_Calc and WR_Calc > OL_Calc):
        y = "WR"
        x["speed"] = random.randint(65,110)
        # WR_Calc = str(WR_Calc)
        # print(WR_Calc + " " + y) 
# RB
    elif(RB_Calc > TE_Calc and RB_Calc > OL_Calc): 
        y = "RB"
        # amount_of_rb = amount_of_rb + 1
        # print(str(amount_of_rb) + " Running Backs Generated")
# TE
    elif(TE_Calc > OL_Calc): 
        y= "TE"
        
        # amount_of_te = 0
        # amount_of_te = amount_of_te + 1
        # print(str(amount_of_te) + " Tigt Ends Generated")
# OL
    else:
        x["manCoverage"] = random.randint(20,60)
        x["zoneCoverage"] = random.randint(20,60)
        x["blockShedding"] = random.randint(20,60)
        x["pursuit"] = random.randint(20,60)
        x["armStrength"] = random.randint(20,60)
        x["accuracy"] = random.randint(20,60)
        x["kickPower"] = random.randint(20,60)
        x["puntPower"] = random.randint(20,60)
        x["tackle"] = random.randint(20,60)
        x["speed"] = random.randint(20,60)
        y="OL"
    
    pos_and_attr = (x,y)
    return pos_and_attr

types = ["HS", "JUCO"]
archtypes = ["a", "b"]
avatars = ["a", "b"]
priorities = ["a", "b"]

data_list = []
# JSON File Writing
for i in range(25):
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
            "avatar": random.choice(avatars),
            "attributes": positionAttributes[0],
            "priority": random.choice(priorities)
        }
        data_list.append(json_data)


with open(output_file_path, "w") as output_file:
        json.dump(data_list, output_file, indent=2)

