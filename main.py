import os
import json
import numpy as np
import names
import random
import time

# numpy 
rng = np.random.default_rng()

# Other Variables 
create_string = input("How many players do you want to create? ")
year = input("What recruting year? ")
start = time.time()
output_file_name = "testing.json"
output_file_path = os.path.join(os.path.dirname(__file__), output_file_name)
types = ["HS", "JUCO"]  
data_list = []

# Get players to create + sort them into a respective position
def init():

    create = int(create_string)
    global qbs_to_create
    qbs_to_create = create / 20
    global rbs_to_create
    rbs_to_create = create / 9
    global wrs_to_create
    wrs_to_create = create / 6
    global te_to_create
    te_to_create = create / 10
    global ol_to_create
    ol_to_create = create / 6
    global dl_to_create
    dl_to_create = create / 6 
    global lb_to_create
    lb_to_create = create / 4
    global db_to_create
    db_to_create = create / 6
    global s_to_create
    s_to_create = create / 9
    global k_to_create
    k_to_create = create / 20
    

def qb_creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(70,79)),
        "weight":int(rng.integers(195,230)),
        "speed": int(rng.integers(55,85)),
        "evasion": int(rng.integers(60,105)),
        "strength": int(rng.integers(55,85)),
        "armStrength": int(rng.integers(55,105)),
        "accuracy":int(rng.integers(55,105)),
       "passIq": int(rng.integers(55,105)),
        "catching":  int(rng.integers(30,75)),
        "routeRunning":  int(rng.integers(30,75)),
        "ballSecurity": int(rng.integers(55,85)),
        "ballCarrierVision": int(rng.integers(55,85)),
        "runBlocking":  int(rng.integers(30,75)),
        "passBlocking":  int(rng.integers(30,75)),
        "tackling":  int(rng.integers(30,75)),
        "manCoverage":  int(rng.integers(30,75)),
        "zoneCoverage":  int(rng.integers(30,75)),
        "blockShedding":  int(rng.integers(30,75)),
        "pursuit":  int(rng.integers(30,75)),
        "defensiveIq":  int(rng.integers(30,75)),
        "kickPower":  int(rng.integers(30,70)),
        "kickAccuracy":  int(rng.integers(30,60)),
        "puntPower":  int(rng.integers(30,60)),
        "puntAccuracy":  int(rng.integers(30,60))   
    }
    print(str(qbs_to_create) + " QBs Generated")  
    return x

def rb_creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(65,74)),
        "weight":int(rng.integers(180,230)),
        "speed": int(rng.integers(55,105)),
        "evasion": int(rng.integers(55,105)),
        "strength": int(rng.integers(55,105)),
        "armStrength": int(rng.integers(55,70)),
        "accuracy":int(rng.integers(55,70)),
       "passIq": int(rng.integers(55,70)),
        "catching":  int(rng.integers(55,80)),
        "routeRunning":  int(rng.integers(55,75)),
        "ballSecurity": int(rng.integers(65,100)),
        "ballCarrierVision": int(rng.integers(55,95)),
        "runBlocking":  int(rng.integers(30,85)),
        "passBlocking":  int(rng.integers(30,85)),
        "tackling":  int(rng.integers(30,75)),
        "manCoverage":  int(rng.integers(30,75)),
        "zoneCoverage":  int(rng.integers(30,75)),
        "blockShedding":  int(rng.integers(30,75)),
        "pursuit":  int(rng.integers(30,75)),
        "defensiveIq":  int(rng.integers(30,75)),
        "kickPower":  int(rng.integers(30,75)),
        "kickAccuracy":  int(rng.integers(30,75)),
        "puntPower":  int(rng.integers(30,75)),
        "puntAccuracy":  int(rng.integers(30,75))   
    }
    print(str(rbs_to_create) + " RBs Generated")
    return x

