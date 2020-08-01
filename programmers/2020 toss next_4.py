SELECT (SELECT NAME FROM BANKS WHERE ID = SEND_BANK_ID), SUM(TRANSFER_AMOUNT)
  FROM TOSS_TRANSFER
 WHERE TRANSFER_DATE BETWEEN '2020-07-01' AND '2020-07-02'
   AND SEND_USER_ID in(
						SELECT USER_ID
							FROM USER_SEGMENT
						 WHERE USER_ID in (SELECT USER_ID
																	FROM USER_SEGMENT
																 WHERE SEGMENT_ID = (SELECT ID FROM SEGMENTS WHERE NAME = '20대'))
							 AND USER_ID in (SELECT USER_ID
																	FROM USER_SEGMENT
																 WHERE SEGMENT_ID = (SELECT ID FROM SEGMENTS WHERE NAME = 'IOS')))
 GROUP BY SEND_BANK_ID
 ORDER BY SUM(TRANSFER_AMOUNT) DESC;





# 토스 데이터 엔지니어 김토스는 어떤 특성을 가진 유저들에 대한
# 송금액을 분석해보고자 합니다.
#
#
#
# '20대 이면서, IOS' 인 유저들의 '2020년 7월 1일'에 송금﻿한 은행별 송금액의 합을 출력하십시오.
#
#
#
# - 송금액의 합 내림차순으로 정렬합니다.
#
#
#
# 테이블 구조
#
#
#
# USERS
#
# ID	NAME
# (사용자 이름)
# INT
# VARCHAR(20)
# SEGMENTS
#
# ID	NAME
# INT	VARCHAR(20)
# USER_SEGMENT
#
# ID	USER_ID (USERS.ID)	SEGMENT_ID (SEGMENTS.ID)
# INT
# INT
# INT
#
# BANKS
#
# ID	NAME
# (은행 이름)
# INT
# VARCHAR(20)
#
# TOSS_TRANSFER
#
# ID	SEND_USER_ID (USERS.ID)	SEND_BANK_ID (BANKS.ID)	RECEIVE_USER_ID (USERS.ID)	RECEIVE_BANK_ID (BANKS.ID)
# TRANSFER_AMOUNT
# (송금액)
#
# TRANSFER_DATE
# (송금 날짜)
# INT
# INT
# INT
# INT	INT	INT	DATETIME
#
# 쿼리 실행결과를 통해 테이블 내용을 직접 확인해볼 수 있습니다.
#
#
#
# 출력 설명
# 은행 이름,  송금액 합
#
#
# 출력 예시 (RAW)
# 토스뱅크     37000
#
# 비바은행      23000
#
# 역삼은행      17000