from random import randint

classh = open('homebrew_classes.txt', 'r')
raceh = open ('homebrew_races.txt', 'r')

# tuples containing possibilities for character names
bnames = ('Noah', 'Liam', 'Jacob', 'Mason', 'William', 'Ethan', 'Michael', 'Alexander', 'Jayden', 'Daniel', 'Elijah', 'Aiden', 'James', 'Benjamin', 'Matthew', 'Jackson', 'Logan', 'David', 'Anthony', 'Joseph', 'Joshua', 'Andrew', 'Lucas', 'Gabriel', 'Samuel', 'Christopher', 'John', 'Dylan', 'Isaac', 'Ryan', 'Nathan', 'Carter', 'Caleb', 'Luke', 'Christian', 'Hunter', 'Henry', 'Owen', 'Landon', 'Jack', 'Wyatt', 'Jonathan', 'Eli', 'Isaiah', 'Sebastian', 'Jaxon', 'Julian', 'Brayden', 'Gavin', 'Levi')
gnames = ('Sophia', 'Emma', 'Olivia', 'Isabella', 'Ava', 'Mia', 'Emily', 'Abigail', 'Madison', 'Elizabeth', 'Charlotte', 'Avery', 'Sofia', 'Chloe', 'Ella', 'Harper', 'Amelia', 'Aubrey', 'Addison', 'Evelyn', 'Natalie', 'Grace', 'Hannah', 'Zoey', 'Victoria', 'Lillian', 'Lily', 'Brooklyn', 'Samantha', 'Layla', 'Zoe', 'Audrey', 'Leah', 'Allison', 'Anna', 'Aaliyah', 'Savannah', 'Gabriella', 'Camila', 'Aria', 'Kaylee', 'Scarlett', 'Hailey', 'Arianna', 'Riley', 'Alexis', 'Nevaeh', 'Sarah', 'Claire', 'Sadie')
lnames = ('Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins')

# Possibilities for classes
c_options = ['Ardent', 'Barbarian', 'Bard', 'Beguiler', 'Cleric', 'Crusader', 'Divine Mind', 'Dragon Shaman', 'Druid', 'Dusk Blade', 'Favored Soul', 'Fighter', 'Hexblade', 'Knight', 'Lurk', 'Monk', 'Ninja', 'Paladin', 'Psion', 'Psychic Warrior', 'Ranger', 'Rogue', 'Samurai', 'Scout', 'Shugenja', 'Sorcerer', 'Soul Knife', 'Spell Thief', 'Spirit Shaman', 'Swashbuckler', 'Swordsage', 'Warblade', 'Warlock', 'Warmage', 'Wilder', 'Wizard', 'Wu Jen']
npcs = ['Adept', 'Adept:6', 'Adept:0', 'Adept:2', 'Adept:0', 'Adept:0', 'Adept:2', 'Adept:5', 'Adept:2', 'Adept:3', 'Adept:1', 'Adept:4', 'Adept:6', 'Adept:DMG I pg 107', 'Aristocrat', 'Aristocrat:8', 'Aristocrat:0', 'Aristocrat:4', 'Aristocrat:0', 'Aristocrat:0', 'Aristocrat:2', 'Aristocrat:6', 'Aristocrat:1', 'Aristocrat:3', 'Aristocrat:2', 'Aristocrat:5', 'Aristocrat:4', 'Aristocrat:DMG I pg 108', 'Commoner', 'Commoner:4', 'Commoner:0', 'Commoner:2', 'Commoner:0', 'Commoner:0', 'Commoner:0', 'Commoner:3', 'Commoner:2', 'Commoner:1', 'Commoner:4', 'Commoner:5', 'Commoner:6', 'Commoner:DMG I pg 109', 'Expert', 'Expert:6', 'Expert:0', 'Expert:6', 'Expert:0', 'Expert:0', 'Expert:2', 'Expert:4', 'Expert:2', 'Expert:1', 'Expert:5', 'Expert:6', 'Expert:3', 'Expert:DMG I pg 109', 'Warrior', 'Warrior:8', 'Warrior:1', 'Warrior:2', 'Warrior:2', 'Warrior:0', 'Warrior:0', 'Warrior:1', 'Warrior:2', 'Warrior:3', 'Warrior:4', 'Warrior:5', 'Warrior:6', 'Warrior:DMG I pg 110']

