def is_k_good_number(num, k):
    digits = set(str(num))
    for i in range(k + 1):
        if str(i) not in digits:
            return False
    return True

def main():
    count = 0

    n, k = map(int, input().split(" "))

    for i in range(n):
        num = int(input())
        if is_k_good_number(num, k):
            count += 1

    print(count)

main()
