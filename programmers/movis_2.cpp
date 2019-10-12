// 효율성에서 전부 시간초과, 무식하게 시뮬레이션 한 결과
// 라이브러리를 사용하여 정렬, 우선순위 큐를 쓰면 해결 될 것 같으나 현재 익숙하지 않으니 최적화를 할 수 없다.
#include <string>
#include <vector>

using namespace std;

string solution(int n, vector<string> plates, vector<int> odo, int k, vector<int> drives) {
    string answer = "";
    for(int i = 0; i < k;i++){
        int min_odo = 1<<30;
        for(int j = 0; j < n; j++)
            if(odo[j] < min_odo)
                min_odo = odo[j];
        int min_index = 1 << 30;
        for(int j = 0; j < n; j++)
            if(min_odo == odo[j] && (min_index == 1 << 30 || plates[min_index]>plates[j]))
               min_index = j;
        odo[min_index] += drives[i];
    }
    int min_odo = 1<<30;
    for(int j = 0; j < n; j++)
        if(odo[j] < min_odo)
            min_odo = odo[j];
    int min_index = 1 << 30;
    for(int j = 0; j < n; j++)
        if(min_odo == odo[j] && (min_index == 1 << 30 || plates[min_index]>plates[j]))
           min_index = j;
    answer = plates[min_index];
    return answer;
}