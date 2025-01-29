from random import *


caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special = '!@#$%*_'
allsymbols = 'abcdefghijklmnopqrstuvwxyz'

first_wish = input('Приветствую тебя в Генераторе паролей! Сколько символов ты желаешь увидеть в пароле?')
first_wish = int(first_wish)
second_wish = input('Хочешь ли ты видеть в пароле буквы, написанные капсом? (да/нет)')

if second_wish == 'да':
    third_wish = input('Хорошо. Как насчет чисел? (да/нет)')
    allsymbols = allsymbols + caps
if second_wish == 'нет':
    third_wish = input('Ладно. Как насчет чисел? (да/нет)')

if third_wish == 'да':
    four_wish = input('Как насчет специальных символов в твоем пароле? (да/нет)')
    allsymbols = allsymbols + numbers
if third_wish == 'нет':
    four_wish = input('А что думаешь по поводу спец. символов? (да/нет)')

if four_wish == 'да':
    fifth_wish = print('Отлично!')
    allsymbols = allsymbols + special
if four_wish == 'нет':
    fifth_wish = print('Ну ладно.')
print("Идёт генерация пароля, подождите...")

password = ""
for i in range(first_wish):
    password = password + choice(allsymbols)

print('Твой пароль готов! Вот он:' , password)
print("В твоем пароле", first_wish, "символов!")
