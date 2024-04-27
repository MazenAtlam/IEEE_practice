def main():
    count = 0
    n = int(input())

    for i in range(n):
        members, capacity = map(int, input().split(" "))

        if capacity - members >= 2:
            count += 1

    print(count)

main()
