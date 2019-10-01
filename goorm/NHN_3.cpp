#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	bool** follow = new bool*[N];
	for (int i = 0; i < N; i++) {
		follow[i] = new bool[N];
	}
	int* candy = new int[N];
	for (int i = 0; i < N; i++) {
		candy[i] = 0;
	}
	char card;
	int follower;
	int turn = 0;
	char g;
	scanf_s("%c", &g);
	while (1) {
		scanf_s("%c", &card);
		if (card == ' ')
			continue;
		else if (card == 'K') {
			scanf_s("%c", &card);
			scanf_s("%d", &follower);
			follow[turn][follower] = true;
		}
		else if (card == 'Q') {
			for (int i = 0; i < N; i++) {
				candy[i]++;
			}
		}
		else if (card == 'A') {
			int temp = turn;
			candy[temp]++;
			bool* visit = new bool[N];
			for (int i = 0; i < N; i++)
				visit[i] = true;
			int* st = new int[N];
			int st_point = 0;
			int start = -1;
			while (start != st_point) {
				if (start != -1) {
					temp = st[start];
				}
				for (int i = 0; i < N; i++) {
					if (follow[temp][i] == true && visit[i] == true) {
						visit[i] = false;
						st[st_point++] = i;
						candy[i]++;
					}
				}
				start++;
			}
		}
		else if (card == 'J') {
			bool* visit = new bool[N];
			for (int i = 0; i < N; i++)
				visit[i] = true;
			int* st = new int[N];
			int st_point = 0;
			int start = -1;
			int temp = (turn - 1 + N) % N;
			candy[temp]++;
			while (start != st_point) {
				if (start != -1) {
					temp = st[start];
				}
				for (int i = 0; i < N; i++) {
					if (follow[temp][i] == true && visit[i] == true) {
						visit[i] = false;
						st[st_point++] = i;
						candy[i]++;
					}
				}
				start++;
			}
			temp = (turn + 1) % N;
			candy[temp]++;
			int temp_start = -1;
			if (start != -1) {
				temp_start = --start;
			}
			while (start != st_point) {
				if (start != temp_start) {
					temp = st[start];
				}
				for (int i = 0; i < N; i++) {
					if (follow[temp][i] == true && visit[i] == true) {
						visit[i] = false;
						st[st_point++] = i;
						candy[i]++;
					}
				}
				start++;
			}
		}
		else if (card == '\n')
			break;
		turn = (turn + 1) % N;
	}
	for (int i = 0; i < N; i++) {
		cout << candy[i];
		if (i != N - 1) {
			cout << ' ';
		}
	}
	return 0;
}