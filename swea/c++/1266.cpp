#include<iostream>
using namespace std;
float list[101];
int C[20][20];
int prime[8] = { 2, 3, 5, 7, 11, 13, 17, 19 };
void Make_C() {
	for (int i = 1; i < 19; ++i) {
		C[i][0] = 1;
		C[i][i] = 1;
	}
	for(int i = 2; i < 19; ++i) {
		for (int j = 1; j <= i; ++j) {
			C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
		}
	}
}
int main(int argc, char** argv)
{
	int test_case;
	int T, skillOfMasterA, skillOfMasterB;
	Make_C();
	for (int i = 0; i <= 100; ++i) {
		list[i] = 0.0;
		float temp;
		for (int j = 0; j < 8; ++j) {
			temp = 1.0;
			for (int k = 0; k < prime[j]; ++k) {
				temp *= ((float)i/100);
			}
			for (int k = 0; k < 18 - prime[j]; ++k) {
				temp *= (1.0 - ((float)i / 100));
			}
			temp *= (float)C[18][prime[j]];
			list[i] += temp;
		}
	}
	float ans;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &skillOfMasterA, &skillOfMasterB);
		ans = list[skillOfMasterA]+list[skillOfMasterB] - (list[skillOfMasterA] * list[skillOfMasterB]);
		printf("#%d %f\n", test_case, ans);
	}
	return 0;
}