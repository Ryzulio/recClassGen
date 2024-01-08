
import os
import json
import random
import names
import asyncio


# rec_year = input("Recruiting Class Year: ")
# players_to_create = input("Player Amount: ")
output_file_name = "results.json"
output_file_path = os.path.join(os.path.dirname(__file__), output_file_name)
def attr_gen_calc(attr):
    x = {
                "year": 2022, 
                "durability": round(random.uniform(40,120),0),
                "potential": round(random.uniform(40,120),0 ),
                "height": round(random.uniform(65,75),0 ),
                "weight": round(random.uniform(180,350),0 ),
                "speed": round(random.uniform(40,100),0 ),
                "evasion": round(random.uniform(40,100),0 ),
                "strength": round(random.uniform(40,100),0 ),
                "armStrength": round(random.uniform(40,100),0 ),
                "accuracy": round(random.uniform(40,100),0 ),
                "passIq": round(random.uniform(40,100),0 ),
                "catching": round(random.uniform(40,100),0 ),
                "routeRunning": round(random.uniform(40,100),0 ),
                "ballSecurity": round(random.uniform(40,100),0 ),
                "ballCarrierVision": round(random.uniform(40,100),0 ),
                "runBlocking": round(random.uniform(50,100),0 ),
                "passBlocking": round(random.uniform(50,100),0 ),
                "tackling": round(random.uniform(40,100),0 ),
                "manCoverage": round(random.uniform(40,100),0 ),
                "zoneCoverage": round(random.uniform(40,100),0 ),
                "blockShedding": round(random.uniform(40,100),0 ),
                "pursuit": round(random.uniform(40,100),0 ),
                "defensiveIq": round(random.uniform(40,100),0 ),
                "kickPower": round(random.uniform(40,100),0 ),
                "kickAccuracy": round(random.uniform(40,100),0 ),
                "puntPower": round(random.uniform(40,100),0 ),
                "puntAccuracy": round(random.uniform(40,100),0 )
            }
    QB_Calc = ((3.25*(x["armStrength"] + x["accuracy"] + x["passIq"])) + 1.25*(x["speed"] + x["evasion"] + x["ballCarrierVision"]))/6
    RB_Calc = (4.25*(x["speed"] + x["evasion"] + x["strength"]) + (x["routeRunning"] + x["ballSecurity"] + x["catching"] +  x["ballCarrierVision"]) + (x["passBlocking"]+x["runBlocking"]))/8
    WR_Calc = (3*(x["routeRunning"] + x["catching"])+2*(x["evasion"] + x["ballCarrierVision"] +x["speed"]))/5
    TE_Calc = (2.75*(x["passBlocking"] + x["runBlocking"] + x["routeRunning"]) + 1.5*(x["strength"] + x["speed"]))/5
    OL_Calc = (2*(x["passBlocking"]+ x["runBlocking"] + 1.25*(x["strength"])))/3

# QB
    if(QB_Calc >= RB_Calc and QB_Calc >= WR_Calc and QB_Calc >= TE_Calc and QB_Calc >= OL_Calc):
        y = "QB"
        QB_Calc = str(QB_Calc)
        print(QB_Calc +" " + y)

# WR
    elif(WR_Calc>=RB_Calc and WR_Calc >= TE_Calc and WR_Calc >= OL_Calc):
        y = "WR"
        x.update({"speed":90})
        print(x["speed"])
        WR_Calc = str(WR_Calc)
        print(WR_Calc + " " + y) 
# RB
    elif(RB_Calc >= TE_Calc and RB_Calc >= OL_Calc): 
        y = "RB"
        RB_Calc = str(RB_Calc)
        print(RB_Calc + " " + y) 
# TE
    elif(TE_Calc >= OL_Calc): 
        y= "TE"
        TE_Calc = str(TE_Calc)
        print(TE_Calc + " " + y)
# OL
    else:
        x["manCoverage"] = round(random.uniform(20,60),0)
        x["zoneCoverage"] = round(random.uniform(20,60),0)
        x["blockShedding"] = round(random.uniform(20,60),0)
        x["pursuit"] = round(random.uniform(20,60),0)
        x["armStrength"] = round(random.uniform(20,60),0)
        x["accuracy"] = round(random.uniform(20,60),0)
        x["kickPower"] = round(random.uniform(20,60),0)
        x["puntPower"] = round(random.uniform(20,60),0)
        x["tackle"] = round(random.uniform(20,60),0)
        y="OL"
        OL_Calc = str(OL_Calc)
        print(OL_Calc + " " + y)
    
    if(attr==1):
        return x 
    else:
        return y

    

types = ["HS", "JUCO"]
positions = ["RB", "QB", "WR", "TE", "OL","DL","K","S","CB"]
# home_zipcodes = [1, 2]
archtypes = ["a", "b"]
avatars = ["a", "b"]
# attributes = ["a", "b"]
priorities = ["a", "b"]

data_list = []
max_length = max( len(types), len(positions), len(archtypes), len(avatars))
attr_gen_calc(attr=0)
for i in range(25):
        rating_gen = round(random.uniform(.5,1), 4)
        zip_code = ''.join(str(random.randint(0, 9)) for _ in range(5))
        json_data = {
            "rating": rating_gen,
            "type": random.choice(types),
            "position": (attr_gen_calc(attr=0)),
            "firstName": names.get_first_name(gender="male"), 
            "lastName": names.get_last_name(),
            "homeZipcode": zip_code,
            "archtype": random.choice(archtypes),
            "avatar": random.choice(avatars),
            "attributes": (attr_gen_calc(attr=1)),
            "priority": random.choice(priorities)
        }
        data_list.append(json_data)


with open(output_file_path, "w") as output_file:
        json.dump(data_list, output_file, indent=2)



