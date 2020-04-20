def get_dict_key(dict, value):
    key_list = [k for k, v in dict.items() if v == value]
    return key_list[0] if key_list else key_list

TOP_NAMES = {
    "排行榜":"雷石总榜",
    "最新热门":"每日榜",
    "KTV热歌榜":"热唱榜",
    "KTV新歌榜":"新歌榜",
    "DJ榜":"DJ榜",
    "经典戏曲":"戏曲榜",
    "网络红歌":"网红歌榜",
    "情歌对唱榜":"情歌对唱",
    "粤语排行榜":"粤语歌榜",
    "k米评分榜":"打分榜",
    "外语榜":"外语歌榜",
    "儿童歌曲":"儿歌榜"
}


type = 'hgdgh'
top_name = get_dict_key(TOP_NAMES, type)
print(top_name)