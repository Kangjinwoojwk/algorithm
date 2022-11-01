#include<iostream>
using namespace std;
char board[8][8];
int palindrome(int n) {
	int end = 9 - n;
	int cnt = 0;
	int half = n/2;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < end; j++) {
			int chk = 1;
			for (int k = 0; k < half; k++) {
				if (board[i][j + k] != board[i][j + n - 1 - k]) {
					chk = 0;
					break;
				}
			}
			cnt += chk;
			chk = 1;
			for (int k = 0; k < half; k++) {
				if (board[j + k][i] != board[j + n - 1 - k][i]) {
					chk = 0;
					break;
				}
			}
			cnt += chk;
		}
	}
	return cnt;
}
int main(int argc, char** argv)
{
	int test_case;
	int T, N;
	T = 10;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N;
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				cin >> board[i][j];
			}
		}
		cout << '#' << test_case <<' '<< palindrome(N);
	}
	return 0;
}