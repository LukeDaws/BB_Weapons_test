import random

#This is the dictionary that contains all stats for the weapons availabe for comparison.
weapon_dict = {
    "Hammer" : {
        "min_damage" : 40,
        "max_damage" : 70,
        "ignore_armour" : .50,
        "eff_armour" : 1.5,
        "fatigue": 14
    },
    "Goedendag" : {
        "min_damage" : 45,
        "max_damage" : 75,
        "ignore_armour" : .25,
        "eff_armour" : 1.1,
        "fatigue": 14
    },
    "Milita spear": {
        "min_damage" : 25,
        "max_damage" : 30,
        "ignore_armour" : .25,
        "eff_armour" : .90,
        "fatigue": 6
    },
    "Crypt Cleaver": {
        "min_damage" : 60,
        "max_damage" : 80,
        "ignore_armour" : .25,
        "eff_armour" : 1.20,
        "fatigue": 16
    },
    "Fire Lance": {
        "min_damage" : 30,
        "max_damage" : 35,
        "ignore_armour" : .25,
        "eff_armour" : 1.10,
        "fatigue": 12
    },
     "Nomad Mace": {
        "min_damage" : 25,
        "max_damage" : 35,
        "ignore_armour" : .40,
        "eff_armour" : .90,
        "fatigue": 8
    },
    "Light Southern Mace": {
        "min_damage" : 30,
        "max_damage" : 40,
        "ignore_armour" : .40,
        "eff_armour" : 1.10,
        "fatigue": 10
    },
     "Morning Star": {
        "min_damage" : 30,
        "max_damage" : 45,
        "ignore_armour" : .40,
        "eff_armour" : 1.00,
        "fatigue": 10
    }
            
            }      

#Comparison function begins here.
def weapon_comparison(weapon_1, weapon_2):
    #How many turns it took the weapon to get to hp to 0. used for comparison each iteration.
    weapons = {weapon_1: 0,
               weapon_2: 0}
    #Modifiers not in use just yet. but is used to calculate damage.
    modifiers = 1
    #Final stats for display of the weapons. 
    overall = {weapon_1: {
            "weapon name" : weapon_1,
            "wins": 0,
            "fatigue" : 0
            },
               weapon_2: { 
            "weapon name": weapon_2,
            "wins": 0,
            "fatigue" : 0
            }
    }
    #This is to pull the winning weapon out of the dictionary.
    win_max = 0
    #range can be changed for more or less weapon testing.
    for i in range(10000):

        for i in weapons:
            #Change this based on enemy health.
            hp = 55
            #hp = 100
            #Change this for value that will reduce damage.
            armour =  5
            #armour = 460 
            turns = 0
            ignore_armour_percent = weapon_dict[i]["ignore_armour"]
            eff_armour_percent = weapon_dict[i]["eff_armour"]
            while hp > 0:
                while armour > 0:
                    #base damage is recalcualted to simulate different attacks, which changes potential damage.
                    base_damage = random.randrange(weapon_dict[i]["min_damage"],weapon_dict[i]["max_damage"])
                    #All damage formulas are from the battlebrothers wiki.
                    armour_damage = (base_damage * modifiers * eff_armour_percent)
                    armour = armour - armour_damage
                    if armour > 0:
                        hp_damage = base_damage * modifiers * ignore_armour_percent - armour * 0.1
                        hp = hp - hp_damage
                        turns += 1
                    #if armour is destroyed (reduced beyond 0) the remaining damage goes through to damage hp. 
                    else:
                        hp_damage = base_damage * modifiers * (1-ignore_armour_percent) - (armour_damage + armour)
                        hp = hp - hp_damage
                        turns += 1
                #base damage needs to be calcualted here if there is no armour.
                base_damage = random.randrange(weapon_dict[i]["min_damage"],weapon_dict[i]["max_damage"])
                if hp > 0:
                    hp_damage = base_damage * modifiers
                    hp = hp - hp_damage 
                    turns += 1
            weapons[i] = turns
            max_fatigue = turns * weapon_dict[i]["fatigue"]
            if max_fatigue > overall[i]["fatigue"]:
                overall[i]["fatigue"] = max_fatigue
        #compares the each weapon if a weapon has less turns or it's a draw the "wins" variable increases by 1.
        min_turns = min(weapons.values())
        for k, v in weapons.items(): 
            if v==min_turns:
                overall[k]["wins"] += 1 
    #Converts the wins to a percentage and finds the weapon with the highest win percentage.
    for v in overall:
        overall[v]["wins"] = round(overall[v]["wins"]/10000*100,2)
        if overall[v]["wins"] > win_max: 
            win_max = overall[v]["wins"]
            best = v 
    for v in overall:
        if v == best:
            print(overall)
            print(f"\n Best weapon to use overall is {overall[v]}")
            return overall[v]

if __name__ == '__main__':
    weapon_comparison("Morning Star","Light Southern Mace")