# Dictionaries containing details about each class, using the class name as the key
chd = {'Ardent':'6', 'Barbarian':'12', 'Bard':'6', 'Beguiler':'6', 'Cleric':'8', 'Crusader':'10', 'Divine Mind':'10', 'Dragon Shaman':'10', 'Druid':'8', 'Dusk Blade':'8', 'Favored Soul':'8', 'Fighter':'10', 'Hexblade':'10', 'Knight':'12', 'Lurk':'6', 'Monk':'8', 'Ninja':'6', 'Paladin':'10', 'Psion':'4', 'Psychic Warrior':'8', 'Ranger':'8', 'Rogue':'6', 'Samurai':'10', 'Scout':'8', 'Shugenja':'6', 'Sorcerer':'4', 'Soul Knife':'10', 'Spell Thief':'6', 'Spirit Shaman':'8', 'Swashbuckler':'10', 'Swordsage':'8', 'Warblade':'12', 'Warlock':'6', 'Warmage':'6', 'Wilder':'6', 'Wizard':'4', 'Wu Jen':'4'}
cbab = {'Ardent':'0', 'Barbarian':'1', 'Bard':'0', 'Beguiler':'0', 'Cleric':'0', 'Crusader':'1', 'Divine Mind':'0', 'Dragon Shaman':'0', 'Druid':'0', 'Dusk Blade':'1', 'Favored Soul':'0', 'Fighter':'1', 'Hexblade':'1', 'Knight':'1', 'Lurk':'0', 'Monk':'0', 'Ninja':'0', 'Paladin':'1', 'Psion':'0', 'Psychic Warrior':'0', 'Ranger':'1', 'Rogue':'0', 'Samurai':'1', 'Scout':'0', 'Shugenja':'0', 'Sorcerer':'0', 'Soul Knife':'0', 'Spell Thief':'0', 'Spirit Shaman':'0', 'Swashbuckler':'1', 'Swordsage':'0', 'Warblade':'1', 'Warlock':'0', 'Warmage':'0', 'Wilder':'0', 'Wizard':'0', 'Wu Jen':'0'}
csp = {'Ardent':'2', 'Barbarian':'4', 'Bard':'6', 'Beguiler':'6', 'Cleric':'2', 'Crusader':'4', 'Divine Mind':'2', 'Dragon Shaman':'2', 'Druid':'4', 'Dusk Blade':'2', 'Favored Soul':'2', 'Fighter':'2', 'Hexblade':'2', 'Knight':'2', 'Lurk':'4', 'Monk':'4', 'Ninja':'6', 'Paladin':'2', 'Psion':'2', 'Psychic Warrior':'2', 'Ranger':'6', 'Rogue':'8', 'Samurai':'2', 'Scout':'8', 'Shugenja':'4', 'Sorcerer':'2', 'Soul Knife':'4', 'Spell Thief':'6', 'Spirit Shaman':'4', 'Swashbuckler':'4', 'Swordsage':'6', 'Warblade':'4', 'Warlock':'2', 'Warmage':'2', 'Wilder':'4', 'Wizard':'2', 'Wu Jen':'2'}
cF = {'Ardent':'0', 'Barbarian':'2', 'Bard':'0', 'Beguiler':'0', 'Cleric':'2', 'Crusader':'2', 'Divine Mind':'2', 'Dragon Shaman':'2', 'Druid':'2', 'Dusk Blade':'2', 'Favored Soul':'2', 'Fighter':'2', 'Hexblade':'0', 'Knight':'0', 'Lurk':'0', 'Monk':'2', 'Ninja':'0', 'Paladin':'2', 'Psion':'0', 'Psychic Warrior':'2', 'Ranger':'2', 'Rogue':'0', 'Samurai':'2', 'Scout':'0', 'Shugenja':'0', 'Sorcerer':'0', 'Soul Knife':'0', 'Spell Thief':'0', 'Spirit Shaman':'2', 'Swashbuckler':'2', 'Swordsage':'0', 'Warblade':'2', 'Warlock':'0', 'Warmage':'0', 'Wilder':'0', 'Wizard':'0', 'Wu Jen':'0'}
cR = {'Ardent':'0', 'Barbarian':'0', 'Bard':'2', 'Beguiler':'0', 'Cleric':'0', 'Crusader':'0', 'Divine Mind':'0', 'Dragon Shaman':'0', 'Druid':'0', 'Dusk Blade':'0', 'Favored Soul':'2', 'Fighter':'0', 'Hexblade':'0', 'Knight':'0', 'Lurk':'2', 'Monk':'2', 'Ninja':'2', 'Paladin':'0', 'Psion':'0', 'Psychic Warrior':'0', 'Ranger':'2', 'Rogue':'2', 'Samurai':'0', 'Scout':'2', 'Shugenja':'0', 'Sorcerer':'0', 'Soul Knife':'2', 'Spell Thief':'0', 'Spirit Shaman':'0', 'Swashbuckler':'0', 'Swordsage':'2', 'Warblade':'0', 'Warlock':'0', 'Warmage':'0', 'Wilder':'0', 'Wizard':'0', 'Wu Jen':'0'}
cW = {'Ardent':'2', 'Barbarian':'0', 'Bard':'2', 'Beguiler':'2', 'Cleric':'2', 'Crusader':'0', 'Divine Mind':'2', 'Dragon Shaman':'2', 'Druid':'2', 'Dusk Blade':'2', 'Favored Soul':'2', 'Fighter':'0', 'Hexblade':'2', 'Knight':'2', 'Lurk':'2', 'Monk':'2', 'Ninja':'0', 'Paladin':'0', 'Psion':'2', 'Psychic Warrior':'0', 'Ranger':'0', 'Rogue':'0', 'Samurai':'0', 'Scout':'0', 'Shugenja':'2', 'Sorcerer':'2', 'Soul Knife':'2', 'Spell Thief':'2', 'Spirit Shaman':'2', 'Swashbuckler':'0', 'Swordsage':'2', 'Warblade':'0', 'Warlock':'2', 'Warmage':'2', 'Wilder':'2', 'Wizard':'2', 'Wu Jen':'2'}
cstr = {'Ardent':'5', 'Barbarian':'1', 'Bard':'6', 'Beguiler':'4', 'Cleric':'5', 'Crusader':'1', 'Divine Mind':'1', 'Dragon Shaman':'1', 'Druid':'5', 'Dusk Blade':'4', 'Favored Soul':'6', 'Fighter':'1', 'Hexblade':'6', 'Knight':'6', 'Lurk':'4', 'Monk':'5', 'Ninja':'2', 'Paladin':'6', 'Psion':'4', 'Psychic Warrior':'1', 'Ranger':'2', 'Rogue':'2', 'Samurai':'1', 'Scout':'2', 'Shugenja':'6', 'Sorcerer':'6', 'Soul Knife':'1', 'Spell Thief':'6', 'Spirit Shaman':'5', 'Swashbuckler':'2', 'Swordsage':'2', 'Warblade':'1', 'Warlock':'6', 'Warmage':'6', 'Wilder':'6', 'Wizard':'4', 'Wu Jen':'4'}
cdex = {'Ardent':'4', 'Barbarian':'2', 'Bard':'2', 'Beguiler':'2', 'Cleric':'3', 'Crusader':'3', 'Divine Mind':'5', 'Dragon Shaman':'3', 'Druid':'2', 'Dusk Blade':'1', 'Favored Soul':'5', 'Fighter':'3', 'Hexblade':'1', 'Knight':'3', 'Lurk':'1', 'Monk':'2', 'Ninja':'5', 'Paladin':'1', 'Psion':'3', 'Psychic Warrior':'5', 'Ranger':'1', 'Rogue':'4', 'Samurai':'2', 'Scout':'5', 'Shugenja':'2', 'Sorcerer':'2', 'Soul Knife':'2', 'Spell Thief':'2', 'Spirit Shaman':'6', 'Swashbuckler':'4', 'Swordsage':'5', 'Warblade':'2', 'Warlock':'2', 'Warmage':'4', 'Wilder':'2', 'Wizard':'2', 'Wu Jen':'2'}
ccon = {'Ardent':'3', 'Barbarian':'5', 'Bard':'4', 'Beguiler':'3', 'Cleric':'6', 'Crusader':'4', 'Divine Mind':'3', 'Dragon Shaman':'6', 'Druid':'3', 'Dusk Blade':'3', 'Favored Soul':'2', 'Fighter':'2', 'Hexblade':'2', 'Knight':'1', 'Lurk':'2', 'Monk':'1', 'Ninja':'3', 'Paladin':'5', 'Psion':'2', 'Psychic Warrior':'2', 'Ranger':'5', 'Rogue':'5', 'Samurai':'3', 'Scout':'4', 'Shugenja':'3', 'Sorcerer':'3', 'Soul Knife':'3', 'Spell Thief':'1', 'Spirit Shaman':'3', 'Swashbuckler':'6', 'Swordsage':'1', 'Warblade':'3', 'Warlock':'3', 'Warmage':'2', 'Wilder':'3', 'Wizard':'3', 'Wu Jen':'3'}
cint = {'Ardent':'2', 'Barbarian':'3', 'Bard':'3', 'Beguiler':'6', 'Cleric':'1', 'Crusader':'2', 'Divine Mind':'2', 'Dragon Shaman':'2', 'Druid':'1', 'Dusk Blade':'2', 'Favored Soul':'1', 'Fighter':'4', 'Hexblade':'3', 'Knight':'5', 'Lurk':'3', 'Monk':'3', 'Ninja':'4', 'Paladin':'3', 'Psion':'5', 'Psychic Warrior':'3', 'Ranger':'6', 'Rogue':'3', 'Samurai':'6', 'Scout':'3', 'Shugenja':'5', 'Sorcerer':'5', 'Soul Knife':'5', 'Spell Thief':'3', 'Spirit Shaman':'2', 'Swashbuckler':'3', 'Swordsage':'4', 'Warblade':'4', 'Warlock':'4', 'Warmage':'3', 'Wilder':'5', 'Wizard':'5', 'Wu Jen':'5'}
cwis = {'Ardent':'1', 'Barbarian':'6', 'Bard':'5', 'Beguiler':'5', 'Cleric':'4', 'Crusader':'5', 'Divine Mind':'4', 'Dragon Shaman':'4', 'Druid':'4', 'Dusk Blade':'5', 'Favored Soul':'3', 'Fighter':'6', 'Hexblade':'5', 'Knight':'4', 'Lurk':'5', 'Monk':'4', 'Ninja':'6', 'Paladin':'2', 'Psion':'1', 'Psychic Warrior':'4', 'Ranger':'4', 'Rogue':'6', 'Samurai':'4', 'Scout':'1', 'Shugenja':'4', 'Sorcerer':'4', 'Soul Knife':'4', 'Spell Thief':'4', 'Spirit Shaman':'4', 'Swashbuckler':'1', 'Swordsage':'3', 'Warblade':'6', 'Warlock':'5', 'Warmage':'1', 'Wilder':'4', 'Wizard':'1', 'Wu Jen':'6'}
ccha = {'Ardent':'6', 'Barbarian':'4', 'Bard':'1', 'Beguiler':'1', 'Cleric':'2', 'Crusader':'6', 'Divine Mind':'6', 'Dragon Shaman':'5', 'Druid':'6', 'Dusk Blade':'6', 'Favored Soul':'4', 'Fighter':'5', 'Hexblade':'4', 'Knight':'2', 'Lurk':'6', 'Monk':'6', 'Ninja':'1', 'Paladin':'4', 'Psion':'6', 'Psychic Warrior':'6', 'Ranger':'3', 'Rogue':'1', 'Samurai':'5', 'Scout':'6', 'Shugenja':'1', 'Sorcerer':'1', 'Soul Knife':'6', 'Spell Thief':'5', 'Spirit Shaman':'1', 'Swashbuckler':'5', 'Swordsage':'6', 'Warblade':'5', 'Warlock':'1', 'Warmage':'5', 'Wilder':'1', 'Wizard':'6', 'Wu Jen':'1'}
csource = {'Ardent':'CPSI pg 6', 'Barbarian':'PHB I pg 25', 'Bard':'PHB I pg 27', 'Beguiler':'PHB II pg 7', 'Cleric':'PHB I pg 31', 'Crusader':'TOB pg 10', 'Divine Mind':'CPSI pg 9', 'Dragon Shaman':'PHB II pg 12', 'Druid':'PHB I pg 35', 'Dusk Blade':'PHB II pg 21', 'Favored Soul':'CDIV pg 7', 'Fighter':'PHB I pg 39', 'Hexblade':'CWAR pg 6', 'Knight':'PHB II pg 26', 'Lurk':'CPSI pg 15', 'Monk':'PHB I pg 40', 'Ninja':'CADV pg 9', 'Paladin':' PHB I pg 43', 'Psion':'EPH pg 20', 'Psychic Warrior':'EPH pg 25', 'Ranger':' PHB I pg 46', 'Rogue':' PHB I pg 49', 'Samurai':'CWAR pg 10', 'Scout':'CADV pg 12', 'Shugenja':'CDIV pg 11', 'Sorcerer':' PHB I pg 52', 'Soul Knife':'EPH pg 27', 'Spell Thief':'CADV pg 18', 'Spirit Shaman':'CDIV pg 15', 'Swashbuckler':'CWAR pg 12', 'Swordsage':'TOB pg 16', 'Warblade':'TOB pg 21', 'Warlock':'CARC pg 7', 'Warmage':'CARC pg 11', 'Wilder':'EPH pg 30', 'Wizard':'PHB I pg 55', 'Wu Jen':'CARC pg 16'}

