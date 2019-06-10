#include <iostream>
using namespace std;
int N, M, K, A, B;//접수, 정비, 고객수, 찾을 번호 넣을 곳
int a[10], b[10];//접수, 정비가 각 시간 얼마인지 확인할 공간 확보
int customert[1001];//고객이 들어온 시간
int customer[1001][2] = { 0, };//접수, 정비 어디서 받았는지 기록할 공간
int acustomer[10][2] = { 0, }, bcustomer[10][2] = { 0, };//접수, 대기 시간 저장 공간
int a_wait[2001], b_wait[2001];//접수, 정비 대기열 생성
int a_start, a_end, b_start, b_end, customercnt, ans, t;// 써먹을 변수들, 접수 대기 인자, 정비대기인자, 정비 마친 사람수, 답, 시간
void sol() {// 시뮬레이션 함수
	while (customercnt != K) {//모든 사람이 정비를 받으면 끝
		for (int i = a_end + 1; i <= K; i++) {//시간이 되면 접수 대기열에 넣는다.
			if (customert[i] > t)
				break;
			if (customert[i] == t)
				a_wait[a_end++] = i;
		}
		for (int i = 1; i <= N; i++) {
			if (acustomer[i][0] == 0 && a_start != a_end) {//접수가 비어있으면 넣는다.
				acustomer[i][0] = a[i];
				acustomer[i][1] = a_wait[a_start++];
				customer[acustomer[i][1]][0] = i;
			}
			if (acustomer[i][0])//접수 중이면 시간 줄임
				acustomer[i][0]--;
			if (acustomer[i][0] == 0 && acustomer[i][1]) {//접수가 끝나면 정비대기
				b_wait[b_end++] = acustomer[i][1];
				acustomer[i][1] = 0;
			}
		}
		for (int i = 1; i <= M; i++) {
			if (bcustomer[i][0] == 0 && b_start != b_end) {//정비가 비어있으면 넣는다.
				bcustomer[i][0] = b[i];
				bcustomer[i][1] = b_wait[b_start++];
				customer[bcustomer[i][1]][1] = i;
			}
			if (bcustomer[i][0])//정비 중이면 시간 줄임
				bcustomer[i][0]--;
			if (bcustomer[i][0] == 0 && bcustomer[i][1]) {//정비가 끝나면 끝난 사람을 넣어준다.
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
	for (int tc = 1; tc <= T; tc++) {//데이터를 받아 초기화한다.
		cin >> N >> M >> K >> A >> B;
		for (int i = 1; i <= N; i++)
			cin >> a[i];
		for (int i = 1; i <= M; i++)
			cin >> b[i];
		for (int i = 1; i <= K; i++)
			cin >> customert[i];
		customercnt = t = a_start = a_end = b_start = b_end = ans = 0;
		sol();
		for (int i = 1; i <= K; i++)//조건에 맞는고객의 번호를 더한다.
			if (customer[i][0] == A && customer[i][1] == B)
				ans += i;
		if (ans == 0)//조건에 맞는 번호가 없을 경우 -1
			ans = -1;
		cout << '#' << tc << ' ' << ans << '\n';
	}
}