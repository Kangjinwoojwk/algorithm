#include<iostream>
#include<string>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T, N;
	T = 10;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N;
		string find_str, str;
		int ans = 0;
		cin >> find_str >> str;
		int here = 0;
		while (here != string::npos) {
			if (here != 0) {
				here++;
			}
			here = str.find(find_str, here);
			ans++;
		}
		cout << '#' << N <<' '<< ans<<'\n';
	}
	return 0;
}