# Options for Character Race
r_options = ['Changeling', 'Dragonborn', 'Dream Dwarf', 'Dwarf', 'Elan', 'Elf', 'Gnome', 'Goblins', 'Gray Elf', 'Half-Elf', 'Half-Orc', 'Human', 'Illumians', 'Kalashtar', 'Killoren', 'Kobold', 'Maenad', 'Mongrelfolk', 'Orc', 'Raptoran', 'Sea Kin', 'Shifter', 'Spellscale', 'Underfolk', 'Warforged', 'Whisper Gnome', 'Wood Elf', 'Xeph']
ecls = ['Aasimar', 'Aasimar:0', 'Aasimar:0', 'Aasimar:0', 'Aasimar:0', 'Aasimar:0', 'Aasimar:0', 'Aasimar:0', 'Aasimar:+0', 'Aasimar:+0', 'Aasimar:+0', 'Aasimar:+0', 'Aasimar:+2', 'Aasimar:+2', 'Aasimar:+1', 'Aasimar:RODe pg 93', 'Azer', 'Azer:2', 'Azer:8', 'Azer:2', 'Azer:8', 'Azer:3', 'Azer:3', 'Azer:3', 'Azer:+2', 'Azer:+2', 'Azer:+2', 'Azer:+2', 'Azer:+2', 'Azer:-2', 'Azer:+4', 'Azer:MMI pg 22', 'Bugbear', 'Bugbear:3', 'Bugbear:8', 'Bugbear:2', 'Bugbear:2', 'Bugbear:1', 'Bugbear:3', 'Bugbear:1', 'Bugbear:+4', 'Bugbear:+2', 'Bugbear:+2', 'Bugbear:+0', 'Bugbear:+0', 'Bugbear:-2', 'Bugbear:+1', 'Bugbear:MMI pg 29', 'Catfolk', 'Catfolk:0', 'Catfolk:0', 'Catfolk:0', 'Catfolk:0', 'Catfolk:0', 'Catfolk:0', 'Catfolk:0', 'Catfolk:+0', 'Catfolk:+4', 'Catfolk:+0', 'Catfolk:+0', 'Catfolk:+0', 'Catfolk:+2', 'Catfolk:+1', 'Catfolk:ROW pg 92', 'Centaur', 'Centaur:4', 'Centaur:8', 'Centaur:4', 'Centaur:2', 'Centaur:1', 'Centaur:4', 'Centaur:4', 'Centaur:+8', 'Centaur:+4', 'Centaur:+4', 'Centaur:-2', 'Centaur:+2', 'Centaur:+0', 'Centaur:+2', 'Centaur:ROW pg 95', 'Chaos Gnome', 'Chaos Gnome:0', 'Chaos Gnome:0', 'Chaos Gnome:0', 'Chaos Gnome:0', 'Chaos Gnome:0', 'Chaos Gnome:0', 'Chaos Gnome:0', 'Chaos Gnome:-2', 'Chaos Gnome:+2', 'Chaos Gnome:+2', 'Chaos Gnome:+0', 'Chaos Gnome:+0', 'Chaos Gnome:+2', 'Chaos Gnome:+1', 'Chaos Gnome:ROS pg 87', 'Doppleganger', 'Doppleganger:4', 'Doppleganger:8', 'Doppleganger:4', 'Doppleganger:2', 'Doppleganger:1', 'Doppleganger:4', 'Doppleganger:4', 'Doppleganger:+2', 'Doppleganger:+2', 'Doppleganger:+2', 'Doppleganger:+2', 'Doppleganger:+4', 'Doppleganger:+2', 'Doppleganger:+4', 'Doppleganger:RODe pg 95', 'Dromite', 'Dromite:0', 'Dromite:0', 'Dromite:0', 'Dromite:0', 'Dromite:0', 'Dromite:0', 'Dromite:0', 'Dromite:-2', 'Dromite:+0', 'Dromite:+0', 'Dromite:+0', 'Dromite:-2', 'Dromite:+2', 'Dromite:+1', 'Dromite:EPH pg 8', 'Drow', 'Drow:0', 'Drow:0', 'Drow:0', 'Drow:0', 'Drow:0', 'Drow:0', 'Drow:0', 'Drow:+0', 'Drow:+0', 'Drow:+0', 'Drow:+2', 'Drow:+0', 'Drow:-2', 'Drow:+2', 'Drow:MMI pg 103', 'Duergar', 'Duergar:0', 'Duergar:0', 'Duergar:0', 'Duergar:0', 'Duergar:0', 'Duergar:0', 'Duergar:0', 'Duergar:+0', 'Duergar:+0', 'Duergar:+2', 'Duergar:+0', 'Duergar:+0', 'Duergar:-4', 'Duergar:+1', 'Duergar:EPH pg 9', 'Feral Gargun', 'Feral Gargun:2', 'Feral Gargun:8', 'Feral Gargun:2', 'Feral Gargun:2', 'Feral Gargun:0', 'Feral Gargun:3', 'Feral Gargun:3', 'Feral Gargun:+1', 'Feral Gargun:+2', 'Feral Gargun:+4', 'Feral Gargun:-2', 'Feral Gargun:+0', 'Feral Gargun:-2', 'Feral Gargun:+2', 'Feral Gargun:ROS pg 91', 'Gargoyle', 'Gargoyle:4', 'Gargoyle:8', 'Gargoyle:4', 'Gargoyle:2', 'Gargoyle:1', 'Gargoyle:4', 'Gargoyle:4', 'Gargoyle:+4', 'Gargoyle:+4', 'Gargoyle:+8', 'Gargoyle:-4', 'Gargoyle:+0', 'Gargoyle:-4', 'Gargoyle:+5', 'Gargoyle:MMI pg 113', 'Githyanki', 'Githyanki:0', 'Githyanki:0', 'Githyanki:0', 'Githyanki:0', 'Githyanki:0', 'Githyanki:0', 'Githyanki:0', 'Githyanki:+0', 'Githyanki:+2', 'Githyanki:+2', 'Githyanki:+0', 'Githyanki:-2', 'Githyanki:+0', 'Githyanki:+2', 'Githyanki:EPH pg 11', 'Githzerai', 'Githzerai:0', 'Githzerai:0', 'Githzerai:0', 'Githzerai:0', 'Githzerai:0', 'Githzerai:0', 'Githzerai:0', 'Githzerai:+0', 'Githzerai:+6', 'Githzerai:+0', 'Githzerai:-2', 'Githzerai:+2', 'Githzerai:+0', 'Githzerai:+2', 'Githzerai:EPH pg 12', 'Gnoll', 'Gnoll:2', 'Gnoll:8', 'Gnoll:1', 'Gnoll:2', 'Gnoll:3', 'Gnoll:0', 'Gnoll:0', 'Gnoll:+4', 'Gnoll:+0', 'Gnoll:+2', 'Gnoll:-2', 'Gnoll:+0', 'Gnoll:-2', 'Gnoll:+1', 'Gnoll:ROW pg 99', 'Goliath', 'Goliath:0', 'Goliath:0', 'Goliath:0', 'Goliath:0', 'Goliath:0', 'Goliath:0', 'Goliath:0', 'Goliath:+4', 'Goliath:-2', 'Goliath:+2', 'Goliath:+0', 'Goliath:+0', 'Goliath:+0', 'Goliath:+1', 'Goliath:ROS pg 56', 'Half-Giant', 'Half-Giant:0', 'Half-Giant:0', 'Half-Giant:0', 'Half-Giant:0', 'Half-Giant:0', 'Half-Giant:0', 'Half-Giant:0', 'Half-Giant:+2', 'Half-Giant:-2', 'Half-Giant:+2', 'Half-Giant:+0', 'Half-Giant:+0', 'Half-Giant:+0', 'Half-Giant:+1', 'Half-Giant:EPH pg 13', 'Half-Ogre', 'Half-Ogre:0', 'Half-Ogre:0', 'Half-Ogre:0', 'Half-Ogre:0', 'Half-Ogre:0', 'Half-Ogre:0', 'Half-Ogre:0', 'Half-Ogre:+6', 'Half-Ogre:-2', 'Half-Ogre:+2', 'Half-Ogre:-2', 'Half-Ogre:+0', 'Half-Ogre:-2', 'Half-Ogre:+2', 'Half-Ogre:RODe pg 98', 'Hill Giant', 'Hill Giant:12', 'Hill Giant:8', 'Hill Giant:8', 'Hill Giant:2', 'Hill Giant:8', 'Hill Giant:4', 'Hill Giant:4', 'Hill Giant:+14', 'Hill Giant:-2', 'Hill Giant:+8', 'Hill Giant:-4', 'Hill Giant:+0', 'Hill Giant:-4', 'Hill Giant:+4', 'Hill Giant:MMI pg 124', 'Hob Goblin', 'Hob Goblin:0', 'Hob Goblin:0', 'Hob Goblin:0', 'Hob Goblin:0', 'Hob Goblin:0', 'Hob Goblin:0', 'Hob Goblin:0', 'Hob Goblin:+0', 'Hob Goblin:+2', 'Hob Goblin:+2', 'Hob Goblin:+0', 'Hob Goblin:+0', 'Hob Goblin:+0', 'Hob Goblin:+1', 'Hob Goblin:MMI pg 154', 'Lizard Folk', 'Lizard Folk:2', 'Lizard Folk:8', 'Lizard Folk:1', 'Lizard Folk:2', 'Lizard Folk:0', 'Lizard Folk:3', 'Lizard Folk:0', 'Lizard Folk:+2', 'Lizard Folk:+0', 'Lizard Folk:+2', 'Lizard Folk:-2', 'Lizard Folk:+0', 'Lizard Folk:+0', 'Lizard Folk:+1', 'Lizard Folk:MMI pg 169', 'Mindflayer', 'Mindflayer:8', 'Mindflayer:8', 'Mindflayer:6', 'Mindflayer:2', 'Mindflayer:2', 'Mindflayer:2', 'Mindflayer:6', 'Mindflayer:+2', 'Mindflayer:+4', 'Mindflayer:+2', 'Mindflayer:+8', 'Mindflayer:+6', 'Mindflayer:+6', 'Mindflayer:+7', 'Mindflayer:MMI pg 188', 'Minotaur', 'Minotaur:6', 'Minotaur:8', 'Minotaur:6', 'Minotaur:2', 'Minotaur:2', 'Minotaur:5', 'Minotaur:5', 'Minotaur:+8', 'Minotaur:+4', 'Minotaur:+0', 'Minotaur:-4', 'Minotaur:+0', 'Minotaur:-2', 'Minotaur:+2', 'Minotaur:MMI pg 189', 'Ogre', 'Ogre:4', 'Ogre:8', 'Ogre:3', 'Ogre:2', 'Ogre:4', 'Ogre:1', 'Ogre:1', 'Ogre:+10', 'Ogre:-2', 'Ogre:+4', 'Ogre:-4', 'Ogre:+0', 'Ogre:-4', 'Ogre:+2', 'Ogre:MMI pg 199', 'Rakshasa', 'Rakshasa:7', 'Rakshasa:8', 'Rakshasa:7', 'Rakshasa:8', 'Rakshasa:5', 'Rakshasa:5', 'Rakshasa:5', 'Rakshasa:+2', 'Rakshasa:+4', 'Rakshasa:+6', 'Rakshasa:+2', 'Rakshasa:+2', 'Rakshasa:+6', 'Rakshasa:+7', 'Rakshasa:MMI pg 212', 'Satyr', 'Satyr:5', 'Satyr:8', 'Satyr:2', 'Satyr:6', 'Satyr:1', 'Satyr:4', 'Satyr:4', 'Satyr:+0', 'Satyr:+2', 'Satyr:+2', 'Satyr:+2', 'Satyr:+2', 'Satyr:+2', 'Satyr:+2', 'Satyr:MMI pg 220', 'Sharakim', 'Sharakim:0', 'Sharakim:0', 'Sharakim:0', 'Sharakim:0', 'Sharakim:0', 'Sharakim:0', 'Sharakim:0', 'Sharakim:+2', 'Sharakim:-2', 'Sharakim:+0', 'Sharakim:+2', 'Sharakim:+0', 'Sharakim:-2', 'Sharakim:+1', 'Sharakim:RODe pg 104', 'Skulk', 'Skulk:2', 'Skulk:8', 'Skulk:1', 'Skulk:2', 'Skulk:0', 'Skulk:3', 'Skulk:0', 'Skulk:+0', 'Skulk:+4', 'Skulk:+0', 'Skulk:+0', 'Skulk:-2', 'Skulk:-4', 'Skulk:+1', 'Skulk:RODE pg 106', 'Stone Giant', 'Stone Giant:14', 'Stone Giant:8', 'Stone Giant:10', 'Stone Giant:2', 'Stone Giant:9', 'Stone Giant:4', 'Stone Giant:4', 'Stone Giant:+16', 'Stone Giant:+4', 'Stone Giant:+8', 'Stone Giant:+0', 'Stone Giant:+2', 'Stone Giant:+0', 'Stone Giant:+4', 'Stone Giant:MMI pg 125', 'Stonechild', 'Stonechild:2', 'Stonechild:8', 'Stonechild:2', 'Stonechild:8', 'Stonechild:3', 'Stonechild:3', 'Stonechild:3', 'Stonechild:+8', 'Stonechild:+0', 'Stonechild:+8', 'Stonechild:+2', 'Stonechild:+0', 'Stonechild:-2', 'Stonechild:+4', 'Stonechild:ROS pg 94', 'Thri-Keen', 'Thri-Keen:0', 'Thri-Keen:0', 'Thri-Keen:0', 'Thri-Keen:0', 'Thri-Keen:0', 'Thri-Keen:0', 'Thri-Keen:0', 'Thri-Keen:+2', 'Thri-Keen:+4', 'Thri-Keen:+0', 'Thri-Keen:-2', 'Thri-Keen:+2', 'Thri-Keen:-4', 'Thri-Keen:+2', 'Thri-Keen:EPH pg 15', 'Tiefling', 'Tiefling:0', 'Tiefling:0', 'Tiefling:0', 'Tiefling:0', 'Tiefling:0', 'Tiefling:0', 'Tiefling:0', 'Tiefling:+0', 'Tiefling:+2', 'Tiefling:+0', 'Tiefling:+2', 'Tiefling:+0', 'Tiefling:-2', 'Tiefling:+1', 'Tiefling:RODe pg 108', 'Troglodyte', 'Troglodyte:2', 'Troglodyte:8', 'Troglodyte:1', 'Troglodyte:2', 'Troglodyte:3', 'Troglodyte:0', 'Troglodyte:0', 'Troglodyte:+0', 'Troglodyte:-2', 'Troglodyte:+4', 'Troglodyte:-2', 'Troglodyte:+0', 'Troglodyte:+0', 'Troglodyte:+2', 'Troglodyte:MMI pg 247', 'Troll', 'Troll:6', 'Troll:8', 'Troll:6', 'Troll:2', 'Troll:5', 'Troll:2', 'Troll:2', 'Troll:+12', 'Troll:+4', 'Troll:+12', 'Troll:-4', 'Troll:-2', 'Troll:-4', 'Troll:+5', 'Troll:MMI pg 248', 'Yuan-Ti', 'Yuan-Ti:4', 'Yuan-Ti:8', 'Yuan-Ti:4', 'Yuan-Ti:2', 'Yuan-Ti:1', 'Yuan-Ti:4', 'Yuan-Ti:4', 'Yuan-Ti:+0', 'Yuan-Ti:+2', 'Yuan-Ti:+0', 'Yuan-Ti:+2', 'Yuan-Ti:+0', 'Yuan-Ti:+2', 'Yuan-Ti:+2', 'Yuan-Ti:MMI pg 263']

