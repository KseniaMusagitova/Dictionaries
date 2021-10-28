car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000}
print(car_prices)
print(car_prices['toyota'])

car_prices['mazda'] = 4000
print(car_prices)

car_prices['mazda'] = 6000
print(car_prices)

del car_prices['toyota']
print(car_prices)

car_prices.clear()
print(car_prices)

person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daughter': 'Pamela'}
}
print(person['age'])
print(person['hobbies'])
# 1 способ
hobbies = person['hobbies']
print(hobbies[2])
# 2 способ
print(person['hobbies'][2])

children = person['children']
print(children['son'])
print(person['children']['son'])

person['car'] = 'mazda'
person['hobbies'][0] = 'basketball'
print(person)

# ключи и значения
print(person.keys())
print(person.values())

print(person.items())

# примеры

students = {'5 class': 10, '6 class': 13}
print(students['6 class'])

computer = {
    'RAM': 4,
    'processor': 'Pentium',
    'year': 2
}
print(computer)