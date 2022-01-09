p = input()
if p == 'P' or p == 'PPAP':
    print('PPAP')
    exit()

if len(p) < 4:
    print("NP")
    exit()

word = []
for x in p: # 길이가 5이상, 5번째 글자부터 입력
    word.append(x)
    if len(word) >= 4 and word[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            word.pop()

if word == ['P'] or word == ['P', 'P', 'A', 'P']:
    print("PPAP")
else:
    print("NP")