# Dictionaries containing details about each race using the Race as the key
rqhd = {'Changeling':'0', 'Dragonborn':'0', 'Dream Dwarf':'0', 'Dwarf':'0', 'Elan':'0', 'Elf':'0', 'Gnome':'0', 'Goblins':'0', 'Gray Elf':'0', 'Half-Elf':'0', 'Half-Orc':'0', 'Human':'0', 'Illumians':'0', 'Kalashtar':'0', 'Killoren':'0', 'Kobold':'0', 'Maenad':'0', 'Mongrelfolk':'0', 'Orc':'0', 'Raptoran':'0', 'Sea Kin':'0', 'Shifter':'0', 'Spellscale':'0', 'Underfolk':'0', 'Warforged':'0', 'Whisper Gnome':'0', 'Wood Elf':'0', 'Xeph':'0'}
rhd = {'Changeling':'0', 'Dragonborn':'0', 'Dream Dwarf':'0', 'Dwarf':'0', 'Elan':'0', 'Elf':'0', 'Gnome':'0', 'Goblins':'0', 'Gray Elf':'0', 'Half-Elf':'0', 'Half-Orc':'0', 'Human':'0', 'Illumians':'0', 'Kalashtar':'0', 'Killoren':'0', 'Kobold':'0', 'Maenad':'0', 'Mongrelfolk':'0', 'Orc':'0', 'Raptoran':'0', 'Sea Kin':'0', 'Shifter':'0', 'Spellscale':'0', 'Underfolk':'0', 'Warforged':'0', 'Whisper Gnome':'0', 'Wood Elf':'0', 'Xeph':'0'}
rbab = {'Changeling':'0', 'Dragonborn':'0', 'Dream Dwarf':'0', 'Dwarf':'0', 'Elan':'0', 'Elf':'0', 'Gnome':'0', 'Goblins':'0', 'Gray Elf':'0', 'Half-Elf':'0', 'Half-Orc':'0', 'Human':'0', 'Illumians':'0', 'Kalashtar':'0', 'Killoren':'0', 'Kobold':'0', 'Maenad':'0', 'Mongrelfolk':'0', 'Orc':'0', 'Raptoran':'0', 'Sea Kin':'0', 'Shifter':'0', 'Spellscale':'0', 'Underfolk':'0', 'Warforged':'0', 'Whisper Gnome':'0', 'Wood Elf':'0', 'Xeph':'0'}
rsp = {'Changeling':'0', 'Dragonborn':'0', 'Dream Dwarf':'0', 'Dwarf':'0', 'Elan':'0', 'Elf':'0', 'Gnome':'0', 'Goblins':'0', 'Gray Elf':'0', 'Half-Elf':'0', 'Half-Orc':'0', 'Human':'0', 'Illumians':'0', 'Kalashtar':'0', 'Killoren':'0', 'Kobold':'0', 'Maenad':'0', 'Mongrelfolk':'0', 'Orc':'0', 'Raptoran':'0', 'Sea Kin':'0', 'Shifter':'0', 'Spellscale':'0', 'Underfolk':'0', 'Warforged':'0', 'Whisper Gnome':'0', 'Wood Elf':'0', 'Xeph':'0'}
rF = {'Changeling':'0', 'Dragonborn':'0', 'Dream Dwarf':'0', 'Dwarf':'0', 'Elan':'0', 'Elf':'0', 'Gnome':'0', 'Goblins':'0', 'Gray Elf':'0', 'Half-Elf':'0', 'Half-Orc':'0', 'Human':'0', 'Illumians':'0', 'Kalashtar':'0', 'Killoren':'0', 'Kobold':'0', 'Maenad':'0', 'Mongrelfolk':'0', 'Orc':'0', 'Raptoran':'0', 'Sea Kin':'0', 'Shifter':'0', 'Spellscale':'0', 'Underfolk':'0', 'Warforged':'0', 'Whisper Gnome':'0', 'Wood Elf':'0', 'Xeph':'0'}
rR = {'Changeling':'0', 'Dragonborn':'0', 'Dream Dwarf':'0', 'Dwarf':'0', 'Elan':'0', 'Elf':'0', 'Gnome':'0', 'Goblins':'0', 'Gray Elf':'0', 'Half-Elf':'0', 'Half-Orc':'0', 'Human':'0', 'Illumians':'0', 'Kalashtar':'0', 'Killoren':'0', 'Kobold':'0', 'Maenad':'0', 'Mongrelfolk':'0', 'Orc':'0', 'Raptoran':'0', 'Sea Kin':'0', 'Shifter':'0', 'Spellscale':'0', 'Underfolk':'0', 'Warforged':'0', 'Whisper Gnome':'0', 'Wood Elf':'0', 'Xeph':'0'}
rW = {'Changeling':'0', 'Dragonborn':'0', 'Dream Dwarf':'0', 'Dwarf':'0', 'Elan':'0', 'Elf':'0', 'Gnome':'0', 'Goblins':'0', 'Gray Elf':'0', 'Half-Elf':'0', 'Half-Orc':'0', 'Human':'0', 'Illumians':'0', 'Kalashtar':'0', 'Killoren':'0', 'Kobold':'0', 'Maenad':'0', 'Mongrelfolk':'0', 'Orc':'0', 'Raptoran':'0', 'Sea Kin':'0', 'Shifter':'0', 'Spellscale':'0', 'Underfolk':'0', 'Warforged':'0', 'Whisper Gnome':'0', 'Wood Elf':'0', 'Xeph':'0'}
rstr = {'Changeling':'+0', 'Dragonborn':'+0', 'Dream Dwarf':'+0', 'Dwarf':'+0', 'Elan':'+0', 'Elf':'+0', 'Gnome':'-2', 'Goblins':'-2', 'Gray Elf':'-2', 'Half-Elf':'+0', 'Half-Orc':'+2', 'Human':'+0', 'Illumians':'+0', 'Kalashtar':'+0', 'Killoren':'+0', 'Kobold':'-4', 'Maenad':'+0', 'Mongrelfolk':'+0', 'Orc':'+4', 'Raptoran':'+0', 'Sea Kin':'+0', 'Shifter':'+0', 'Spellscale':'+0', 'Underfolk':'+0', 'Warforged':'+0', 'Whisper Gnome':'-2', 'Wood Elf':'+2', 'Xeph':'-2'}
rdex = {'Changeling':'+0', 'Dragonborn':'-2', 'Dream Dwarf':'-2', 'Dwarf':'+0', 'Elan':'+0', 'Elf':'+2', 'Gnome':'+0', 'Goblins':'+2', 'Gray Elf':'+2', 'Half-Elf':'+0', 'Half-Orc':'+0', 'Human':'+0', 'Illumians':'+0', 'Kalashtar':'+0', 'Killoren':'+0', 'Kobold':'+2', 'Maenad':'+0', 'Mongrelfolk':'+0', 'Orc':'+0', 'Raptoran':'+0', 'Sea Kin':'+0', 'Shifter':'+2', 'Spellscale':'+0', 'Underfolk':'+0', 'Warforged':'+0', 'Whisper Gnome':'+2', 'Wood Elf':'+2', 'Xeph':'+2'}
rcon = {'Changeling':'+0', 'Dragonborn':'+2', 'Dream Dwarf':'+2', 'Dwarf':'+2', 'Elan':'+0', 'Elf':'-2', 'Gnome':'+2', 'Goblins':'+0', 'Gray Elf':'-2', 'Half-Elf':'+0', 'Half-Orc':'+0', 'Human':'+0', 'Illumians':'+0', 'Kalashtar':'+0', 'Killoren':'+0', 'Kobold':'+2', 'Maenad':'+0', 'Mongrelfolk':'+4', 'Orc':'+0', 'Raptoran':'+0', 'Sea Kin':'+0', 'Shifter':'+0', 'Spellscale':'-2', 'Underfolk':'+0', 'Warforged':'+2', 'Whisper Gnome':'+2', 'Wood Elf':'-2', 'Xeph':'+0'}
rint = {'Changeling':'+0', 'Dragonborn':'+0', 'Dream Dwarf':'+0', 'Dwarf':'+0', 'Elan':'+0', 'Elf':'+0', 'Gnome':'+0', 'Goblins':'+0', 'Gray Elf':'+2', 'Half-Elf':'+0', 'Half-Orc':'-2', 'Human':'+0', 'Illumians':'+0', 'Kalashtar':'+0', 'Killoren':'+0', 'Kobold':'-2', 'Maenad':'+0', 'Mongrelfolk':'-2', 'Orc':'-2', 'Raptoran':'+0', 'Sea Kin':'+0', 'Shifter':'-2', 'Spellscale':'+0', 'Underfolk':'+0', 'Warforged':'+0', 'Whisper Gnome':'+0', 'Wood Elf':'-2', 'Xeph':'+0'}
rwis = {'Changeling':'+0', 'Dragonborn':'+0', 'Dream Dwarf':'+0', 'Dwarf':'+0', 'Elan':'+0', 'Elf':'+0', 'Gnome':'+0', 'Goblins':'+0', 'Gray Elf':'+0', 'Half-Elf':'+0', 'Half-Orc':'+0', 'Human':'+0', 'Illumians':'+0', 'Kalashtar':'+0', 'Killoren':'+0', 'Kobold':'+0', 'Maenad':'+0', 'Mongrelfolk':'+0', 'Orc':'-2', 'Raptoran':'+0', 'Sea Kin':'+0', 'Shifter':'+0', 'Spellscale':'+0', 'Underfolk':'+0', 'Warforged':'-2', 'Whisper Gnome':'+0', 'Wood Elf':'+0', 'Xeph':'+0'}
rcha = {'Changeling':'+0', 'Dragonborn':'+0', 'Dream Dwarf':'+0', 'Dwarf':'-2', 'Elan':'+0', 'Elf':'+0', 'Gnome':'+0', 'Goblins':'-2', 'Gray Elf':'+0', 'Half-Elf':'+0', 'Half-Orc':'-2', 'Human':'+0', 'Illumians':'+0', 'Kalashtar':'+0', 'Killoren':'+0', 'Kobold':'+0', 'Maenad':'+0', 'Mongrelfolk':'-4', 'Orc':'-2', 'Raptoran':'+0', 'Sea Kin':'+0', 'Shifter':'-2', 'Spellscale':'+2', 'Underfolk':'+0', 'Warforged':'-2', 'Whisper Gnome':'-2', 'Wood Elf':'+0', 'Xeph':'+0'}
recl = {'Changeling':'+0', 'Dragonborn':'+0', 'Dream Dwarf':'+0', 'Dwarf':'+0', 'Elan':'-2', 'Elf':'+0', 'Gnome':'+0', 'Goblins':'+0', 'Gray Elf':'+0', 'Half-Elf':'+0', 'Half-Orc':'+0', 'Human':'+0', 'Illumians':'+0', 'Kalashtar':'+0', 'Killoren':'+0', 'Kobold':'+0', 'Maenad':'+0', 'Mongrelfolk':'+0', 'Orc':'+0', 'Raptoran':'+0', 'Sea Kin':'+0', 'Shifter':'+0', 'Spellscale':'+0', 'Underfolk':'+0', 'Warforged':'+0', 'Whisper Gnome':'+0', 'Wood Elf':'+0', 'Xeph':'+0'}
rsource = {'Changeling':'ROE pg 42', 'Dragonborn':'RODr pg 8', 'Dream Dwarf':'ROS pg 89', 'Dwarf':'PHB I pg 14', 'Elan':'+0', 'Elf':'PHB I pg 16', 'Gnome':'PHB I pg 17', 'Goblins':'MMI pg 134', 'Gray Elf':'MMI pg 104', 'Half-Elf':'PHB I pg 18', 'Half-Orc':'PHB I pg 19', 'Human':'PHB I pg 13', 'Illumians':'RODe pg 53', 'Kalashtar':'ROE pg 56', 'Killoren':'ROW pg 103', 'Kobold':'+0', 'Maenad':'EPH pg 14', 'Mongrelfolk':'RODE pg 99', 'Orc':'MMI pg 204', 'Raptoran':'ROW pg 68', 'Sea Kin':'RODe pg 102', 'Shifter':'ROE pg 25', 'Spellscale':'RODr pg 23', 'Underfolk':'RODe pg 110', 'Warforged':'ROE pg 8', 'Whisper Gnome':'ROS pg 96', 'Wood Elf':'MMI pg 104', 'Xeph':'EPH pg 16'}

