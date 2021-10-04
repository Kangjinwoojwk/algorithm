import requests #pip install requests
import json
x_auth_token = ''
BASE_URL = ''
header = {'X-Auth-Token': x_auth_token, 'Content-Type': 'application/json', }
data = {'problem': 2, }#문제 설정

request = requests.post(BASE_URL+'/start', headers=header, params=data)#시작
response = json.loads(request.content)
auth_key, problem_no, time = response['auth_key'], response['problem'], response['time']
headers = {'Authorization': auth_key, 'Content-Type': 'application/json', }
match_data = {'pairs': list(),} # 매칭 시 pairs에 길이 2인 array append
grade_data = {'commands': list(), } # 변경 시 list에 dict로 id: grade: 추가 append
waiting_line, game_result, user_info, status, score = list(), list(), list(), 'ready', dict() # 데이터 받을 변수 미리 선언
request = requests.put(BASE_URL+'/match', headers=headers, data=json.dumps(match_data)) # 시작시 1부터
status, time = json.loads(request.content)['status'], json.loads(request.content)['time']
while time <= 595:
    match_data = {'pairs': list(), }
    grade_data = {'commands': list(), }
    if status == 'finished':
        break
    request = requests.get(BASE_URL + '/waiting_line', headers=headers)
    waiting_line = json.loads(request.content)['waiting_line']

    request = requests.get(BASE_URL + '/user_info', headers=headers)
    user_info = json.loads(request.content)['user_info']

    user_infos = {i['id']: i['grade'] for i in user_info} # grade 찾기 쉽게 변형
    waiting_user = [[[abs(user_infos[i['id']] - user_infos[j['id']]), i['from']+j['from']] if i != j else 99999999999 for i in waiting_line] for j in waiting_line]
    waiting_visit = [True] * len(waiting_line)
    for i in range(len(waiting_line)): # 매칭 만들기
        for j in range(len(waiting_line)):
            if i != j and waiting_visit[i] and waiting_visit[j] and waiting_user[i][j][0] < 3 * waiting_user[i][j][1]:
                match_data['pairs'].append([waiting_line[i]['id'], waiting_line[j]['id']]) #1 # 5,11,6,232.60 #3 6 3 222.9913 #3 11 5 227.257 #3 11 6 224.5903
                waiting_visit[i], waiting_visit[j] = False, False#2 #5, 11, 6, 204 #3 6 3 194 #3 9 6 204

    #for i in range(len(waiting_line)//2):
    #    match_data['pairs'].append([waiting_line[2*i]['id'], waiting_line[2*i+1]['id']]) #59.333	48.716	99.9	209.58 57.798	54.147	99.877	214.24
    request = requests.get(BASE_URL+'/game_result', headers=headers)
    game_result = json.loads(request.content)['game_result']
    for i in game_result:
        for j in user_info:
            if i['win'] == j['id']:
                grade_data['commands'].append({'id':i['win'], 'grade':j['grade'] + (21 * (50 - i['taken']))})
            if i['lose'] == j['id']:
                grade_data['commands'].append({'id':i['lose'], 'grade':j['grade'] - (6*(40 - i['taken']))})
                if grade_data['commands'][-1]['grade'] < 0:
                    grade_data['commands'][-1]['grade'] = 0
    request = requests.put(BASE_URL + '/change_grade', headers=headers, data=json.dumps(grade_data))

    request = requests.put(BASE_URL + '/match', headers=headers, data=json.dumps(match_data))
    status, time = json.loads(request.content)['status'], json.loads(request.content)['time']
    print(time)

request = requests.get(BASE_URL+'/score', headers=headers)
score = json.loads(request.content)
print(score)