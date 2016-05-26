#!/usr/bin/python
import math
import os
import textwrap
from random import randint
from collections import OrderedDict

def menu(lst, question):
    for i in lst:
        print '({}) {}'.format(1+lst.index(i),i)
    return input(question) - 1

def getmodifier(stat):
    stat_mod = math.floor((stat-10)/2)
    if stat_mod >= 0:
        rtn_stat = "+" + str(int(stat_mod))
    else:
        rtn_stat = str(int(stat_mod))
    return rtn_stat

def increasestats(stat,amnt):
    stats[stat] = stats[stat] + amnt

def printstats():
# need to get this to print in the right order. look into 'from collections import OrderedDict'    
    for k,v in stats.items():
        print '{}: {} ({})'.format(k, v, getmodifier(int(v)))
    print ''

def printspells():
    for k,v in spells.items():
        if v:
            print k
            for spell in v:
                print spell
    print '' 

def printh(lst):
    rtn = ''
    for i in lst:
        rtn += i + ', '
    return rtn[:-2]

def printv(lst):
    rtn = ''
    for i in lst:
        rtn += i + '\n\n'
    return rtn

def wraptext(lst):
    rtn = ''
    for i in lst:
        rtn += textwrap.fill(i, width=65, subsequent_indent='    ') + '\n\n'
    return rtn

def printcharacter():
    os.system('clear')
    print '-----------------------------------------------------------------'
    print 'Race: {} \t Subrace: {}'.format(race, subrace)
    print 'Class: {} \t Background: {}'.format(cclass, bg)
    print 'Initiative: {} \t Speed: {}'.format(getmodifier(stats['DEX']), speed)
    print 'Hit Points: {} \t Armour Class: {}'.format(AC, HP)
    print '-----------------------------------------------------------------'
    printstats()
    printspells()
    print '-----------------------------------------------------------------'
    print 'Proficiencies:'
    print '-----------------------------------------------------------------'
    print 'Languages: {}'.format(printh(languages))
    print 'Armour: {}'.format(printh(prof_armour))
    print 'Weapons: {}'.format(printh(prof_weapons))
    print 'Tools: {}'.format(printh(prof_tools))
    print 'Vehicles: {}'.format(printh(prof_vehicles))
    print ''
    print '-----------------------------------------------------------------'
    print 'Traits:'
    print '-----------------------------------------------------------------'
    print wraptext(traits)

stats = OrderedDict()
stats['STR'] = 10
stats['DEX'] = 10
stats['CON'] = 10
stats['INT'] = 10
stats['WIS'] = 10
stats['CHR'] = 10

languages = ['Common']
# skill_proficiencies = []
equipment = []
weapons = []
prof_weapons = []
prof_armour = []
prof_tools = []
prof_vehicles = []
spells = OrderedDict()
spells['Cantrips'] = []
spells['1st Level'] = []
spells['2nd Level'] = []
spells['3rd Level'] = []
spells['4th Level'] = []
spells['5th Level'] = []
spells['6th Level'] = []
spells['7th Level'] = []
spells['8th Level'] = []
spells['9th Level'] = []
traits = []
size = ""
speed = 0
AC = 0
HP = 0
hitdice = ""
subrace = "None"

race_list = ['Aarakocra', 'Dragonborn','Dwarf','Elf','Genasi','Gnome','Goliath','Half-Elf','Half-Orc','Halfling','Human','Tiefling']
dwarf_subraces = ['Hill Dwarf','Mountain Dwarf']
elf_subraces = ['Drow','High Elf','Wood Elf']
genasi_subraces = ['Air Genasi','Earth Genasi','Fire Genasi','Water Genasi']
gnome_subraces = ['Deep Gnome','Forest Gnome','Rock Gnome']
halfling_subraces = ['Lightfoot Halfling','Stout Halfling']

class_list = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard'] 
bg_list = ['Acolyte','Charlatan','Criminal','Entertainer','Folk Hero','Guild Artisan','Hermit','Noble','Outlander','Sage','Sailor','Soldier','Urchin']

race = race_list[menu(race_list, "Choose a race: ")]
if race == "Dwarf":
    subrace = dwarf_subraces[menu(dwarf_subraces, "Choose a subrace: ")]
elif race == "Elf":
    subrace = elf_subraces[menu(elf_subraces, "Choose a subrace: ")]
elif race == "Genasi":
    subrace = genasi_subraces[menu(genasi_subraces, "Choose a subrace: ")]
elif race == "Gnome":
    subrace = gnome_subraces[menu(gnome_subraces, "Choose a subrace: ")]
elif race == "Halfling":
    subrace = halfling_subraces[menu(halfling_subraces, "Choose a subrace: ")]

