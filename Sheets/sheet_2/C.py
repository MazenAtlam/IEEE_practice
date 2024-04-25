def is_almost_lucky(num):
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 744, 477, 747, 774, 777]

    for n in lucky_numbers:
        if num % n == 0:
            return True

    return False

def main():
    n = int(input())

    if is_almost_lucky(n):
        print("YES")
    else:
        print("NO")

main()
