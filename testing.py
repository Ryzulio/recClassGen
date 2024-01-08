
import os
import random

def attr_gen():
    x: {
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
    y=0
    if(y==0):
        print("OL Before" + x)
        y+1
    else:
        x.pop("passBlocking")
        x.create
    
    return x
    

