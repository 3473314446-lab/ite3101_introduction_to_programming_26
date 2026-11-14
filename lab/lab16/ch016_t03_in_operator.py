my_dict = {
    "Name": "Peter",
    "Age": 18,
    "BDFL": True
}

# 遍历字典中的每一个 key
for key in my_dict:
    # print(a, b) 会自动在两个参数之间加空格，满足题目要求，无需字符串拼接
    print(key, my_dict[key])