cclass = class_list[menu(class_list, "Choose a class: ")]
bg = bg_list[menu(bg_list, "Choose a background: ")]

if race == "Aarakocra":
    increasestats('DEX',2)
    increasestats('WIS',1)
    size = "Medium"
    speed = 25
    traits.append('Flight. You have a flying speed of 50ft. To use this speed you can\'t be wearing medium or heavy armour.')
    traits.append('Talons. You are proficient with your unarmed strikes, which deal 1d4 slashing damage on a hit.')
    languages.append('Aarakocra')
    languages.append('Auran')

elif race == "Dragonborn":
    increasestats('STR',2)
    increasestats('CHR',1)
    size = "Medium"
    speed = 30
    # Draconic Ancestry
    # Breath weapon
    # Damage resistance
    languages.append('Draconic')

elif race == "Dwarf":
    increasestats('CON',2)
    size = "Medium"
    speed = 25
    traits.append('Darkvision. 60ft')
    traits.append('Dwarven Resilience. You have advantage on saving throws against poison, and have resistance against poison damage.')
    prof_weapons.append('Battleaxe')
    prof_weapons.append('Handaxe')
    prof_weapons.append('Light Hammer')
    prof_weapons.append('Warhammer')
    dwarven_tools = ['Smith\'s Tools','Brewer\'s Supplies','Mason\'s Tools']
    prof_tools.append(dwarven_tools[menu(dwarven_tools, "Choose a tool proficiency: ")])
    traits.append('Stonecunning. Whenever you make a History check related to the origin of stonework, you are considered proficient in the History skill and add double your profiency bonus, instead of your normal proficiency bonus.')
    languages.append('Dwarvish')
    if subrace == "Hill Dwarf":
        increasestats('WIS',1)
        traits.append('Dwarven Toughness. Your HP maximum increases by 1, and it increases by 1 every time ou gain a level')
        HP = HP + 1
    elif subrace == "Mountain Dwarf":
        increasestats('STR',1)
        prof_armour.append('Light Armour')
        prof_armour.append('Medium Armour')

elif race == "Elf":
    increasestats('DEX',2)
    size = "Medium"
    speed = 30
    traits.append('Darkvision. 60ft')
    # Keen senses. proficiency in Perception
    traits.append('Fey Ancestry. You have advantage on saving throws against being charmed, and magic can\'t put you to sleep.')
    traits.append('Trance. Elves don\'t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day.')
    languages.append('Elvish')
    if subrace == "Drow":
        # traits.append('Darkvision. 120ft') Modify to 120ft
        increasestats('CHR',1)
        traits.append('Sunlight Sensitivity. You had disadvantage on attack rolls and Perception checks that rely on sight when you, the target of your attack, or whatever you are trying to percieve is in direct sunlight.')
        traits.append('Drow Magic. Spellcasting.')
        spells['Cantrips'].append('Dancing Lights')
        # drow weapon training
    elif subrace == "High Elf":
        increasestats('INT',1)
        prof_weapons.append('Shortsword')
        prof_weapons.append('Longsword')
        prof_weapons.append('Shortbow')
        prof_weapons.append('Longbow')
        # Know one additional cantrip
        # Know one additional language
    elif subrace == "Wood Elf":
        increasestats('WIS',1)
        prof_weapons.append('Shortsword')
        prof_weapons.append('Longsword')
        prof_weapons.append('Shortbow')
        prof_weapons.append('Longbow')
        speed = 35
        traits.append('Mask of the Wild. You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist or other natural phenomena.')
elif race == "Genasi":
    increasestats('CON',2)
    size = "Medium"
    speed = 25
    languages.append('Primordial')
    if subrace == "Air Genasi":
        increasestats('DEX',1)
        traits.append('Unending Breath. You can hold your breath indefinitely while you\'re not incapacitated.')
        spells['2nd'].append('Levitate')
        traits.append('Mingle with the Wind. You can cast the Levitate spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.')
    elif subrace == "Earth Genasi":
        increasestats('STR',1)
        traits.append('Earth Walk. You can move across difficult terrian made of earth or stone without expending additional movement.')
        spells['2nd'].append('Pass Without Trace')
        traits.append('Merge with Stone. You can cast the Pass Without Trace spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.')
    elif subrace == "Fire Genasi":
        increasestats('INT',1)
        traits.append('Darkvision. 60ft')
        traits.append('Fire Resistance. You have resistance to fire damage.')
        spells['Cantrips'].append('Produce Flame')
        traits.append('Reach to the Blaze. You can cast the Produce Flame cantrip once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.')
    elif subrace == "Water Genasi":
        increasestats('WIS',1)
        traits.append('Acid Resistance. You have resistance to acid damage.')
        traits.append('Amphibious. You can breath in air and water.')
        traits.append('Swim. You have a swimming speed of 30 feet.')
        spells['Cantrips'].append('Shape Water')
        traits.append('Reach to the Wave. You can cast the Shape Water cantrip once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.')

