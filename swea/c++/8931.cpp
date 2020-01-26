#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;
	int* st;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int K;
		cin >> K;
		int idx = 0;
		st = new int[K];
		int temp, answer = 0;
		for (int i = 0; i<K; i++) {
			cin >> temp;
			if (temp == 0) {
				--idx;
			}
			else {
				st[idx++] = temp;
			}
		}
		for (int i = 0; i<idx; i++) {
			answer += st[i];
		}
		cout << '#' << test_case << ' ' << answer << '\n';
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}