# Check with user about using NPC classes for generation
ans = raw_input("Would you like to include NPC Classes?  ")
z = 0
if ans == 'Y' or ans == 'y':
    for term in npcs:
        if z == 0:
            term = term
            c_options.append(term)
        elif z == 1:
            term = term.split(":")
            a, b = term[0], term[1]
            chd[a] = b
        elif z == 2:
            term = term.split(":")
            a, b = term[0], term[1]
            cbab[a] = b
        elif z == 3:
            term = term.split(":")
            a, b = term[0], term[1]
            csp[a] = b
        elif z == 4:
            term = term.split(":")
            a, b = term[0], term[1]
            cF[a] = b
        elif z == 5:
            term = term.split(":")
            a, b = term[0], term[1]
            cR[a] = b
        elif z == 6:
            term = term.split(":")
            a, b = term[0], term[1]
            cW[a] = b
        elif z == 7:
            term = term.split(":")
            a, b = term[0], term[1]
            cstr[a] = b
        elif z == 8:
            term = term.split(":")
            a, b = term[0], term[1]
            cdex[a] = b
        elif z == 9:
            term = term.split(":")
            a, b = term[0], term[1]
            ccon[a] = b
        elif z == 10:
            term = term.split(":")
            a, b = term[0], term[1]
            cint[a] = b
        elif z == 11:
            term = term.split(":")
            a, b = term[0], term[1]
            cwis[a] = b
        elif z == 12:
            term = term.split(":")
            a, b = term[0], term[1]
            ccha[a] = b
        else:
            term = term.split(":")
            a, b = term[0], term[1]
            csource[a] = b
            z = -1
        z = z + 1
