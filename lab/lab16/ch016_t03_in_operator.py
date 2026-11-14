my_dict = {
    "Name": "Peter",
    "Age": 18,
    "BDFL": True
}

# 用 in 遍历字典的每个键，逐个打印键和对应的值，所有内容保持在同一行
for key in my_dict:
    print(key, my_dict[key], end=" ")