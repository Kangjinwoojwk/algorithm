#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> P) {
    int answer = 0;
    int minP = 10000000;
    for(int i = 0; i < n; i++){
        if(P[i] < minP)
            minP = P[i];
        else
            P[i] = minP;
    }
    for(int i = 0; i < n; i++)
        answer += P[i];
    return answer;
}