else:
    ''

# Check with user about generating Home Brew Classes
ans = raw_input("Would you like to include Home Brew Classes?  ")
z = 0
if ans == 'Y' or ans == 'Y':
    cur = 1
    while cur != '':
        cur = classh.readline()
        line = cur.strip()
        line = line.split('.')
        for term in line:
            if z == 0:
                c_options.append(term)
            elif z == 1:
                term = term.split(":")
                a, b = term[0], term[1]
                chd[a] = b
            elif z == 2:
                term = term.split(":")
                a, b = term[0], term[1]
                cbab[a] = b
            elif z == 3:
                term = term.split(":")
                a, b = term[0], term[1]
                csp[a] = b
            elif z == 4:
                term = term.split(":")
                a, b = term[0], term[1]
                cF[a] = b
            elif z == 5:
                term = term.split(":")
                a, b = term[0], term[1]
                cR[a] = b
            elif z == 6:
                term = term.split(":")
                a, b = term[0], term[1]
                cW[a] = b
            elif z == 7:
                term = term.split(":")
                a, b = term[0], term[1]
                cstr[a] = b
            elif z == 8:
                term = term.split(":")
                a, b = term[0], term[1]
                cdex[a] = b
            elif z == 9:
                term = term.split(":")
                a, b = term[0], term[1]
                ccon[a] = b
            elif z == 10:
                term = term.split(":")
                a, b = term[0], term[1]
                cint[a] = b
            elif z == 11:
                term = term.split(":")
                a, b = term[0], term[1]
                cwis[a] = b
            elif z == 12:
                term = term.split(":")
                a, b = term[0], term[1]
                ccha[a] = b
            else:
                term = term.split(":")
                a, b = term[0], term[1]
                csource[a] = b
                z = -1
            z = z + 1
