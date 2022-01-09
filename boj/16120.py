"""p = input()

if len(p) < 4:
    print("NP")
    exit()

word = p[:4]

for x in p[4:]:
    word += x
    if word[-4:] == "PPAP":
        word = word[:-3]

if word == "P" or word == "PPAP":
    print("PPAP")
else:
    print("NP")"""

p = list(input())
if len(p) < 4:
    print("NP")
    exit()

word = p[:4]

for x in p[4:]: # 길이가 5이상
    word.append(x)
    if len(word) >= 4 and word[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            word.pop()
    
print(word)
if word == ['P'] or word == ['P', 'P', 'A', 'P']:
    print("PPAP")
else:
    print("NP")