def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) >= len(phone_book[j]):
                if phone_book[i] == phone_book[j]:
                    return False
                break
            if phone_book[j].startswith(phone_book[i]):
                return False
            # for k in range(len(phone_book[i])):
            #     if phone_book[i][k] != phone_book[j][k]:
            #         break
            # else:
            #     return False
    return True

print(solution(["119", "97674223", "1195524421"]))