def wr_creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(69,77)),
        "weight":int(rng.integers(180,230)),
        "speed": int(rng.integers(55,105)),
        "evasion": int(rng.integers(55,105)),
        "strength": int(rng.integers(55,80)),
        "armStrength": int(rng.integers(55,70)),
        "accuracy":int(rng.integers(55,70)),
       "passIq": int(rng.integers(55,70)),
        "catching":  int(rng.integers(55,80)),
        "routeRunning":  int(rng.integers(55,105)),
        "ballSecurity": int(rng.integers(65,100)),
        "ballCarrierVision": int(rng.integers(55,95)),
        "runBlocking":  int(rng.integers(30,70)),
        "passBlocking":  int(rng.integers(30,70)),
        "tackling":  int(rng.integers(30,75)),
        "manCoverage":  int(rng.integers(30,75)),
        "zoneCoverage":  int(rng.integers(30,75)),
        "blockShedding":  int(rng.integers(30,75)),
        "pursuit":  int(rng.integers(30,75)),
        "defensiveIq":  int(rng.integers(30,75)),
        "kickPower":  int(rng.integers(30,75)),
        "kickAccuracy":  int(rng.integers(30,75)),
        "puntPower":  int(rng.integers(30,75)),
        "puntAccuracy":  int(rng.integers(30,75))   
    }
    print(str(wrs_to_create) + " WRs Generated")
    return x

def te_creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(74,78)),
        "weight":int(rng.integers(220,260)),
        "speed": int(rng.integers(55,75)),
        "evasion": int(rng.integers(55,75)),
        "strength": int(rng.integers(55,90)),
        "armStrength": int(rng.integers(55,70)),
        "accuracy":int(rng.integers(55,70)),
       "passIq": int(rng.integers(55,70)),
        "catching":  int(rng.integers(60,75)),
        "routeRunning":  int(rng.integers(55,75)),
        "ballSecurity": int(rng.integers(65,80)),
        "ballCarrierVision": int(rng.integers(55,80)),
        "runBlocking":  int(rng.integers(60,90)),
        "passBlocking":  int(rng.integers(60,90)),
        "tackling":  int(rng.integers(30,60)),
        "manCoverage":  int(rng.integers(30,60)),
        "zoneCoverage":  int(rng.integers(30,60)),
        "blockShedding":  int(rng.integers(30,60)),
        "pursuit":  int(rng.integers(30,60)),
        "defensiveIq":  int(rng.integers(30,60)),
        "kickPower":  int(rng.integers(30,60)),
        "kickAccuracy":  int(rng.integers(30,60)),
        "puntPower":  int(rng.integers(30,60)),
        "puntAccuracy":  int(rng.integers(30,60))   
    }
    print(str(te_to_create) + " TEs Generated")
    return x    

def ol_creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(71,84)),
        "weight":int(rng.integers(250,350)),
        "speed": int(rng.integers(30,60)),
        "evasion": int(rng.integers(30,60)),
        "strength": int(rng.integers(55,90)),
        "armStrength": int(rng.integers(30,60)),
        "accuracy":int(rng.integers(30,60)),
       "passIq": int(rng.integers(30,60)),
        "catching":  int(rng.integers(55,80)),
        "routeRunning":  int(rng.integers(55,75)),
        "ballSecurity": int(rng.integers(30,60)),
        "ballCarrierVision": int(rng.integers(30,50)),
        "runBlocking":  int(rng.integers(55,90)),
        "passBlocking":  int(rng.integers(55,90)),
        "tackling":  int(rng.integers(30,50)),
        "manCoverage":  int(rng.integers(30,50)),
        "zoneCoverage":  int(rng.integers(30,50)),
        "blockShedding":  int(rng.integers(30,50)),
        "pursuit":  int(rng.integers(30,50)),
        "defensiveIq":  int(rng.integers(30,50)),
        "kickPower":  int(rng.integers(30,50)),
        "kickAccuracy":  int(rng.integers(30,50)),
        "puntPower":  int(rng.integers(30,50)),
        "puntAccuracy":  int(rng.integers(30,50))   
    }
    print(str(ol_to_create) + " OL Generated")
    return x

