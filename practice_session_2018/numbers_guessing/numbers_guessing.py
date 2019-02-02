t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    n = int(input())
    lower_bound = a+1
    higher_bound = b
    guess_number = (lower_bound+higher_bound)//2
    print(guess_number)
    reply = input()
    while reply not in ['CORRECT', 'WRONG_ANSWER']:
        if reply == 'TOO_SMALL':
            lower_bound = guess_number+1
        else:
            higher_bound = guess_number-1
        guess_number = (lower_bound + higher_bound) // 2
        print(guess_number)
        reply = input()
