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
if dna:
    new = ""
    cnt = 1
    L = int(len(dna))
    first_chair = dna[0]
    last_chair = dna[-1]
    chair = first_chair
    new = f"{chair}{cnt}"
    if L > 1:
        for i in range(1, (L-1)):
            if dna[i] == dna[i-1]:
                cnt += 1
                chair = dna[i-1]
                if cnt > 9:
                    new = new[:-2] + str(cnt)
                else:
                    new = new[:-1] + str(cnt)
            else:
                cnt = 1
                chair = dna[i]
                new += f"{chair}{cnt}"
        if last_chair == dna[-2]:
            cnt += 1
            chair = dna[-2]
            new = new[:-2] + f"{chair}{cnt}"
        else:
            cnt = 1
            chair = last_chair
            new += f"{chair}{cnt}"
        print(new)
    else:
        print(new)
else:
    print(dna)
input("Put in enter to out")
