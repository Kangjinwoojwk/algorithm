#include<iostream>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T, n, m;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> n >> m;
		int ans = 0;
		int* R = new int[n];
		int* W = new int[m];
		int* wait = new int[m] { -1, };
		int* park = new int[n] { -1, };
		for (int i = 0; i < m; i++)wait[i] = -1;
		for (int i = 0; i < n; i++)park[i] = -1;
		int wait_front = 0;
		int wait_rear = 0;
		for (int i = 0; i < n; i++)cin >> R[i];
		for (int i = 0; i < m; i++)cin >> W[i];
		int l = 2 * m;
		int temp;
		for (int i = 0; i < l; i++) {
			cin >> temp;
			if (temp > 0) {
				temp--;
				bool chk = true;
				for (int j = 0; j < n; j++) {
					if (park[j] == -1) {
						ans += R[j] * W[temp];
						park[j] = temp;
						chk = false;
						break;
					}
				}
				if (chk) {
					wait[wait_front] = temp;
					wait_front++;
				}
			}
			else {
				temp++;
				temp = -1 * temp;
				for (int j = 0; j < n; j++) {
					if (park[j] == temp) {
						park[j] = -1;
						if (wait_front != wait_rear) {
							ans += R[j] * W[wait[wait_rear]];
							park[j] = wait[wait_rear];
							wait_rear++;
						}
						break;
					}
				}
			}
		}

		cout << '#' << test_case << ' ' << ans << '\n';
		delete R, W, wait;
	}
	return 0;
}