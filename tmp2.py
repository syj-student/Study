from collections import defaultdict

class Trie():
    def __init__(self, char=None):
        self.len_counter = defaultdict(int)
        self.chars = defaultdict(Trie)
        self.end = False
    
    def insert(self, word):
        now = self
        for c in word:
            now.len_counter[len(word)] += 1
            now = now.chars[c]
        now.end = True

    def search(self, word):
        now = self
        for c in word:
            if c == '?':
                return now.len_counter.get(len(word), 0)
            exist = now.chars.get(c)
            if exist:
                now = exist
            else:
                return 0
        return True
    
# # -- 코드를 입력하세요
# SELECT
#     CAR_ID, CAR_TYPE,
#     CASE
#         WHEN CAR_TYPE = '세단'
#         THEN
#             CASE
#                 WHEN RENT_DAYS >= 90
#                 THEN ROUND(DAILY_FEE * RENT_DAYS * 0.85)
#                 WHEN RENT_DAYS >= 30
#                 THEN ROUND(DAILY_FEE * RENT_DAYS * 0.90)
#                 WHEN RENT_DAYS >= 7
#                 THEN ROUND(DAILY_FEE * RENT_DAYS * 0.95)
#                 ELSE ROUND(DAILY_FEE * RENT_DAYS)
#             END
#         WHEN CAR_TYPE = 'SUV'
#         THEN
#             CASE
#                 WHEN RENT_DAYS >= 90
#                 THEN ROUND(DAILY_FEE * RENT_DAYS * 0.88)
#                 WHEN RENT_DAYS >= 30
#                 THEN ROUND(DAILY_FEE * RENT_DAYS * 0.92)
#                 WHEN RENT_DAYS >= 7
#                 THEN ROUND(DAILY_FEE * RENT_DAYS * 0.97)
#                 ELSE ROUND(DAILY_FEE * RENT_DAYS)
#             END
#     END FEE
# FROM (
#     SELECT CAR.CAR_ID, CAR_TYPE, DAILY_FEE, (HISTORY.END_DATE - HISTORY.START_DATE + 1) RENT_DAYS
#     FROM CAR_RENTAL_COMPANY_CAR AS CAR
#     JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS HISTORY
#     ON  CAR.CAR_ID = HISTORY.CAR_ID
#     WHERE CAR_TYPE = '세단' OR 
#         CAR_TYPE = 'SUV' AND 
#         HISTORY.END_DATE - HISTORY.START_DATE + 1 >= 7 AND
#         YEAR(HISTORY.START_DATE) = 2022 AND MONTH(HISTORY.START_DATE) = 11
# ) AS A
# WHERE A.FEE >= 500000 AND A.FEE < 2000000
# ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC



def solution(words, queries):
    trie = Trie()
    rev_trie = Trie()

    for word in words:
        rev_trie.insert(reversed(word))
        trie.insert(word)
            
    answer = []
    for q in queries:
        if q[0] == '?':
            n = rev_trie.search(reversed(q))
        else:
            n = trie.search(q)
        answer.append(n)
    
    return answer

####
print(solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"]
))