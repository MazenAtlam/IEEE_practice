def is_in_sequence(t, a, b, item):
    flag = False

    if t > item:
        if a != 1 and is_in_sequence(t, a, b, item * a):
            flag = True
        elif b != 0:
            flag = is_in_sequence(t, a, b, item + b)
    elif t == item:
        flag = True

    return flag

def main():
    n = int(input())
    
    for i in range(n):
        t , a, b = map(int, input().split(" "))
        
        if is_in_sequence(t, a, b, 1):
            print("Yes")
        else:
            print("No")

main()
