#include <iostream>
#include <cmath>

using namespace std;

int num_length(int num){
    int length = 0;

    if (num == 0)
        return 1;

    while (num != 0){
        length += 1;
        num /= 10;
    }

    return length;
}

int main(){
    int N, N_len, i, total = 0;

    cin >> N;

    N_len = num_length(N);
    for (i = 1; i < N_len; i += 2)
        total += pow(10, i - 1) * 9;

    if (N_len % 2 != 0)
        total += N - pow(10, N_len - 1) + 1;

    cout << total;

    return 0;
}
