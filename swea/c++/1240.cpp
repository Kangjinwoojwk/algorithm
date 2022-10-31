#include<iostream>
#include<algorithm>
using namespace std;
char number[10][8] = { "0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011" };
int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int N, M;
		cin >> N >> M;
		int ans = 0;
		int chk_ans = 0;
		char** code;
		code = new char*[N];
		char code_get[56];
		for (int i = 0; i < N; i++) {
			code[i] = new char[M];
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cin >> code[i][j];
			}
		}
		bool chk = false;
		for (int i = 0; i < N; i++) {
			for (int j = M - 1; j >= 0; j--) {
				if (code[i][j] == '1') {
					for (int k = 0; k < 56; k++) {
						code_get[k] = code[i][j - 55 + k];
					}
					chk = true;
					break;
				}
			}
			if (chk) {
				break;
			}
		}
		for (int i = 0; i < 56; i += 7) {
			for (int j = 0; j < 10; j++) {
				if (code_get[i] == number[j][0] && code_get[i + 1] == number[j][1] && code_get[i + 2] == number[j][2] && code_get[i + 3] == number[j][3] && code_get[i + 4] == number[j][4] && code_get[i + 5] == number[j][5] && code_get[i + 6] == number[j][6]) {
					ans += j;
					if (i % 2) {
						chk_ans += j;
					}
					else {
						chk_ans += 3 * j;
					}
				}
			}
		}
		if (chk_ans % 10) {
			cout << "#" << test_case << " " << "0"<<"\n";
		}
		else {
			cout << "#" << test_case << " " << ans << "\n";
		}
		
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}