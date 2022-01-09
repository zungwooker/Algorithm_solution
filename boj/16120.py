p = list(input())
if p == ['P'] or p == p['P', 'P', 'A', 'P']:
    print("PPAP")
    exit()
    
if len(p) < 4:
    print("NP")
    exit()

word = p[:4] # 앞 4글자 입력
print(word)
for x in p[4:]: # 길이가 5이상, 5번째 글자부터 입력
    word.append(x)
    print(word)
    if len(word) >= 4 and word[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            word.pop()
        print(word)
    
print("final",word)
if word == ['P'] or word == ['P', 'P', 'A', 'P']:
    print("PPAP")
else:
    print("NP")