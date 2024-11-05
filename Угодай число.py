import random
popitok = 0
name = input("Привет! Как тебя зовут?")
print("Приятно познакомится,", str(name) ,"Готов ли ты сыграть в ИГРУ!?")
cislo = 0
print("Угодаешь число которое я загодал")
sluc = random.randint(1,100)

while cislo != sluc:
    cislo = input("Как думаешь что за число я загадал?")
    popitok += 1
    if int(cislo) > int(sluc) :
        print("ДАЖЕ ДЛЯ МЕНЯ ЭТО МНОГОВАТО")
    elif int(cislo) < int(sluc) :
        print("Я БЫ ТАК МАЛО НЕ ЗАГОДАЛ")
    else :
        print("Ты Выйграл За", popitok ,"попыток! Молодец!")
        break
    
exit