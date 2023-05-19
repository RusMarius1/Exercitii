file = open("C:\\Users\\Marius\\Desktop\\Laborator.txt", 'r+')
txt = file.read()
v = txt.split('\n')
i = 0
while i < len(v):
    print(v[i])
    i += 1
print(v)
for i in range(len(v)):
    if v[i].startswith('7'):
        v.insert(i, '5555')
        v.insert(i + 1, 6666)
        break
print(v)
f5 = 0
f6 = 0
for i in range(len(v)):
    if v[i].startswith('5'):
        f5 = 1
    if v[i].startswith('6'):
        f6 = 1
    if v[i].startswith('7'):
        if f5 == 0:
            v.insert(i, '5555')
        if f6 == 0:
            v.insert(i, '6666')
        break
print(v)
file.close()
file = open("C:\\Users\\Marius\\Desktop\\Laborator.txt", 'w+')
for e in v:
    file.write(e)
    file.write('\n')

file.close()

file = open("C:\\Users\\Marius\\Desktop\\Laborator.txt",'w+')
file.seek(0)
line = file.readline()
while line !='':
    if line.startswith('7'):
        file.seek(file.tell()-len(line)-1)
        file.write('5555\n')
        file.write(line)
    print(line)
    print(file.tell())
    line = file.readline()
file.close()
file = open("C:\\Users\\Marius\\Desktop\\Laborator.txt", 'r+')
file.seek(0)
line = file.readline()
while line !='':
    if line.startswith('7'):
        file.seek(file.tell())
        file.writelines('5555\n')
        file.write(line)
    print(line)
    print(file.tell())
    line = file.readline()
file.close()
