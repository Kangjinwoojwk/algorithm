#include<iostream>
#include<queue>
#include<vector>
#include<math.h>
using namespace std;
long long cord[1000][2];
long long bridge[1000][1000];
double E;
int island[1000];
int main(int argc, char** argv)
{
	int test_case;
	int T, N, N_temp;
	int i1, i2;
	long long ans, temp;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		ans = 0;
		priority_queue<pair<long long, pair<int, int>>> pq;
		cin >> N;
		for (int i = 0; i < N; i++) cin >> cord[i][0];
		for (int i = 0; i < N; i++) cin >> cord[i][1];
		cin >> E;
		for (int i = 0; i < N; i++) island[i] = i;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < i; j++) {
				pq.push({ -1 * ((cord[i][0] - cord[j][0])*(cord[i][0] - cord[j][0]) + (cord[i][1] - cord[j][1])*(cord[i][1] - cord[j][1])), {i, j}});
			}
		}
		N_temp = N - 1;
		while (N_temp) {
			temp = pq.top().first; i1 = pq.top().second.first; i2 = pq.top().second.second;
			if (island[i1] != island[i2]) {
				ans += -1*temp;
				N_temp--;
				int temp1 = island[i1];
				int temp2 = island[i2];
				for (int i = 0; i < N; i++) {
					if (island[i] == temp1 || island[i] == temp2) {
						island[i] = temp1;
					}
				}
			}
			pq.pop();
		}
		ans = round(double(ans)*E);
		cout << '#' << test_case << ' ' << ans << '\n';
	}
	return 0;
}