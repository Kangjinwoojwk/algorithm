#include <iostream>
using namespace std;
int N, M, K, A, B;//����, ����, ����, ã�� ��ȣ ���� ��
int a[10], b[10];//����, ���� �� �ð� ������ Ȯ���� ���� Ȯ��
int customert[1001];//���� ���� �ð�
int customer[1001][2] = { 0, };//����, ���� ��� �޾Ҵ��� ����� ����
int acustomer[10][2] = { 0, }, bcustomer[10][2] = { 0, };//����, ��� �ð� ���� ����
int a_wait[2001], b_wait[2001];//����, ���� ��⿭ ����
int a_start, a_end, b_start, b_end, customercnt, ans, t;// ����� ������, ���� ��� ����, ����������, ���� ��ģ �����, ��, �ð�
void sol() {// �ùķ��̼� �Լ�
	while (customercnt != K) {//��� ����� ���� ������ ��
		for (int i = a_end + 1; i <= K; i++) {//�ð��� �Ǹ� ���� ��⿭�� �ִ´�.
			if (customert[i] > t)
				break;
			if (customert[i] == t)
				a_wait[a_end++] = i;
		}
		for (int i = 1; i <= N; i++) {
			if (acustomer[i][0] == 0 && a_start != a_end) {//������ ��������� �ִ´�.
				acustomer[i][0] = a[i];
				acustomer[i][1] = a_wait[a_start++];
				customer[acustomer[i][1]][0] = i;
			}
			if (acustomer[i][0])//���� ���̸� �ð� ����
				acustomer[i][0]--;
			if (acustomer[i][0] == 0 && acustomer[i][1]) {//������ ������ ������
				b_wait[b_end++] = acustomer[i][1];
				acustomer[i][1] = 0;
			}
		}
		for (int i = 1; i <= M; i++) {
			if (bcustomer[i][0] == 0 && b_start != b_end) {//���� ��������� �ִ´�.
				bcustomer[i][0] = b[i];
				bcustomer[i][1] = b_wait[b_start++];
				customer[bcustomer[i][1]][1] = i;
			}
			if (bcustomer[i][0])//���� ���̸� �ð� ����
				bcustomer[i][0]--;
			if (bcustomer[i][0] == 0 && bcustomer[i][1]) {//���� ������ ���� ����� �־��ش�.
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
	for (int tc = 1; tc <= T; tc++) {//�����͸� �޾� �ʱ�ȭ�Ѵ�.
		cin >> N >> M >> K >> A >> B;
		for (int i = 1; i <= N; i++)
			cin >> a[i];
		for (int i = 1; i <= M; i++)
			cin >> b[i];
		for (int i = 1; i <= K; i++)
			cin >> customert[i];
		customercnt = t = a_start = a_end = b_start = b_end = ans = 0;
		sol();
		for (int i = 1; i <= K; i++)//���ǿ� �´°��� ��ȣ�� ���Ѵ�.
			if (customer[i][0] == A && customer[i][1] == B)
				ans += i;
		if (ans == 0)//���ǿ� �´� ��ȣ�� ���� ��� -1
			ans = -1;
		cout << '#' << tc << ' ' << ans << '\n';
	}
}