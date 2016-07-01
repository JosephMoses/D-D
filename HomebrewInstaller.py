def mk(x, y, z):
    n = y + ':' + z
    m = x + n
    return m

def Class():
    a = raw_input('Class Name: ')
    m = a + '.'
    b = raw_input('How large is the hit die for this class? ') + '.'
    m = mk(m, a, b)
    b = raw_input('What is the BAB of this class at level one? ') + '.'
    m = mk(m, a, b)
    b = raw_input('How many skill points does this class get per level? ') + '.'
    m = mk(m, a, b)
    b = raw_input('What is the base fortitude save of this class at level one? ') + '.'
    m = mk(m, a, b)
    b = raw_input('What is the base reflex save of this class at level one? ') + '.'
    m = mk(m, a, b)
    b = raw_input('What is the base will save of this class at level one? ') + '.'
    m = mk(m, a, b)
    b = raw_input('On a scale of one to six, (1 being highest) rate the value of Strength to this class. ') + '.'
    m = mk(m, a, b)
    b = raw_input('On a scale of one to six, (1 being highest) rate the value of Dexterity to this class.') + '.'
    m = mk(m, a, b)
    b = raw_input('On a scale of one to six, (1 being highest) rate the value of Constitution to this class.') + '.'
    m = mk(m, a, b)
    b = raw_input('On a scale of one to six, (1 being highest) rate the value of Intelligence to this class.') + '.'
    m = mk(m, a, b)
    b = raw_input('On a scale of one to six, (1 being highest) rate the value of Wisdom to this class.') + '.'
    m = mk(m, a, b)
    b = raw_input('On a scale of one to six, (1 being highest) rate the value of Charisma to this class.') + '.'
    m = mk(m, a, b)
    b = raw_input('What is the name of the author of this class? ') + "'s Homebrews"
    m = mk(m, a, b)
    return m

def Race():
    a = raw_input('Race Name: ')
    m = a + '.'
    b = raw_input('How many racial hit die does this race have? ') + '.'
    m = mk(m, a, b)
    b = raw_input('What size is the racial hit dice for this class? ') + '.'
    m = mk(m, a, b)
    b = raw_input('What base attack bonus does this race have from racial hit dice? ') + '.'
    m = mk(m, a, b)
    b = raw_input('How many skill points does this race have from racial hit dice?') + '.'
    m = mk(m, a, b)
    b = raw_input('What is the base fort save of this race? ') + '.'
    m = mk(m, a, b)
    b = raw_input('What is the base reflex save of this race? ') + '.'
    m = mk(m, a, b)
    b = raw_input('What is the base will save of this race? ') + '.'
    m = mk(m, a, b)
    b = raw_input('What bonus does this race get to STR (use + and the number for bonus or none and - with the number for penalty)') + '.'
    m = mk(m, a, b)
    b = raw_input('What bonus does this race get to DEX (use + and the number for bonus or none and - with the number for penalty)') + '.'
    m = mk(m, a, b)
    b = raw_input('What bonus does this race get to CON (use + and the number for bonus or none and - with the number for penalty)') + '.'
    m = mk(m, a, b)
    b = raw_input('What bonus does this race get to INT (use + and the number for bonus or none and - with the number for penalty)') + '.'
    m = mk(m, a, b)
    b = raw_input('What bonus does this race get to WIS (use + and the number for bonus or none and - with the number for penalty)') + '.'
    m = mk(m, a, b)
    b = raw_input('What bonus does this race get to CHA (use + and the number for bonus or none and - with the number for penalty)') + '.'
    m = mk(m, a, b)
    b = raw_input('What ECL does this race have?  (Use + with the number and +0 for no ECL)') + '.'
    m = mk(m, a, b)
    b = raw_input('What is the name of the author of this race? ') + "'s Homebrews"
    m = mk(m, a, b)
    return m

CF, RF = open('homebrew_classes.txt', 'a'), open('homebrew_races.txt', 'a')

G = raw_input('Are you installing a Class or a Race? (type class for class or race for race)  ')
if G == 'class':
    CF.write(Class() + '\n')
else:
    RF.write(Race() + '\n')

CF.close()
RF.close()
