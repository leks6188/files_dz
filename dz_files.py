names = ['1.txt', '2.txt', '3.txt']
a = []
for i in names:
    with open(i,'r', encoding='UTF-8') as f:
        h = f.read()
        a.append((len(h.split('\n')),i,h))

b = sorted(a)

with open('result.txt', 'r+', encoding="UTF-8" ) as w:
     for j in b:
         w.write(j[1]+'\n')
         w.write(str(j[0])+'\n')
         w.write(j[2]+'\n')
