#include <iostream>
using namespace std;
int get_v[40][2];
int ans[80];
int n;
void sol(int start, int end) {
	if (end == 2 * n - 1)
		return;
	for (int i = 1; i < n; i++) {
		if (get_v[i][0] != 0) {
			if (get_v[i][0] == ans[end]) {
				ans[end + 1] = get_v[i][0];
				ans[end + 2] = get_v[i][1];
				get_v[i][0] = 0;
				sol(start, end + 2);
				return;
			}
			if (get_v[i][1] == ans[start]) {
				for (int j = end; j >= 0; j--) {
					ans[j + 2] = ans[j];
				}
				ans[start] = get_v[i][0];
				ans[start + 1] = get_v[i][1];
				get_v[i][0] = 0;
				sol(start, end + 2);
				return;
			}
		}
	}
}
int main(void) {
	int T;
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> get_v[i][0] >> get_v[i][1];
		}
		ans[0] = get_v[0][0];
		get_v[0][0] = NULL;
		ans[1] = get_v[0][1];
		sol(0, 1);
		cout << '#' << test_case;
		for (int i = 0; i < 2 * n; i++) {
			cout <<' '<< ans[i];
		}
		cout << '\n';
	}
	return 0;
}