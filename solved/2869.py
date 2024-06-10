import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
Walkthrough = 0
Time = 0

# case of small V
if (V - A) // (A - B) <= 2:
    while Walkthrough < V:
        Walkthrough += A
        Time += 1
        if Walkthrough >= V:
            break
        Walkthrough -= B

    print(Time)
# But this code is too slow
else:
# Skip the loop
# Daily Walkthrough = A - B

# Judge the time nearby mathmatical division result 'Time'(MDR)
# Let the nearby is MDR - 2
# And Lets subtract A from V because effect of A in last day is maybe big
    NearTime = ((V - A) // (A - B)) - 2
    while (A - B) * NearTime < V:
        if (A - B) * NearTime + A >= V:
            NearTime += 1
            break
        else:
            NearTime += 1
    Time = NearTime
    print(Time)