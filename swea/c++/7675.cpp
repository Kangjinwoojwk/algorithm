#include<iostream>
#include<string>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T, N, cnt;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N;
		string str;
		cout << '#' << test_case<<' ';
		for (int i = 0; i < N; i++) {
			int cnt = 0;
			do {
				cin >> str;
				if (str[0] >= 'A'&&str[0] <= 'Z') {
					bool chk = true;
					if (str[str.size() - 1] == '!' || str[str.size() - 1] == '?' || str[str.size() - 1] == '.') {
						if (str.size() == 2)cnt++;
						else {
							for (int j = 1; j < str.size() - 1; j++) {
								if (str[j] >= 'a'&&str[j] <= 'z')continue;
								chk = false;
								break;
							}
						}
					}
					else {
						for (int j = 1; j < str.size(); j++) {
							if (str[j] >= 'a'&&str[j] <= 'z')continue;
							chk = false;
							break;
						}
					}
					if (chk)cnt++;
				}
			} while (str[str.size() - 1] != '!'&&str[str.size() - 1] != '?'&&str[str.size() - 1] != '.');
			cout << cnt << ' ';
		}
		cout << '\n';
	}
	return 0;
}