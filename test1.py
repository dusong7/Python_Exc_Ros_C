print("Hello world")
print 28+45
print 34*46

fred = 100;
john = fred
print john;

found_coins = 20
magic_coins = 10
stolen_coins = 3

print (found_coins + magic_coins * 365 - stolen_coins * 52)
stolen_coins = 2
print (found_coins + magic_coins * 365 - stolen_coins * 52)

fred = '''Why do gorillas have big nostrils?
Big fingers!!'''  ##
print fred;

single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
double_quote_str = "He said, \"Aren't can't shouldn't wouldn't.\""

print(single_quote_str)
print(double_quote_str)

myscore = 100
message = 'I scored %s is %s points'
print (message % (myscore,myscore))

print (10 * '1')

space = ' ' * 25
print('%s 12 Butts Wynd' % space)
print('%s Twinklebottom Heath' % space)
print('%s West Snoring' % space)
print()
print()
print('Dear Sir')
print()
print('I wish to report that tiles are missing from the')
print('outside toilet roof')
print('I think it was bad wind the other night that blew them away')
print()
print('Regards')
print('Malcolm Dithering')

##print(1000 * 'snirt')

wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']

print(wizard_list)



wizard_list[2] = 'Human hand'
print(wizard_list)
print(wizard_list[2:5])


numbers = [1,3,4,5,6,8]
string = ['Guo', 'Lulu', 'Chang', 'Shuting']
mylist = [numbers, string]
print(mylist)

wizard_list.append('Bear burp')
print(wizard_list)

del wizard_list[5]
print(wizard_list)

list1  = numbers * 5

print (list1)

print (numbers + string)

favorite_sport = {'A' : 'football',
                  'B' : 'Basketball',
                  'D' : 'Bjarb',
                  'C' : 'Netball',
                  'E' : 'Rugby' }

favorite_color = {'A' : 'Red',
                  'B' : 'Yellow',
                  'C' : 'Blue'}

##favorite_sport['D'] = 'Ice Hockey'

##print(favorite_sport + favorite_color)

##import turtle

##t = turtle.Pen()
##t.forward(40)

age  = 13
if age == 20 or age == 15 or age == 13:
    print('You are too old!')
elif age == 14:
    print('You are a 13!')
##else:
    ##

myval = None
print(myval)

if myval == None:
    print('It dose not have any value !')
age = 10
converted_age = str(age)

if converted_age == '10':
    print('Age is 10 !')


money = 200
if money > 1000:
    print("I am Rich!")
else:
    print("I'am not ritch")
    print("But I might be later")

for x in range(0, 10):
    print('Hello %s' % x)

print(list(range(10,20)))


for i in wizard_list:
    print(i)

hugehairypants = ['huge', 'hair', 'pants']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)
        
coins = found_coins
for week in range(1, 52):
    coins = coins + magic_coins - stolen_coins
    ##print('Week %s = %s', week, coins)

for step in range(1, 20):
    print(step)

x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print x, y
    
    if (x + y > 130):
        break

for x in range(0, 20):
    if (x % 2) == 0:
        print('hello %s' % x)

ingredients = ['snails', 'leeches', 'gorilla', 'cater']

for x in range(0,4):
    ##print(x+1)
    print(x+1),ingredients[x]
    
    
def testfunc(fname, lname):
    print('hello %s %s' %(fname, lname))

firstname = 'Joe'
secname = 'Robertson'

testfunc(firstname, secname)

def saving(pocket_money, paper_money, spending):
    return pocket_money + paper_money - spending

print (saving(10, 10, 5))

another_variable = 100
def variable_test():
    fir_variable = 10
    second_variable = 20
    return fir_variable * second_variable + another_variable

print(variable_test())
print(another_variable)

__author__ = 'Du'
print "Hello PyCharm IDE !"
print "Hello"

import time
print(time.asctime())

import sys
##print(sys.stdin.readline())

def silly_age_joke():
    print('How old are you ?')
    age = int(sys.stdin.readline())
    if age >=10 and age <= 13:
        print('What is 13+ 48 ? A headache')
    else:
        print('Huh!')

##age = sys.stdin.readline()
silly_age_joke()

class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class SideWalks(Inanimate):
    pass

class Animals(Animate):
    def brath(self):
        print('Breathing')
    def move(self):
        print('Moving')
    def eat_food(self):
        print('Eating Food')

class Mammal(Animals):
    def feed_young(self):
        print('Feeding young')

class Giraffes(Mammal):
    def eat_leaves_from_trees(self):
        self.eat_food()
    def find_food(self):
        self.move()
        print("I've found food !")
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

##reginald = Giraffes()

##reginald.dance_a_jig()

def this_is_a_normal_function():
    print('I am a normal function ')

class ThisIsMySillyClass():
    def this_is_a_function(self):
        print('I am a class function')
    def this_is_also_class_function(self):
        print('I am also a class funtion.see?')

##my = ThisIsMySillyClass()
##my.this_is_also_class_function()

class Spot_Grif:
    def __init__(self,spots):
        self.gira_spot = spots

oz = Spot_Grif(100)
ger = Spot_Grif(150)

print(oz.gira_spot)
print(ger.gira_spot)


calcu = input('Enter a calution ')

print(calcu)

print(len('1234534'))

creat_list = ['unicorn', 'cyclop','fairy']
print(len(creat_list))

string = 'A, a, B, c, C'
print(max(string))

count_by_twos = list(range(10,3,-3))
print(sum(count_by_twos))


file = open('C:\\file.txt','w')
##new = 'This is new Write'
file.write('Hello')
##text = file.read()
##print(text)
file.close()
file1 = open('C:\\file.txt')
text = file1.read()
print(text)


##page.69
