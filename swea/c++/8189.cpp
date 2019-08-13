#include <iostream>
using namespace std;
int T, N, A, B, t_check, letter_check;
int t[100], ans[100], letter[100];
int main(int argc, char** argv)
{
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N >> A >> B;
		for (int i = 0; i < N; i++) {
			cin >> t[i];
		}
		ans[N - 1] = t_check = letter_check = 0;
		for (int time = 1; time < 2001; time++) {
			if (t[t_check] == time) {
				letter[letter_check] = t[t_check];
				letter_check++;
				t_check++;
			}
			if (letter_check == A) {
				for (int i = t_check - letter_check; i < (t_check - (A / 2)); i++) {
					ans[i] = time;
				}
				int temp = letter_check;
				for (int i = 0; i < temp - (A / 2); i++) {
					letter[i] = letter[i + ((A + 1) / 2)];
					letter_check--;
				}
			}
			if ((time - letter[0]) == B) {
				for (int i = t_check - letter_check; i < (t_check - (letter_check / 2)); i++) {
					ans[i] = time;
				}
				int temp = letter_check;
				for (int i = 0; i < temp - (temp / 2); i++) {
					letter[i] = letter[i + ((temp + 1) / 2)];
					letter_check--;
				}
			}
			if (ans[N - 1] != 0) {
				break;
			}
		}
		cout << '#' << tc;
		for (int i = 0; i < N; i++) {
			cout <<' '<< ans[i];
		}
	}
}