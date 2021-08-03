testcase = int(input())

for _ in range(testcase):
    scores = list(map(int, input().split()))
    sumOfScores = 0
    upper = 0
    for i in scores[1:]:
        sumOfScores += i
    avg = float(sumOfScores/scores[0])
    for i in scores[1:]:
        if avg < i:
            upper += 1
    percent = '{0:0.3f}%'.format(float(upper/scores[0]*100))
    print(percent)
