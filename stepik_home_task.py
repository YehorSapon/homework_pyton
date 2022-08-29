dna = input()
new = ""
cnt = 1
L = int(len(dna))
first_chair = dna[1]
last_chair = dna[-1]
chair = first_chair
new = f"{chair}{cnt}"
for i in range(1,(L-1), 1):
    if dna[i] == dna[i-1]:
        cnt += 1
        chair = dna[i-1]
        new = new[:-1] + str(cnt)
    else:
        cnt = 1
        cnair = dna[i]
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
