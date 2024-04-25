def append_list(original, new):
    for element in new:
        original.append(element)

def generate_lucky_list(no_of_digits):
    lucky_digit = [4, 7]
    lucky_list = []

    if no_of_digits <= 1:
        return lucky_digit

    previous_list = generate_lucky_list(no_of_digits - 1)
    for i in range(2):
        higher_digit = lucky_digit[i] * (10 ** (no_of_digits - 1))
        append_list(lucky_list, list(map(lambda n: n + higher_digit, previous_list)))

    return lucky_list

def num_length(num):
    length = 0

    while num != 0:
        length += 1
        num //= 10

    return length

def next_lucky_num(num, lucky_numbers):
    for lucky_num in lucky_numbers:
        if num <= lucky_num:
            return lucky_num

def main():
    sum = 0
    start, last = map(int, input().split(" "))
    num_len = num_length(start)
    lucky_numbers = generate_lucky_list(num_len)
    max_lucky = 0

    max_lucky = lucky_numbers[-1]

    for num in range(start, last + 1):
        if num == max_lucky:
            sum += max_lucky
            continue

        elif num > max_lucky:
            max_lucky = 0
            num_len += 1
            lucky_numbers = generate_lucky_list(num_len)
            max_lucky = lucky_numbers[-1]

        sum += next_lucky_num(num, lucky_numbers)

    print(sum)

main()