elif race == "Gnome":
    increasestats('INT',2)
    size = "Small"
    speed = 25
    traits.append('Darkvision. 60ft')
    traits.append('Gnome Cunning. You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.')
    languages.append('Gnomish')
    if subrace == "Deep Gnome":
        increasestats('DEX',1)
        # increase darkvision to 120ft
        traits.append('Stone Camouflage. You have advantage on Stealth checks to hide in rocky terrain.')
        languages.append('Undercommon')
    elif subrace == "Forest Gnome":
        increasestats('DEX',1)
        spells['Cantrips'].append('Minor Illusion')
        traits.append('Speak with Small Beasts. Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets.')
    elif subrace == "Rock Gnome":
        increasestats('CON',1)
        traits.append('Artificier\'s Lore. Whenever you make a History check related to magic items, alchemical objects or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply.')
        prof_tools.append('Tinker\'s Tools')
        traits.append('Tinker. Using Tinker\'s Tools you can spend 1 hour and 10 gp worth of materials to contstruct a Tiny clockwork device (AC 5, 1 HP). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. Refer to PHB page 37 for creation options.')

elif race == "Goliath":
    increasestats('STR',2)
    increasestats('CON',1)
    size = "Medium"
    speed = 30
    # Natural Athlete, proficiency in Athletics
    traits.append('Stone\'s Endurance. You can focus yourself to occasionally shrug off injury. When you take damage, you can use your reaction to roll a d12. Add your Constitution modifier to the number rolled, and reduce the damage by that total. After you use this trait, you can\'t use it again until you finish a short or long rest.')
    traits.append('Powerful Build. You count as one size larger when determining your carrying cpacity and the weight you can push, drag or lift.')
    traits.append('Mountain Born. You\'re acclimated to high altitude, including elevations above 20,000 feet. You\'re also naturally adapted to cold climates.')
    languages.append('Giant')

elif race == "Half-Elf":
    increasestats('CHR',2)
    halfelf_statinc = ['STR','DEX','CON','INT','WIS']
    increasestats(halfelf_statinc[menu(halfelf_statinc, "Choose one stat to add +1 to: ")],1)
    increasestats(halfelf_statinc[menu(halfelf_statinc, "Choose another stat to add +1 to: ")],1)
    size = "Medium"
    speed = 30
    traits.append('Darkvision. 60ft')
    traits.append('Fey Ancestry. You have advantage on saving throws against being charmed, and magic can\'t put you to sleep.')
    # Skill versatility. Gain proficiecy in 2 skills
    languages.append('Elvish')
    # one extra language

elif race == "Half-Orc":
    increasestats('STR',2)
    increasestats('CON',1)
    size = "Medium"
    speed = 30
    traits.append('Darkvision. 60ft')
    # Menacing. Proficiency in Intimidation
    traits.append('Relentless Endurance. When you are reduced to 0 hit points, but not killed outright, you can drop to 1 hit point instead. You can\'t use this feature again until you finish a long rest.')
    traits.append('Savage Attacks. When you score a critical hit with a melee weapon attack, you can roll one of the weapon\'s damage dice one additional time and add it to the extra damage of the critical hit.')
    languages.append('Orcish')

elif race == "Halfling":
    increasestats('DEX',2)
    size = small
    speed = 25
    traits.append('Lucky. When you roll a 1 on the d20 for an attack roll, ability check or saving throw, you can re-roll the die and must use the new roll.')
    traits.append('Brave. You have advantage on saving throws against being frightened.')
    traits.append('Halfling Nimbleness. You cna move through the space of any create that is of a size larger than yours.')
    languages.append('Halfling')
    if subrace == "Lightfoot Halfling":
        increasestats('CHR',1)
        traits.append('Naturally Stealthy. You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.')
    elif subrace == "Stout Halfling":
        increasestats('CON',1)
        traits.append('Stout Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage.')

elif race == "Human":
    increasestats('STR',1)
    increasestats('DEX',1)
    increasestats('CON',1)
    increasestats('INT',1)
    increasestats('WIS',1)
    increasestats('CHR',1)
    size = "Medium"
    speed = 30
    # plus one language

elif race == "Tiefling":
    increasestats('CHR',2)
    increasestats('INT',1)
    size = "Medium"
    speed = 30
    traits.append('Darkvision. 60ft')
    traits.append('Hellish Resistance. You have resistance to fire damage.')
    spells['Cantrips'].append('Thaumaturgy')
    languages.append('Infernal')

printcharacter()
# print 'Known languages: {}'.format(languages)