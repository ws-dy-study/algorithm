import sys
# sys.stdin = open('22252.txt', 'r')
import heapq

n, m = map(int, input().split())
sy,sx,ey,ex = map(int, input().split())

miro = []
for _ in range(n):
    row = list(map(int, input().split()))
    miro.append(row)

INF = float('inf')
array = [[[INF] * 3 for _ in range(m)] for _ in range(n)]

heap = []
heapq.heappush(heap, [0, sy-1, sx-1, 0])
zero_dy = [0,0,-1,1] # 좌,우,상,하
zero_dx = [-1,1,0,0]
one_dy = [-1,1] # 상,하
one_dx = [0,0]
two_dy = [0,0]
two_dx = [-1,1] # 좌,우

while heap:

    damage , y, x , moveCnt = heapq.heappop(heap)

    if array[y][x][moveCnt] < damage:
        continue

    newMoveCnt = (moveCnt + 1) % 3

    loopCount = 4
    dy = zero_dy
    dx = zero_dx

    if newMoveCnt == 1:
        loopCount = 2
        dy = one_dy
        dx = one_dx
    elif newMoveCnt == 2:
        loopCount = 2
        dy = two_dy
        dx = two_dx

    for k in range(loopCount):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<= ny <n and 0<= nx <m:
            if miro[ny][nx] != -1:
                newDamage = damage + miro[ny][nx]
                if newDamage < array[ny][nx][newMoveCnt]:
                    array[ny][nx][newMoveCnt] = newDamage
                    heapq.heappush(heap, [newDamage, ny, nx, newMoveCnt])

ANSWER = min(array[ey-1][ex-1])

if ANSWER == INF:
    print(-1)
else:
    print(ANSWER)