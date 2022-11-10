#include<iostream>
#include<queue>
using namespace std;
char board_cnt[1000][1000];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };
int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int test_case;
	int T, N, M;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N >> M;
		int ans = 0;
		char temp;
		queue < pair<int, int>> q;
		for (register int i = 0; i < N; ++i) {
			for (register int j = 0; j < M; ++j) {
				cin >> temp;
				if (temp == 'W') {
					board_cnt[i][j] = 0;
					q.push({ i,j });
				}
				else {
					board_cnt[i][j] = -1;
				}
			}
		}
		register int tempi, tempj, tempx, tempy;
		while (!q.empty()) {
			tempi = q.front().first;
			tempj = q.front().second;
			q.pop();
			for (int i = 0; i < 4; ++i) {
				tempx = tempi + dx[i];
				tempy = tempj + dy[i];
				if (0 <= tempx && tempx < N && 0 <= tempy && tempy < M&&board_cnt[tempx][tempy] == -1) {
					board_cnt[tempx][tempy] = board_cnt[tempi][tempj] + 1;
					q.push({ tempx, tempy });
				}
			}
		}
		for (register int i = 0; i < N; ++i)
			for (register int j = 0; j < M; ++j) ans += board_cnt[i][j];
		cout << '#' << test_case << ' ' << ans << '\n';
	}
	return 0;
}