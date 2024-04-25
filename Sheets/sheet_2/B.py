def max_ammount(fruits):
    for i in range(fruits[0], -1, -1):
        if (i * 2) <= fruits[1] and (i * 4) <= fruits[2]:
            break

    return i * 7

def main():
    fruits = []
    for i in range(3):
        fruits.append(int(input()))
    
    print(max_ammount(fruits))

main()
