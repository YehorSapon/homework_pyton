"""Coding DNA.
Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
то есть группы одинаковых символов исходной строки
заменяются на этот символ и количество его повторений
в этой позиции строки.
Напишите программу, которая считывает строку,
кодирует её предложенным алгоритмом и выводит
закодированную последовательность на стандартный вывод.
Кодирование должно учитывать регистр символов.
"""


dna = input()
new = ""
cnt = 1
L = int(len(dna))
first_chair = dna[0]
last_chair = dna[-1]
chair = first_chair
new = f"{chair}{cnt}"
if L == 1:
    print(new)
elif L == 0:
    print()
else:
    for i in range(1, (L-1)):
        if dna[i] == dna[i-1]:
            chair = dna[i-1]
            cnt += 1
            if cnt <= 10:
                new = new[:-1] + str(cnt)
            elif 101 <= cnt <= 1000:
                new = new[:-3] + str(cnt)
            elif 1001 <= cnt <= 10000:
                new = new[:-4] + str(cnt)
            elif 10001 <= cnt <= 100000:
                new = new[:-5] + str(cnt)
            else:
                new = new[:-2] + str(cnt)
        else:
            cnt = 1
            chair = dna[i]
            new += f"{chair}{cnt}"
    if last_chair == dna[-2]:
        chair = dna[-2]
        cnt += 1
        if cnt <= 10:
            new = new[:-1] + str(cnt)
        elif 101 <= cnt <= 1000:
            new = new[:-3] + str(cnt)
        elif 1001 <= cnt <= 10000:
            new = new[:-4] + str(cnt)
        elif 10001 <= cnt <= 100000:
            new = new[:-5] + str(cnt)
        else:
            new = new[:-2] + str(cnt)
    else:
        cnt = 1
        chair = last_chair
        new += f"{chair}{cnt}"
    print(new)
input("Put in enter to out")
