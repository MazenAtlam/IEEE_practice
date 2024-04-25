def int_listing(num):
    length = 0
    digits = []

    while num != 0:
        length += 1
        digits.append(num % 10)
        num //= 10

    return digits, length

def sorting(digits, length):
    sorted_num = 0
    
    if length > 1 :
        digits.sort()

        if digits[0] == 0:
            for i in range(1, length):
                if digits[i] != 0:
                    digits[0], digits[i] = digits[i], digits[0]
                    break

    for i in range(length):
        sorted_num += digits[i] * (10 ** (length - i - 1))

    return sorted_num

def main():
    n = int(input())
    m = int(input())
    
    digits, n_len = int_listing(n)
    
    if n_len != int_listing(m)[1]:
        print("WRONG_ANSWER")
        return

    sorted_n = sorting(digits, n_len)

    if sorted_n == m:
        print("OK")
    else:
        print("WRONG_ANSWER")

main()
