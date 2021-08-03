docu = input()
word = input()
counts = 0

i = 0
while i<len(docu):
    appeared = True
    for char in word:
        if i<len(docu) and docu[i] != char:
            appeared = False
            i += 1
            break
        i += 1
    if appeared == True:
        counts += 1

print(counts)