r"""Доделать BMI

Дозапросить пол и возраст Выдавать рекомендации 10 градаций:

2 пола и по 3 рекомендаци для каждого + возраст
print(" менш за 18,5 кг/м² — нястача масы цела \n",
        "18,5—25 кг/м² — здаровая маса цела \n",
        "25—30 кг/м² — залішняя маса цела \n",
        "30—35 кг/м² — атлусценне 1-й ступені \n",
        "35—40 кг/м² — атлусценне 2-й ступені \n",
        "звыш 40 кг/м² — атлусценне 3-й ступені \n")
"""


gender = int(input("Увядзіце 1 калі вы мужчына і 2 калі жанчына: "))
age = int(input("Колькі вам поўных год: "))
weight = int(input("Увядзіце вашу вагу ў кг: "))
height = int(input("Увядзіце ваш рост у см: "))
BMI = (weight//((height/100)**2))
print(f"Ваш Індэкс масы цела ( ІМЦ ) : {BMI}")
number1 = int((BMI-10)//3)
number2 = (20 - number1)
print("10" + "=" * number1 + "|" + "=" * number2 + "70")
if gender == 1:
    if age <= 20 and BMI <= 18.5:
        print("Хлопчык табе трэба больш есці")
    elif age <= 20 and 18.5 < BMI <= 25:
        print("Хлопчык ты малайчына ты здароў")
    elif age <= 20 and BMI > 25:
        print("Хлопчык табе трэба больш рухацца")
    elif 20 < age <= 40 and BMI <= 18.5:
        print("Мужчына вам трэба больш есці")
    elif 20 < age <= 40 and 18.5 < BMI <= 25:
        print("Мужчына вы малайчына вы здаровы")
    elif 20 < age <= 40 and BMI > 25:
        print("Мужчына табе трэба больш рухацца")
    elif age > 40 and BMI <= 18.5:
        print("Дзядуля вам трэба больш есці")
    elif age > 40 and 18.5 < BMI <= 25:
        print("Дзядуля вы малайчына вы здароў")
    elif age > 40 and BMI > 25:
        print("Дзядуля табе трэба больш рухацца")
else:
    if age <= 20 and BMI <= 18.5:
        print("Дзяўчынка табе трэба больш есці")
    elif age <= 20 and 18.5 < BMI <= 25:
        print("Дзяўчынка ты малайчына ты здароў")
    elif age <= 20 and BMI > 25:
        print("Дзяўчынка табе трэба больш рухацца")
    elif 20 < age <= 40 and BMI <= 18.5:
        print("Жанчына вам трэба больш есці")
    elif 20 < age <= 40 and 18.5 < BMI <= 25:
        print("Жанчына вы малайчына вы здаровы")
    elif 20 < age <= 40 and BMI > 25:
        print("Жанчына табе трэба больш рухацца")
    elif age > 40 and BMI <= 18.5:
        print("Бабуля вам трэба больш есці")
    elif age > 40 and 18.5 < BMI <= 25:
        print("Бабуля вы малайчына вы здаровы")
    elif age > 40 and BMI > 25:
        print("Бабуля вам трэба больш рухацца")
