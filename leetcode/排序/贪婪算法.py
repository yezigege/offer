
# 州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# 广播台清单
# 键是广播台名称，值是该广播台能覆盖的州
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 存储最终要选择的广播台
final_stations = set()


while states_needed:
    # 每次选择的最优广播台
    best_station = None
    states_covered = set()  # 该广播台覆盖的州
    for station, states in stations.items():
        covered = states_needed & states  # 计算交集
        if len(covered) > len(states_covered):  # 检查该广播台覆盖的州是否比best_station多
            best_station = station  # 如果是，将 best_station 设置为当前广播台
            states_covered = covered

    final_stations.add(best_station)  # 将best_sation 添加到最终广播台列表中
    states_needed -= states_covered   # 更新 states_needed

print(final_stations)