This is to create a web app so that I can compare different weapons in the game battle brothers. 

Currently the web app only shows the weapons and their stats. 

The python file "BB_Weapon_Test.py" does the actual comparison. It involves setting the armour and HP of the creature you are attacking and then it will see how many turns it would take to kill that creature per weapon. The wepaon that takes the least amount of turns is considered better. 

Since the weapons have a damage range, for each swing of the weapon the damage is randomised. So sometimes one weapon can beat another one and then running the simulation again, the results could be oposite. Hence the simulation is run multiple times and then a percentage of the amount of times a weapon won is listed. The weapon with the highest win percetage is consider a better weapon.

It is assumed that the weapon will hit everytime and it also doesn't take into account perks.

All damage calcualtions and how armour effects the formulas have been taken from the [battle brothers wiki page](https://battlebrothers.fandom.com/wiki/Combat_Mechanics#Damage).
