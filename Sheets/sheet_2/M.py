def int_listing(num):
    length = 0
    digits = []

    if num == 0:
        return [0], 1

    while num != 0:
        length += 1
        digits.append(num % 10)
        num //= 10

    return digits, length

def is_good_k(num, k):
    if num == 0:
        return False

    digits, num_len = int_listing(num)
    if num_len != k + 1:
        return False

    digits.sort()
    for i in range(num_len - 1):
        if digits[i] == digits[i + 1] or digits[i] > k:
            return False

    if digits[num_len - 1] > k:
        return False

    return True

def main():
    count = 0

    n, k = map(int, input().split(" "))

    for i in range(n):
        num = int(input())
        if is_good_k(num, k):
            count += 1

    print(count)

main()
