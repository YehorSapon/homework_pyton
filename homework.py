weight = int(input("Увядзіце вашу вагу ў кг: "))
height = int(input("Увядзіце ваш рост у см: "))
BMI = (weight//((height/100)**2))
print(f"Ваш Індэкс масы цела (ІМЦ): {BMI}")
number1 = int((BMI-10)//3)
number2 = (20 - number1)
print("10","="*number1,"|","="*number2,"70")
"""
print(" менш за 18,5 кг/м² — нястача масы цела \n",
        "18,5—25 кг/м² — здаровая маса цела \n",
        "25—30 кг/м² — залішняя маса цела \n",
        "30—35 кг/м² — атлусценне 1-й ступені \n",
        "35—40 кг/м² — атлусценне 2-й ступені \n",
        "звыш 40 кг/м² — атлусценне 3-й ступені \n")
"""
