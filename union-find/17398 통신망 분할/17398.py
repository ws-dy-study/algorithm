import sys
# sys.stdin = open('17398.txt','r')
sys.setrecursionlimit(123456)

nodeCnt, edgeCnt, divideCnt = map(int, input().split())
edgeList = [[0,0]]
divideEdgeConfirm = [False] * (edgeCnt + 1)
divideEdgeList = []

for i in range(edgeCnt):
    node1, node2 = map(int, sys.stdin.readline().split())
    edgeList.append([node1, node2])

for i in range(divideCnt):
    egdeNumber = int(sys.stdin.readline())
    divideEdgeConfirm[egdeNumber] = True
    divideEdgeList.append(egdeNumber)

parents = [i for i in range(nodeCnt + 1)]
size = [1 for i in range(nodeCnt + 1)]
answer = 0

def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(nodeA, nodeB, state):
    global answer,size

    rootA = find(nodeA)
    rootB = find(nodeB)

    # 둘이 부모가 다른 경우
    if rootA != rootB:
        if state == 1:
            answer += size[min(rootA,rootB)] * size[max(rootA,rootB)]
        parents[max(rootA,rootB)] = min(rootA,rootB)
        size[min(rootA,rootB)] += size[max(rootA,rootB)]
        size[max(rootA,rootB)] = 0
        
    return

for edgeNumber in range(1, edgeCnt+1):
    if divideEdgeConfirm[edgeNumber] == False:
        divideEdgeConfirm[edgeNumber] = True
        nodeA, nodeB = edgeList[edgeNumber]
        union(nodeA, nodeB, 0)

for edgeNumber in divideEdgeList:
    nodeA , nodeB = edgeList[edgeNumber]
    union(nodeA, nodeB, 1)

print(answer)
# print(parents)
# print(size)