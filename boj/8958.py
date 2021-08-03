test_case = int(input())
for _ in range(test_case):
    answers = input()
    points = 0
    series = 0
    for i in answers:
        if i == 'O':
            series += 1
            points += series
        else:
            series = 0
    print(points)