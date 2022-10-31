#include<iostream>
#include<algorithm>
using namespace std;

int building_height[1000];
int main(int argc, char** argv)
{
	int test_case;
	int T = 10;
	//freopen("input.txt", "r", stdin);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		int ans = 0;
		int building_count;
		cin >> building_count;
		for (int i = 0; i < building_count; i++) {
			cin >> building_height[i];
		}
		for (int i = 0; i < building_count; i++) {
			for (int j = 2; j < building_count - 2; j++) {
				int temp = std::max(std::max(building_height[j - 2], building_height[j - 1]), std::max(building_height[j + 2], building_height[j + 1]));
				if (building_height[j] - temp > 0) {
					ans += building_height[j] - temp;
				}
			}
		}
		cout << "#" << test_case << " " << ans << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}