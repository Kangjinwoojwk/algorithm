#include<iostream>
using namespace std;
//0 0 1 0 0 1 1 0 0 0 1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 0 1 1 0 1 1

//0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0

int main(int argc, char** argv)
{
	int test_case;
	int T;
	long long K;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> K;
		K--;
		int ans = 0;
		while (K % 2) {
			K = K / 2;
		}
		if (K % 4 == 0) ans = 0;
		else if (K % 2 == 0) ans = 1;

		cout << '#' << test_case << ' ' << ans << '\n';
	}
	return 0;
}