#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int cnt[101] = { 0, };
	int FQ[100] = { 0, };
	int here = 0;
	int ans[100] = { 0, };
	int ans_cnt = 0;
	char input[8];
	for (int i = 0; i < N; i++) {
		cin >> input;
		if (input[0] == 'e') {
			cin >> FQ[here];
			cnt[FQ[here]]++;
			here++;
		}
		else {
			int it = 0;
			for (int j = 1; j <= 100; j++) {
				if (it < cnt[j]) {
					it = cnt[j];
				}
			}
			for (int j = 0; j < 100; j++) {
				if (cnt[FQ[j]] == it) {
					ans[ans_cnt] = FQ[j];
					ans_cnt++;
					cnt[FQ[j]]--;
					FQ[j] = 0;
					break;
				}
			}
		}
	}
	for (int i = 0; i < ans_cnt; i++) {
		cout << ans[i];
		if (i != ans_cnt - 1) {
			cout << ' ';
		}
	}
	
	return 0;
}