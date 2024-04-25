def take_inputs():
    n, v = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    return n, v, a, b

def min_ratio(arr, size):
    minimum = arr[0]
    for i in range(1, size):
        if arr[i] < minimum:
            minimum = arr[i]

    return minimum

def calc_volume(a, x, size):
    vol = 0

    for i in range(size):
        vol += a[i] * x

    return vol

def calc_ratio(a, b, size):
    arr = []
    
    for i in range(size):
        arr.append(b[i] / a[i])

    return arr

def main():
    n, v, a, b = take_inputs()

    arr = calc_ratio(a, b , n)
    x = min_ratio(arr, n)
    real_v = calc_volume(a, x, n)
    if real_v <= v:
        print('{0:.4f}'.format(real_v))
    else:
        print('{0:.4f}'.format(v))

main()
