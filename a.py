pre_order = []
while 1:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행
    except:
        break

print(pre_order)