def dl_creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(70,82)),
        "weight":int(rng.integers(270,380)),
        "speed": int(rng.integers(30,70)),
        "evasion": int(rng.integers(30,70)),
        "strength": int(rng.integers(50,85)),
        "armStrength": int(rng.integers(30,40)),
        "accuracy":int(rng.integers(30,40)),
       "passIq": int(rng.integers(30,40)),
        "catching":  int(rng.integers(55,80)),
        "routeRunning":  int(rng.integers(30,60)),
        "ballSecurity": int(rng.integers(30,60)),
        "ballCarrierVision": int(rng.integers(30,60)),
        "runBlocking":  int(rng.integers(30,60)),
        "passBlocking":  int(rng.integers(30,60)),
        "tackling":  int(rng.integers(45,80)),
        "manCoverage":  int(rng.integers(30,70)),
        "zoneCoverage":  int(rng.integers(30,70)),
        "blockShedding":  int(rng.integers(55,85)),
        "pursuit":  int(rng.integers(50,88)),
        "defensiveIq":  int(rng.integers(50,85)),
        "kickPower":  int(rng.integers(30,60)),
        "kickAccuracy":  int(rng.integers(30,60)),
        "puntPower":  int(rng.integers(30,60)),
        "puntAccuracy":  int(rng.integers(30,60))   
    }
    print(str(dl_to_create) + " DL Generated")
    return x

def lb__creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(70,77)),
        "weight":int(rng.integers(200,260)),
        "speed": int(rng.integers(50,85)),
        "evasion": int(rng.integers(40,70)),
        "strength": int(rng.integers(50,85)),
        "armStrength": int(rng.integers(30,40)),
        "accuracy":int(rng.integers(30,40)),
       "passIq": int(rng.integers(30,40)),
        "catching":  int(rng.integers(55,80)),
        "routeRunning":  int(rng.integers(30,50)),
        "ballSecurity": int(rng.integers(30,50)),
        "ballCarrierVision": int(rng.integers(30,50)),
        "runBlocking":  int(rng.integers(30,50)),
        "passBlocking":  int(rng.integers(30,50)),
        "tackling":  int(rng.integers(45,80)),
        "manCoverage":  int(rng.integers(40,75)),
        "zoneCoverage":  int(rng.integers(40,75)),
        "blockShedding":  int(rng.integers(55,85)),
        "pursuit":  int(rng.integers(50,88)),
        "defensiveIq":  int(rng.integers(50,85)),
        "kickPower":  int(rng.integers(30,60)),
        "kickAccuracy":  int(rng.integers(30,60)),
        "puntPower":  int(rng.integers(30,60)),
        "puntAccuracy":  int(rng.integers(30,60))   
    }
    print(str(lb_to_create) + " LBs Generated")
    return x

def db_creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(68,75)),
        "weight":int(rng.integers(180,220)),
        "speed": int(rng.integers(65,85)),
        "evasion": int(rng.integers(40,70)),
        "strength": int(rng.integers(50,85)),
        "armStrength": int(rng.integers(30,40)),
        "accuracy":int(rng.integers(30,40)),
       "passIq": int(rng.integers(30,40)),
        "catching":  int(rng.integers(55,80)),
        "routeRunning":  int(rng.integers(30,50)),
        "ballSecurity": int(rng.integers(30,50)),
        "ballCarrierVision": int(rng.integers(30,50)),
        "runBlocking":  int(rng.integers(30,50)),
        "passBlocking":  int(rng.integers(30,50)),
        "tackling":  int(rng.integers(45,65)),
        "manCoverage":  int(rng.integers(55,90)),
        "zoneCoverage":  int(rng.integers(55,90)),
        "blockShedding":  int(rng.integers(55,70)),
        "pursuit":  int(rng.integers(50,75)),
        "defensiveIq":  int(rng.integers(50,85)),
        "kickPower":  int(rng.integers(30,60)),
        "kickAccuracy":  int(rng.integers(30,60)),
        "puntPower":  int(rng.integers(30,60)),
        "puntAccuracy":  int(rng.integers(30,60))   
    }
    print(str(db_to_create) + " CBs Generated")
    return x

