
'''
a = (17*3) 
b = (12*5)
c = a > b
d = a < b
e = a == b
print('a болььше или b:',c)
print('a меньше чем b:',d)
print('a и b равны ли они:',e)

a = 17925
b = 34**2 > a
c = 26*3 > a
d = 17**33 > a
e = 4394 > a
print(d,c,b,e)
'''
'''
a = 120
b = 80
c = 50
d = 193432
reshenie = (193432-(a + b * 5 ))
print(reshenie)
'''
'''
a = 25
b = 20
c = 30
if a > b :
	print('верно')
if a > c :
	print('не верно')
if a > b :
	print('верно')
'''
'''
a = 7
b = 3
c = 4.8
gaws = ((a % b)*4.8)
print(gaws)
'''
'''
vyrajenie1 = 455+200
vyrajenie2 = 200+455
asus = vyrajenie1 == vyrajenie2
if vyrajenie1 == vyrajenie2:
	print('все верно')
'''
'''
gig = 12**7
hih = 23**3
if gig != hih:
	print('все верно')
'''
'''
ds = 2**3
marvel = 3**2
	print('неверно') 
elif ds < marvel:
	print('верно')
'''
'''
a = int(input('введите '))
if a % 2:
	print('положительный число')

if a % 3:
	print('отрицательное число')
'''
'''
a = range(0, 21)
b = range(57, 100)
numb = int(input('веди число'))
if numb in a :
	print('разрешенные числа')
elif numb in b:
	print('не разрешенные числа')
'''

































'''

brawl = range ( 0, 51)
stars = range (52 ,100)
pam = int(input('введите букву'))
if pam in brawl:
	print('ращрешенные числа')
-0_)=elif pam in stars:
	print('неразрешенные числа')
'''
'''
a = 10//5
b = 10/5
if a == b:
	print('равны')
elif a != b:
	print('не равны')
'''
'''
dict = {'Вид компьютера':['ноутбук','ПК']}
type = str(input(' вид компьтера:'))
if type == 'ноутбук':
	print ('хорошо')
elif type == 'пк':
	print('понял')
else:
	print('к сожалению у нас нет этого товара')
ozu = str(input('размер памяти оперативки:'))
if ozu > '4' :
	print ('понял')
dss = {'TYPE':['ssd','hdd']}
print(dss)
ssd  = str(input(' тип накопителя'))
if ssd == 'ssd':
	print ('хоршо')
memore = int(input(' размер ' + str(ssd) ))
if memore == 256:
	print ('отличный выбор')
elif memore == 500:
	print('супермегабебра хорошш')
cost = int(input('укажите сумму' + str(type)))
if cost < 100000:
	print('спасибо за покупку')
elif cost == 100000:
	print(' ваш ' + str(dict) + ' превысил сумму ')
'''
'''
age = int(input('Укажите возраст'))
if age > 18:
	print(' Совершеннолетний ')
elif age == 18:
	print(' Совершеннолетний ')
else:
	print(' Несовршеннолетний ')
'''
'''
a = {'a4 всем влад': ['влад', 'влад' ,'влад', 'привет', 'влад', 'с вами влад а четырее глент кобяков серега']}
a.update({'opfg':['cfgopdjhotddhjothid']})
print(a)
'''
'''
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}

print(menu)

menu.update({'besh_barmak': 130})

print(menu)

menu.update({'lagman' : 135})

print(menu)

menu.pop('borsh')

print(menu)

menu2 = {'Drinks':['Coca Cola','Fanta','Sprite']}

print(menu2)

menu2.update({'Natural juices' : ['orange']})

print(menu2)

menu2.pop('Drinks')

print(menu2)
'''











































'''
cars = {'Машины':['мерседес'],'Дома'   :['особняк']}
print (cars)
cars.update({'Спорт Кары':['астон' 'мартин' 'масерати' 'бугатти']})
print(cars)
cars.update({'Собаки':['овчарки','доберманы','питбули']})
print(cars)
cars.update({'Каналы':['cartoon network''nickelodeon']})
print (cars)
cars.update({'Игры':['gta5','mafia2','cod']})
print (cars)
'''

dict = {'name':['Bob'],'age':['25'],'Job':['Dev']}
