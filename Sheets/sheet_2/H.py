def main():
    passengers = 0
    capacity = passengers
    n = int(input())
    
    for i in range(n):
        a, b = map(int, input().split(" "))

        if passengers <= a:
            passengers = 0
        else:
            passengers -= a

        passengers += b
        if passengers > capacity:
            capacity = passengers

    print(capacity)

main()
