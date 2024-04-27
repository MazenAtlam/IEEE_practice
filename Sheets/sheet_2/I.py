def main():
    n, k = map(int, input().split(" "))

    for i in range(k):
        if n == 0:
            break

        ld = n % 10
        if ld != 0:
            n -= 1
        else:
            n //= 10

    print(n)

main()
