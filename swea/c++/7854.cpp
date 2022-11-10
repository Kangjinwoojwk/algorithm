#include<iostream>
using namespace std;
long long list[2000] = { 1, 2, 5, 10, 20, 25, 50, 100, 125, 200, 250, 500, };
int chk = 12;
int main(int argc, char** argv)
{
	long long test_case;
	long long T, N;
	scanf("%d", &T);
	for (long long i = 10; i <= 10000000; i *= 10) {
		for (long long j = 7; j < 12; j++) {
			list[chk] = list[j] * i;
			++chk;
		}
	}
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
		int ans = 0;
		while (list[ans] <= N) {
			++ans;
		}
		printf("#%d %d\n", test_case, ans);
	}
	return 0;
}