def s_creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(70,77)),
        "weight":int(rng.integers(200,240)),
        "speed": int(rng.integers(60,85)),
        "evasion": int(rng.integers(50,70)),
        "strength": int(rng.integers(50,85)),
        "armStrength": int(rng.integers(30,40)),
        "accuracy":int(rng.integers(30,40)),
       "passIq": int(rng.integers(30,40)),
        "catching":  int(rng.integers(55,80)),
        "routeRunning":  int(rng.integers(30,50)),
        "ballSecurity": int(rng.integers(30,50)),
        "ballCarrierVision": int(rng.integers(30,50)),
        "runBlocking":  int(rng.integers(30,50)),
        "passBlocking":  int(rng.integers(30,50)),
        "tackling":  int(rng.integers(55,80)),
        "manCoverage":  int(rng.integers(40,80)),
        "zoneCoverage":  int(rng.integers(40,80)),
        "blockShedding":  int(rng.integers(55,80)),
        "pursuit":  int(rng.integers(55,88)),
        "defensiveIq":  int(rng.integers(55,85)),
        "kickPower":  int(rng.integers(30,60)),
        "kickAccuracy":  int(rng.integers(30,60)),
        "puntPower":  int(rng.integers(30,60)),
        "puntAccuracy":  int(rng.integers(30,60))   
    }
    print(str(s_to_create) + " S Generated")
    return x

def k_creator():
    x = {
         "year": year, 
        "durability": int(rng.integers(55,99)),
        "potential":int(rng.integers(55,99)),
        "height": int(rng.integers(68,75)),
        "weight":int(rng.integers(180,205)),
        "speed": int(rng.integers(50,60)),
        "evasion": int(rng.integers(40,60)),
        "strength": int(rng.integers(50,60)),
        "armStrength": int(rng.integers(30,40)),
        "accuracy":int(rng.integers(30,40)),
       "passIq": int(rng.integers(30,40)),
        "catching":  int(rng.integers(40,55)),
        "routeRunning":  int(rng.integers(30,50)),
        "ballSecurity": int(rng.integers(30,50)),
        "ballCarrierVision": int(rng.integers(30,50)),
        "runBlocking":  int(rng.integers(30,50)),
        "passBlocking":  int(rng.integers(30,50)),
        "tackling":  int(rng.integers(45,50)),
        "manCoverage":  int(rng.integers(40,50)),
        "zoneCoverage":  int(rng.integers(40,50)),
        "blockShedding":  int(rng.integers(40,50)),
        "pursuit":  int(rng.integers(30,50)),
        "defensiveIq":  int(rng.integers(40,50)),
        "kickPower":  int(rng.integers(55,85)),
        "kickAccuracy":  int(rng.integers(55,90)),
        "puntPower":  int(rng.integers(55,85)),
        "puntAccuracy":  int(rng.integers(55,90))   
    }
    print(str(k_to_create) + " Ks Generated")
    return x

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
    facialHair_list = [" int(rng.integers(30,75))", "Light beard", "Medium beard", "Majestic beard", "Moustache", "Fancy moustache"]
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

def loop(positionAttributes, position, position_to_create):
    amount_in_position = int(position_to_create)
    for i in range(amount_in_position):
        avatar_priority = priority_avatar_gen()
        zip_code = ''.join(str(rng.integers(low = 0, high=9)) for _ in range(5))
        rating = rng.random()
        json_data = {
            "rating": rating,
            "type": random.choice(types),
            "position": position,
            "firstName": names.get_first_name(gender="male"), 
            "lastName": names.get_last_name(),
            "homeZipcode": zip_code,
            "archetype":  "N/A",
            "avatar": avatar_priority[0],
            "attributes": positionAttributes,
            "priority": avatar_priority[1]
        }           
        data_list.append(json_data)

# Function Calls
init()
# Position Attributes Variables
qb = qb_creator()
rb = rb_creator()
wr = wr_creator()
te = te_creator()
ol = ol_creator()
dl = dl_creator()
lb = lb__creator()
db = db_creator()
s = s_creator()
k = k_creator()

# Generation Loops

try: 
    loop(qb, "QB", qbs_to_create)
    loop(rb, "RB", rbs_to_create)
    loop(wr, "WR", wrs_to_create)
    loop(te, "TE", te_to_create)
    loop(ol, "OL", ol_to_create)
    loop(dl, "DL", dl_to_create)
    loop(lb, "LB", lb_to_create)
    loop(db, "CB", db_to_create)
    loop(s, "S", s_to_create)
    loop(k, "K", k_to_create) 
except Exception as e:
    print("Generation Failed: " + e)
finally: 
    end = time.time()
    print(str(end-start) + " Time Elapsed")
    print("All players succesfully generated.")

# Creating JSON File
with open(output_file_path, "w") as output_file:
        json.dump(data_list, output_file, indent=2)
