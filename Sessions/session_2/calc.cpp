#include <iostream>

using namespace std;

int main() {
    int A, B;
    char op;

    cin >> A >> op >> B;

    switch (op)
    {
    default:
        cout << "Invalid operator";
        break;
    case '+':
        cout << A+B;
        break;
    case '-':
        cout << A-B;
        break;
    case '*':
        cout << A*B;
        break;
    case '/':
        if (B != 0)
            cout << A/B;
        else
            cout << "Can not divide by zero";
        break;
    }
    cout << endl;

    return 0;
}
