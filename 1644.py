import sys

input = sys.stdin.readline

x = int(input())
def make_prime_list():
    def off_palette(start):
        now = start * 2
        while now < len(palette):
            palette[now] = False
            now += start

    palette = [True] * (x+1)
    for i in range(2, len(palette)):
        if palette[i]:
            off_palette(i)
    return [i  for i in range(2, x+1) if palette[i]]

prime_list = make_prime_list()
# answer = 0

# left = right = 0
# s = 0
# while left < len(prime_list) and right < len(prime_list):
#     if s == x:
#         answer += 1
#         s -= prime_list[left]
#         left += 1
#     elif s < x:
#         s += prime_list[right]
#         right += 1
#     else:
#         s -= prime_list[left]
#         left += 1

# print(answer)
left, answer, acc = 0, 0, 0
lst = prime_list
for i in range(len(lst)):
    acc += lst[i]
    if acc == x:
        answer += 1
    elif acc > x:
        while acc > x:
            acc -= lst[left]
            left += 1
        if acc == x:
            answer += 1

print(answer)