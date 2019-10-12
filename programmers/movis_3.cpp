//2, 3테스트 세그멘테이션 폴트
//N을 넘어가서 잡는지 N - 1로 하면 없어진다. 그러나 그러면 다른게 틀린다.
//효율성은 1개만 맞는다
#include <string>
#include <vector>

using namespace std;

int solution(vector<string> board) {
    int dx[4] = {1, 1, -1, -1};
    int dy[4] = {1, -1, 1, -1};
    int answer = 0;
    int N = board[0].length();
    for(int i=0; i<N;i++){
        for(int j=0;j<N;j++){
            int lengthi = 0;
            bool stopcheck = false;
            for(int k = 0; k < N; k++){
                for(int l = 0; l <4;l++){
                    if(i + k * dx[l] < 0 || i + k * dx[l] >= N || j + k * dy[l] < 0 || j + k * dy[l] >= N){
                        stopcheck = true;
                        break;
                    }
                    if(board[i + k * dx[l]][j + k * dy[l]] != board[i][j]){
                        stopcheck = true;
                        break;
                    }
                }
                if(stopcheck)
                    break;
                lengthi++;
            }
            if(lengthi)
                if(lengthi * 2 + 1> answer)
                    answer = lengthi*2 + 1;
        }
    }
    return answer;
}