else:
    ''

# Check with user about generating races with an ECL
ans = raw_input("Would you like to include races with an ECL?  ")
z = 0
if ans == 'y' or ans == 'Y':
    for term in ecls:
        if z == 0:
            r_options.append(term)
        elif z == 1:
            term = term.split(":")
            a, b = term[0], term[1]
            rqhd[a] = b
        elif z == 2:
            term = term.split(":")
            a, b = term[0], term[1]
            rhd[a] = b
        elif z == 3:
            term = term.split(":")
            a, b = term[0], term[1]
            rbab[a] = b
        elif z == 4:
            term = term.split(":")
            a, b = term[0], term[1]
            rsp[a] = b
        elif z == 5:
            term = term.split(":")
            a, b = term[0], term[1]
            rF[a] = b
        elif z == 6:
            term = term.split(":")
            a, b = term[0], term[1]
            rR[a] = b
        elif z == 7:
            term = term.split(":")
            a, b = term[0], term[1]
            rW[a] = b
        elif z == 8:
            term = term.split(":")
            a, b = term[0], term[1]
            rstr[a] = b
        elif z == 9:
            term = term.split(":")
            a, b = term[0], term[1]
            rdex[a] = b
        elif z == 10:
            term = term.split(":")
            a, b = term[0], term[1]
            rcon[a] = b
        elif z == 11:
            term = term.split(":")
            a, b = term[0], term[1]
            rint[a] = b
        elif z == 12:
            term = term.split(":")
            a, b = term[0], term[1]
            rwis[a] = b
        elif z == 13:
            term = term.split(":")
            a, b = term[0], term[1]
            rcha[a] = b
        elif z == 14:
            term = term.split(":")
            a, b = term[0], term[1]
            recl[a] = b
        else:
            term = term.split(":")
            a, b = term[0], term[1]
            rsource[a] = b
            z = -1
        z = z + 1
else:
    ''


# Check with user about generating home brew races
ans = raw_input("Would you like to include Home Brew Races?  ")
z = 0
if ans == 'y' or ans == 'Y':
    cur = 0
    while cur != '':
        cur = raceh.readline()
        line = cur.strip()
        line = line.split('.')
        for term in line:
            if z == 0:
                r_options.append(term)
            elif z == 1:
                term = term.split(":")
                a, b = term[0], term[1]
                rqhd[a] = b
            elif z == 2: # Clause is not adding new keys to given dictionary
                term = term.split(":")
                a, b = term[0], term[1]
                rhd[a] = b
            elif z == 3: # Clause is not adding new keys to given dictionary
                term = term.split(":")
                a, b = term[0], term[1]
                rbab[a] = b
            elif z == 4:
                term = term.split(":")
                a, b = term[0], term[1]
                rsp[a] = b
            elif z == 5:
                term = term.split(":")
                a, b = term[0], term[1]
                rF[a] = b
            elif z == 6:
                term = term.split(":")
                a, b = term[0], term[1]
                rR[a] = b
            elif z == 7:
                term = term.split(":")
                a, b = term[0], term[1]
                rW[a] = b
            elif z == 8:
                term = term.split(":")
                a, b = term[0], term[1]
                rstr[a] = b
            elif z == 9:
                term = term.split(":")
                a, b = term[0], term[1]
                rdex[a] = b
            elif z == 10:
                term = term.split(":")
                a, b = term[0], term[1]
                rcon[a] = b
            elif z == 11:
                term = term.split(":")
                a, b = term[0], term[1]
                rint[a] = b
            elif z == 12:
                term = term.split(":")
                a, b = term[0], term[1]
                rwis[a] = b
            elif z == 13:
                term = term.split(":")
                a, b = term[0], term[1]
                rcha[a] = b
            elif z == 14:
                term = term.split(":")
                a, b = term[0], term[1]
                recl[a] = b
            else:
                term = term.split(":")
                a, b = term[0], term[1]
                rsource[a] = b
                z = -1
            z = z + 1

