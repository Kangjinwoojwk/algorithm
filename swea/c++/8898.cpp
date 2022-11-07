#include<iostream>
#include <algorithm>
using namespace std;
int cows[500000];
int horses[500000];
int main(int argc, char** argv)
{
	int test_case;
	int T, N, M, c1, c2, min_distance, ans, cow_idx, horse_idx, temp_distance;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &M);
		scanf("%d %d", &c1, &c2);
		min_distance = 1 << 30;
		ans = 0;
		for (int i = 0; i < N; i++)scanf("%d", &cows[i]);
		for (int i = 0; i < M; i++)scanf("%d", &horses[i]);
		sort(cows, cows + N);
		sort(horses, horses + M);
		cow_idx = 0;
		horse_idx = 0;
		while (cow_idx < N && horse_idx < M) {
			if (cows[cow_idx] > horses[horse_idx]) {
				temp_distance = cows[cow_idx] - horses[horse_idx];
				if (temp_distance < min_distance) {
					min_distance = temp_distance;
					ans = 1;
				}
				else if (temp_distance == min_distance) {
					ans++;
				}
				horse_idx++;
			}
			else {
				temp_distance = horses[horse_idx] - cows[cow_idx];
				if (temp_distance < min_distance) {
					min_distance = temp_distance;
					ans = 1;
				}
				else if (temp_distance == min_distance) {
					ans++;
				}
				cow_idx++;
			}
		}
		min_distance += abs(c1 - c2);
		cout << '#' << test_case << ' ' << min_distance << ' ' << ans << '\n';
	}
	return 0;
}