def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 1
    camera_loc = routes[0][1]
    for start, end in routes:
        if start <= camera_loc <= end:
            pass
        else:
            camera_loc = end
            answer += 1
    return answer

print(solution(
    [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
))