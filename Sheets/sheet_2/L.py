def get_kth_element(t):
    i = 1
    count = 0

    while True:
        if i % 3 != 0 and i % 10 != 3:
            count += 1
            if count == t:
                return i

        i += 1

def main():
    n = int(input())

    for i in range(n):
        t = int(input())
        print(get_kth_element(t))

main()
