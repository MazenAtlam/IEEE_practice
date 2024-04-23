#include <iostream>

using namespace std;

int sum(int num) {
    if (num <= 1)
        return 1;

    return num + sum(num - 1);
}

int factorial(int num) {
    if (num <= 1)
        return 1;

    return num * factorial(num - 1);
}

int main() {
    int n, choice;
    bool not_valid = true;

    cin >> choice;

    while (not_valid)
    {
        switch (choice) {
            case 1:
                cin >> n;
                cout << sum(n);
                not_valid = false;
                break;
            case 2:
                cin >> n;
                cout << factorial(n);
                not_valid = false;
                break;
            default:
                cout << "Invalid choice";
                not_valid = true;
                break;
        }
        cout << endl;
    }

    // for(a = 10; a < 16; a++) {
    //     if (a == 13)
    //         continue;
    //     cout << a << endl;
    // }
    // cout << a << endl;

    return 0;
}
