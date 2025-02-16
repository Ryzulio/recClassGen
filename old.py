
import os
import json
import random
import names
import time


start = time.time()
rec_year = (input("Recruiting Class Year: "))
print("Recommended Amount: 3000-3600")
players_to_create = int(input("Player Amount: "))
output_file_name = f"{rec_year}.json"
output_file_path = os.path.join(os.path.dirname(__file__), output_file_name)
def attr_gen_calc():
    players_created = 0
# Initial Randomization
    while True:
        x = {
                "year": 2022, 
                "durability": random.randint(55,99),
                "potential": random.randint(55,99),
                "height": random.randint(67,80),
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
        TE_Calc = (2.35*(x["passBlocking"] + x["runBlocking"] + x["routeRunning"]) + (x["strength"] + x["speed"]))/5
        OL_Calc = (2*(x["passBlocking"]+ x["runBlocking"]) + 1.25*(x["strength"]))/3
        DL_Calc = (2*(x['blockShedding'] + x['tackling'] + x['pursuit']) + 1.75*(x["defensiveIq"] + x["strength"]))/5
        LB_Calc = ((x['blockShedding'] + x['defensiveIq'] + x['tackling'] + x['pursuit'] + x['manCoverage'] + x['zoneCoverage']))/3.25
        CB_Calc = (2.75*(x["manCoverage"] + x["zoneCoverage"]) + 1.25*(x['defensiveIq'] + x["tackling"]) + 1.5*(x["speed"]))/5
        S_Calc = (2.9*(x['defensiveIq'] + x['tackling']) + 2*(x['manCoverage'] + x['zoneCoverage']) + 1.3*(x['speed'] + x['strength'] + x['evasion']))/7
        K_Calc = ((x['kickAccuracy'] + x['kickPower'] + x['puntAccuracy'] + x['puntPower']))/2.25
# QB
        if(QB_Calc >= RB_Calc and QB_Calc >= WR_Calc and QB_Calc >= TE_Calc and QB_Calc >= OL_Calc and QB_Calc >= DL_Calc and QB_Calc >= LB_Calc and QB_Calc  >= CB_Calc and QB_Calc >= S_Calc and QB_Calc >= K_Calc):
            
            y = "QB"
            x['accuracy'] = random.randint(60,85) 
            x['armStrength'] = random.randint(60,85)
            x['passIq'] = random.randint(60,85)
            x['weight'] = random.randint(190,220)
            x['height']= random.randint(70,78)
            
            if((x["speed"] + x["evasion"] + x["ballCarrierVision"])/3 >= (x["accuracy"] + x['passIq'] + x['armStrength'])/3 +10):
                archetype = 'dual-threat'
            elif((x["speed"] + x["evasion"] + x["ballCarrierVision"])/3 +10 <=  x['armStrength']+5):
                archetype = 'gunslinger'
            elif((x["speed"] + x["evasion"] + x["ballCarrierVision"])/3 +10 <= (x["accuracy"] + x['passIq'] + x['armStrength'])/3):
                archetype='field-general'
            else: 
                archetype='balanced'
                
# WR
        elif(WR_Calc > RB_Calc and WR_Calc > TE_Calc and WR_Calc > OL_Calc and WR_Calc > DL_Calc and WR_Calc > LB_Calc and WR_Calc > CB_Calc and WR_Calc > S_Calc and WR_Calc > K_Calc):
            y = "WR"
            archetype = 'balanced'
            x["speed"] = random.randint(65,110)
            x['weight'] = random.randint(180,230)
            x['height']= random.randint(67,76)
# RB
        elif(RB_Calc > TE_Calc and RB_Calc > OL_Calc and RB_Calc > DL_Calc and RB_Calc > LB_Calc and RB_Calc > CB_Calc and RB_Calc > S_Calc and RB_Calc > K_Calc): 
            y = "RB"
            archetype = 'balanced'
            x['weight'] = random.randint(180,230)
            x['height']= random.randint(66,73)
# TE
        elif(TE_Calc > OL_Calc and TE_Calc > DL_Calc and TE_Calc > LB_Calc and TE_Calc > CB_Calc and TE_Calc > S_Calc and TE_Calc > K_Calc): 
            y= "TE"
            archetype = 'balanced'
            x['weight'] = random.randint(220,260)
            x['height']= random.randint(72,77)
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
            x['weight'] = random.randint(270,350)
            x['height']= random.randint(76,82)
            y="OL"
            archetype = 'balanced'
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
            x['weight'] = random.randint(270,350)
            x['height']= random.randint(76,82)
            y="DL"
            archetype = 'balanced'
        elif(LB_Calc> CB_Calc and LB_Calc > S_Calc and LB_Calc > K_Calc):
            y = "LB"
            archetype = 'balanced'
            x['weight'] = random.randint(230,270)
            x['height']= random.randint(70,75)
            x['speed'] = random.randint(60,80)
        elif(CB_Calc > S_Calc and CB_Calc > K_Calc):
            y="CB"
            archetype = 'balanced'
            x['weight'] = random.randint(180,230)
            x['height']= random.randint(69,75)
        elif(S_Calc > K_Calc):
            y= "S"
            archetype = 'balanced'
            x['weight'] = random.randint(185,235)
            x['height']= random.randint(70,76)
        else:
            y="K"
            archetype = 'balanced'
            x['weight'] = random.randint(180,210)
            x['height']= random.randint(66,73)
            
        if(players_created == players_to_create):
            print("Player Created")
            break
        else:        
            players_created = players_created +1
             
    pos_and_attr = (x,y,archetype,players_created)
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

data_list = []
for i in range(players_to_create):
    avatar_priority = priority_avatar_gen()
    positionAttributes = attr_gen_calc()
    rating_gen = round(random.uniform(.1,1), 4)
    zip_code = ''.join(str(random.randint(0, 9)) for _ in range(5))
    json_data = {
        "rating": rating_gen,
        "type": random.choice(types),
        "position": positionAttributes[1],
        "firstName": names.get_first_name(gender="male"), 
        "lastName": names.get_last_name(),
        "homeZipcode": zip_code,
        "archetype": positionAttributes[2],
        "avatar": avatar_priority[0],
        "attributes": positionAttributes[0],
        "priority": avatar_priority[1]
    }           
    data_list.append(json_data)
    
end = time.time()
print(str(positionAttributes[3]) + " Players Succesfully Created")
print(str(end-start) + " Time Elapsed")

with open(output_file_path, "w") as output_file:
        json.dump(data_list, output_file, indent=2)

