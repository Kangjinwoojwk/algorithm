#include <iostream>
using namespace std;
int N, M, K, A, B;
int a[10], b[10];
int customert[1001];
int customer[1001][2] = { 0, };
int acustomer[10][2] = { 0, }, bcustomer[10][2] = { 0, };
int a_wait[2001], b_wait[2001];
int a_start, a_end, b_start, b_end, customercnt, endcnt, ans, t;
void sol() {
	while (customercnt != K) {
		for (int i = a_end + 1; i <= K; i++) {
			if (customert[i] > t)
				break;
			if (customert[i] == t)
				a_wait[a_end++] = i;
		}
		for (int i = 1; i <= N; i++) {
			if (acustomer[i][0] == 0 && a_start != a_end) {
				acustomer[i][0] = a[i];
				acustomer[i][1] = a_wait[a_start++];
				customer[acustomer[i][1]][0] = i;
			}
			if (acustomer[i][0])
				acustomer[i][0]--;
			if (acustomer[i][0] == 0 && acustomer[i][1]) {
				b_wait[b_end++] = acustomer[i][1];
				acustomer[i][1] = 0;
			}
		}
		for (int i = 1; i <= M; i++) {
			if (bcustomer[i][0] == 0 && b_start != b_end) {
				bcustomer[i][0] = b[i];
				bcustomer[i][1] = b_wait[b_start++];
				customer[bcustomer[i][1]][1] = i;
			}
			if (bcustomer[i][0])
				bcustomer[i][0]--;
			if (bcustomer[i][0] == 0 && bcustomer[i][1]) {
				customercnt++;
				bcustomer[i][1] = 0;
			}
		}
		t++;
	}
}
int main(void) {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N >> M >> K >> A >> B;
		for (int i = 1; i <= N; i++)
			cin >> a[i];
		for (int i = 1; i <= M; i++)
			cin >> b[i];
		for (int i = 1; i <= K; i++)
			cin >> customert[i];
		customercnt = t = a_start = a_end = b_start = b_end = endcnt = ans = 0;
		sol();
		for (int i = 1; i <= K; i++)
			if (customer[i][0] == A && customer[i][1] == B)
				ans += i;
		if (ans == 0)
			ans = -1;
		cout << '#' << tc << ' ' << ans << '\n';
	}
}