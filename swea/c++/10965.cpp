#include<iostream>
using namespace std;
bool ast[10000001];
int list[3500];
int prime_cnt = -1;
int main(int argc, char** argv)
{
	int test_case;
	int T, N;
	scanf("%d", &T);
	ast[0] = true;
	ast[1] = true;
	for (int i = 2; i <= 3200; ++i) {
		if (ast[i]) continue;
		else list[++prime_cnt] = i;
		for (int j = 2 * i; j < 10000001; j += i) {
			if (ast[j]) {
				continue;
			}
			ast[j] = true;
		}
	}
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
		int ans = 1;
		if (!ast[N]) {
			printf("#%d %d\n", test_case, N);
			continue;
		}
		int idx = 0;
		int cnt = 0;
		while (N != 1) {
			if (!(N%list[idx])) {
				++cnt;
				N /= list[idx];
			}
			if (N%list[idx]) {
				if ((cnt % 2)) ans *= list[idx];
				if (!ast[N]) {
					ans *= N;
					break;
				}
				if (idx == prime_cnt) {
					ans *= N;
					break;
				}
				++idx;
				cnt = 0;
			}
		}
		printf("#%d %d\n", test_case, ans);
	}
	return 0;
}