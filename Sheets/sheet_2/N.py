def get_last_digit(n):
    if n == 0:
        return 6
    elif n == 1:
        return 8
    elif n == 2:
        return 4
    else:
        return 2

def main():
    n = int(input())

    if n == 0:
        print (1)
    else:
        print(get_last_digit(n % 4))

main()
