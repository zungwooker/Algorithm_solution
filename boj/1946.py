import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    N = int(sys.stdin.readline().rstrip())
    volunteers = [0]*(N+1)
    passedApplicants = 1

    for _ in range(N):
        resume, interview = map(int, sys.stdin.readline().rstrip().split())
        volunteers[resume] = interview
    
    minInter = volunteers[1]
    for i in range(1, N+1):
        if volunteers[i] < minInter:
            passedApplicants += 1
            minInter = volunteers[i]

    print(passedApplicants)
