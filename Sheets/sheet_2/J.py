def main():
    no_of_officers = 0
    no_of_crimes = 0

    n = int(input())
    events = list(map(int, input().split(" ")))

    for i in range(n):
        if events[i] == -1:
            if no_of_officers != 0:
                no_of_officers -= 1
            else:
                no_of_crimes += 1
        else:
            no_of_officers += events[i]

    print(no_of_crimes)

main()