classh.close()
raceh.close()

# randomly generate ability scores
abilities = []
As = []
do_i_stop = "n"
while do_i_stop == "n":
    while len(As) != 6:
        v = randint(3, 18)
        As.append(v)
    cumulation, nogo, rep = 0, 0, 0
    for term in As:
        cumulation = cumulation + ((int(term) - 10) / 2)
        rep = rep + 1
        if term < 14:
            nogo = nogo + 1
        else:
            "" 
    if cumulation <= 0 and rep == 6:
        nogo = 6
    else:
        ""
    if nogo == 6:
        As = [] # if a character has no scores above 14 or the sum of the modifiers of a characters ability scores is zero or less, he / she is entitled to re-roll his or her ability scores
    else:
        do_i_stop = ""

# sort ability scores from highest to lowest, this is required as the order of the Abilities will be that in which the character would need their scores to range from high to low
ab = []
while len(ab) != 6:
    As1, c = As, 0
    for term in As1:
        n = 0
        for item in As1:
            if int(term) < int(item):
                n = n + 1
            else:
                ""
        if n > 0:
            c = c + 1
        else:
            ab.append(term)
            As.pop(c)
    
# randomly determine gender, name, race, and class.
g = randint(1,2)
if g == 1:
    g = 'Female'
    Name = gnames[randint(0, 49)] + " " + gnames[randint(0, 49)] + " " + lnames[randint(0,49)]
else:
    g = 'Male'
    Name = bnames[randint(0, 49)] + " " + bnames[randint(0, 49)] + " " + lnames[randint(0,49)]
c, r = len(c_options) - 1, len(r_options) - 1
c, r = randint(0, c), randint(0, r)
c, r = c_options[c], r_options[r]

# Generate official ability scores for first class level
STR, DEX, CON, INT, WIS, CHA = int(cstr[c]), int(cdex[c]), int(ccon[c]), int(cint[c]), int(cwis[c]), int(ccha[c])
STR, DEX, CON, INT, WIS, CHA = int(ab[STR - 1]), int(ab[DEX - 1]), int(ab[CON - 1]), int(ab[INT - 1]), int(ab[WIS - 1]), int(ab[CHA - 1])
if rstr[r][0] == "+":
    STR = STR + int(rstr[r][1:])
else:
    STR = STR - int(rstr[r][1:])
if rdex[r][0] == "+":
    DEX = DEX + int(rdex[r][1:])
else:
    DEX = DEX - int(rdex[r][1:])
if rcon[r][0] == "+":
    CON = CON + int(rcon[r][1:])
else:
    CON = CON - int(rcon[r][1:])
if rint[r][0] == "+":
    INT = INT + int(rint[r][1:])
else:
    INT = INT - int(rint[r][1:])
if rwis[r][0] == "+":
    WIS = WIS + int(rwis[r][1:])
else:
    WIS = WIS - int(rwis[r][1:])
if rcha[r][0] == "+":
    CHA = CHA + int(rcha[r][1:])
else:
    CHA = CHA - int(rcha[r][1:])
# According to rules in PHB I and DMG I a character can not have an INT < 3 and any other score < 1 means a character can take no action, rememdy follows using house rule of author
if STR < 1:
    STR = 1
else:
    ''
if DEX < 1:
    DEX = 1
else:
    ''
if CON < 1:
    CON = 1
else:
    ''
if INT < 3:
    INT = 3
else:
    ''
if WIS < 1:
    WIS = 1
else:
    ''
if CHA < 1:
    CHA = 1
else:
    ''

# Collect information
HP = int(chd[c]) + (int(rqhd[r]) * int(rhd[r])) + (((CON - 10) / 2) * (1 + int(rqhd[r])))
SP = ((int(csp[c]) + ((INT - 10) / 2)) * 4) + (int(rsp[r]) + ((INT - 10) / 2))
if SP < 1:
    SP = 4
else:
    ''
BAB = int(cbab[c]) + int(rbab[r])
FORT = ((CON - 10) / 2) + int(cF[c]) + int(rF[r])
REF = ((DEX - 10) / 2) + int(cR[c]) + int(rR[r])
WILL = ((WIS - 10) / 2) + int(cW[c]) + int(rW[r])
CLASS, Race = c, r
ECL = recl[r]
ClassSource, RaceSource = csource[c], rsource[r]


print "\n" * 15

# Display generated character to user
print Name + "     " + g + " " + r
print c + " " * 5 + str(HP) + "HP" + " " * 5 + str(SP) + "skill points" + " " * 5 + "ECL " + ECL
print "BAB +" + str(BAB) + " " * 5 + "FORT +" + str(FORT) + " " * 5 + "REF +" + str(REF) + " " * 5 + "WILL +" + str(WILL)
print "STR " + str(STR) + "|" + str((STR - 10) / 2) + "  DEX " + str(DEX) + "|" + str((DEX - 10) / 2) + "  CON " + str(CON) + "|" + str((CON - 10) / 2 ) + "  INT " + str(INT) + "|" + str((INT - 10) / 2) + "  WIS " + str(WIS) + "|" + str((WIS - 10 ) / 2) + "  CHA " + str(CHA) + "|" + str((CHA - 10) / 2)
print "Character data from", csource[c]
print "Race data from", rsource[r]

# Prepare character to output to a file
line1 = Name + "     " + g + " " + r + "\n"
line2 = c + " " * 5 + str(HP) + "HP" + " " * 5 + str(SP) + "skill points" + " " * 5 + "ECL " + ECL + "\n"
line3 = "BAB +" + str(BAB) + " " * 5 + "FORT +" + str(FORT) + " " * 5 + "REF +" + str(REF) + " " * 5 + "WILL +" + str(WILL) + "\n"
line4 = "STR " + str(STR) + "|" + str((STR - 10) / 2) + "  DEX " + str(DEX) + "|" + str((DEX - 10) / 2) + "  CON " + str(CON) + "|" + str((CON - 10) / 2 ) + "  INT " + str(INT) + "|" + str((INT - 10) / 2) + "  WIS " + str(WIS) + "|" + str((WIS - 10 ) / 2) + "  CHA " + str(CHA) + "|" + str((CHA - 10) / 2) + "\n"
line5 = "Character data from " + csource[c] + "\n"
line6 = "Race data from " + rsource[r] + "\n"

datum = [line1, line2, line3, line4, line5, line6]

# Ask the user if they would like to save their generated character
print "\n" * 3
ans = raw_input("Would you like to save this character?  ")
if ans == 'y' or ans == 'Y':
    ans = raw_input("Please supply the name of the file which you want to save this character to.  ")
    ans = ans + ".txt"
    outfile = open(ans, 'a')
    for term in datum:
        outfile.write(term)
    outfile.close()
else:
    ''


raw_input(' ')
