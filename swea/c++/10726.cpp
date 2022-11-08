#include<iostream>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T, N, M;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N >> M;
		bool ans = true;
		int temp = (1 << N) - 1;
		M = M & temp;
		M = M ^ temp;
		cout << '#' << test_case << ' ';
		if (!M) cout << "ON\n";
		else cout << "OFF\n";
	}
	return 0;
}