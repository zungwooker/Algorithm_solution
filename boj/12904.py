S = input()
T = input()

def answer(s,t,updown):
    if not updown:
        answer = "".join(reversed(t))
    else:
        answer = t

    if s == answer:
        print(1)
    else:
        print(0)

counter = len(T)-len(S)
front = 0
back = -1
start = True

while counter:
    if start:
        if T[back] == 'B':
            start = False
        back -= 1
        counter -= 1
    else:
        if T[front] == 'B':
            start = True
        front += 1
        counter -= 1

if back == -1:
    answer(S,T[front:],start)
else:
    answer(S,T[front:back+1],start)


            
