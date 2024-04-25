def who_win(m, c):
    if m > c:
        return 'm'
    
    if c > m:
        return 'c'
    
    return 'd'

def main():
    m_win = 0
    c_win = 0
    n = int(input())
    
    for i in range(n):
        m, c = map(int, input().split(" "))
        
        ch = who_win(m, c)
        
        if ch == 'm':
            m_win += 1
        elif ch == 'c':
            c_win += 1

    if m_win > c_win:
        print("Mishka")
    elif c_win > m_win:
        print("Chris")
    else:
        print("Friendship is magic!^^")

main()
