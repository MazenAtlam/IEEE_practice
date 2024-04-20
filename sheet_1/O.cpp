#include <iostream>

using namespace std;

int main() {
	int N, K, X, Y, cost;

	cin >> N >> K >> X >> Y;

	if (N < K)
		K = N;

	cost = (K * X) + ((N - K) * Y); 

	cout << cost << endl;

	return 0;
}
