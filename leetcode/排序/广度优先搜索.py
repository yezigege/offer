
graph = {}  # 图的基本结构

def person_is_need(person):
    # 判断逻辑

    # ...
    return name[-1] == 'm'  # person的name结尾为 'm' 的符合条件


def search(name):
    search_queue = deque()  # 存储待检查数据
    search_queue += graph[name]
    searched = []  # 存储检查过的数据
    while search_queue:  # 只要存储数据还有，就一直检查
        person = search_queue.popleft()  # 从待检查区取出一个检查
        if person not in searched:  # 查看此数据是否被检查过
            if person_is_need(person):  # 判断这个人是否是需要的
                return person
                print("yes, we need this guy!")
                break
            else:  # 不是要查到的那个人
                search_queue += graph[person]  # 将已查询的子节点加入到待查询数据中
                searched.append(person)  # 标记已经检查过的数据
