"""
两个字符串，求公共字符串
最长公共子串（LCS，Longest Common Substring）
"""


def getLCString(str1, str2):
    maxlen = len(str1) if len(str1) < len(str2) else len(str2)
    example = str1 if len(str1) < len(str2) else str2
    other = str2 if str1 == example else str1
    print(f"maxlen=>{maxlen}, example===>{example}, other===>{other}")

    for i in range(maxlen):
        for j in range(maxlen, 0, -1):
            if other.find(example[i:j]) != -1:
                print(f"i===>{i}, j===>{j}")
                return example[i:j]


if __name__ == '__main__':
    str1 = 'abcddefg'
    str2 = 'ecddyefgh'
    res = getLCString(str1, str2)
    print(res)