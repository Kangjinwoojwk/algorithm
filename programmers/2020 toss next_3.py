# 하나가 안맞네...
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
answer = True
li_st , li_qu = list(), list()
for i in user_input:
	if not answer:
		break
	if i == '-':
		li_st.append(li_st[-1])
	elif i == '+':
		li_qu.append('+')
	else:
		if i in ['(','{','[']:
			li_st.append(i)
			continue
		while li_qu:
			if li_st and ((li_st[-1] == '(' and i ==')') or (li_st[-1] == '{' and i =='}') or (li_st[-1] == '[' and i ==']')):
				li_st.pop()
				li_qu.pop()
			else:
				answer = False
				break
		if answer and li_st and ((li_st[-1] == '(' and i ==')') or (li_st[-1] == '{' and i =='}') or (li_st[-1] == '[' and i ==']')):
				li_st.pop()
		else:
			answer = False
if li_st:
	answer = False
print(answer)





# [DE-2] 괄호 짝 맞추기제출완료
# 10초
# 대괄호 [ ], 중괄호 { }, 소괄호 ( )가 짝이 맞게 적절히 배치되어 있는지를 판별하는 프로그램을 작성하십시오.
#
# 각 괄호의 우선순위는 상관하지 않습니다. 예를 들어, {[]} 와 같이 중괄호 안에 대괄호가 들어있어도 적절히 배치되어 있는 것으로 판별합니다.
#
#
#
# 괄호 외에도 -,+ 문자가 존재 할 수 있으며,
#
# - 가 입력될 경우, 왼쪽으로 가장 가까운 괄호와 동일하게 취급합니다. (입력의 가장 왼쪽에는 -가 입력되지 않습니다.)
#
# + 가 입력될 경우, 오른쪽으로 가장 가까운 괄호와 동일하게 취급합니다. (입력의 가장 오른쪽에는 -가 입력되지 않습니다.)
#
#
#
# ex. [(-))] , ((-++) , {{-(-+)}+}는 짝이 맞게 배치되어 있다고 판별합니다.
#
#
#
# 입력 설명
#
# 임의의 괄호와 +,- 배치
# 출력 설명
#
# 짝이 맞는 적절한 배치의 경우 True 출력, 그렇지 않을 경우 False 출력
#
#
# 입/출력 예시
# :
# 공백
# :
# 줄바꿈
# :
# 탭
# 예시 1
# 입력
# ()((({}})({}[]]
# 출력
# False
# 예시 2
# 입력
# (()){[]}
# 출력
# True
# 예시 3
# 입력
# ((((--+++))){[]}
# 출력
# True
# ⋇ 입출력 형식을 잘 지켜주세요