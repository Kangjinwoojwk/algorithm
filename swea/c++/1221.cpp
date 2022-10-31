#include<iostream>
#include<algorithm>
using namespace std;

char number[10][4] = { "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN" };
int num_cnt[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		char tr;
		int tr1;
		cin >> tr >> tr1;
		int num_all;
		cin >> num_all;
		char temp[3];
		for (int i = 0; i < num_all; i++) {
			cin >> temp[0] >> temp[1] >> temp[2];
			for (int j = 0; j < 10; j++) {
				if (number[j][0] == temp[0] && number[j][1] == temp[1] && number[j][2] == temp[2]) {
					num_cnt[j]++;
					break;
				}
			}
		}

		cout << "#" << test_case << "\n";
		for (int i = 0; i < 10; i++) {
			while (num_cnt[i]) {
				cout << number[i] << " ";
				num_cnt[i]--;
			}
		}
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}