# 迪捷科思特拉算法

infinity = float("inf")  # python 中 正无穷

# 示例 1.
# graph = {}  # 图的初始化
# graph["start"] = {}
# graph["start"]["a"] = 6  # start ---> a  权重为 6
# graph["start"]["b"] = 2   # start ---> b  权重为 2


# graph["a"] = {}
# graph["a"]["fin"] = 1
# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5
# graph["fin"] = {}


# # 创建开销表
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity


# # 创建父节点的散列表
# parents = {}
# parents["a"] = "start"  # a 节点的父节点是 start
# parents["b"] = "start"  # b 节点的父节点是 start
# parents["fin"] = None  # fin(终点) 节点的父节点是 None


# # 创建存储遍历过节点的数组
processed = []

# 示例 2
graph = {}

graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["fin"] = 3
graph["c"]["d"] = 6

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

parents = {}
parents["a"] = "start"  # a 节点的父节点是 start
parents["b"] = "start"  # b 节点的父节点是 start
parents["c"] = None # a 节点的父节点是 start
parents["d"] = None  # b 节点的父节点是 start
parents["fin"] = None  # fin(终点) 节点的父节点是 None



def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # 在未处理的节点中找到开销最小的节点
while node is not None:  # 当前节点不是终点
    cost = costs[node]  # 获取需要被验证节点的开销值
    neighbors = graph[node]  # 获取待验证节点的邻居
    for n in neighbors.keys():  # 遍历待验证节点的邻居
        new_cost = cost + neighbors[n]  # 算出每个当前节点开销值 + 当前节点到当前邻居的开销值
        if costs[n] > new_cost:  # 判断经由节点比直接到节点的耗费少
            costs[n] = new_cost  # 更新到指定节点为最小耗费
            parents[n] = node  # 将到指定节点的父节点更新为经过的节点
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)

