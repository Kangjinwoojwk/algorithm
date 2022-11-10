#include<iostream>
using namespace std;
int list[2000];
int main(int argc, char** argv)
{
	int test_case;
	int T, N;
	long long K;
	scanf("%d", &T);
	long long ans;
	long long div = 1e9 + 7;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %lld", &N, &K);
		ans = 0;
		for (int i = 0; i<N; ++i) {
			scanf("%d", &list[i]);
		}
		long long up = 0, down = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = i + 1; j < N; ++j) {
				if (list[i] == list[j]) continue;
				if (list[i] > list[j]) {
					++up;
				}
				else if (list[i] < list[j]) {
					++down;
				}
			}
		}
		long long n1 = (K * up) % div;
		long long n2 = (K*(K-1)/2) % div;
		n2 = ((up + down)*n2) % div;
		ans = (n1 + n2)%div;
		printf("#%d %lld\n", test_case, ans);
	}
	return 0;
}