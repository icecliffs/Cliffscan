import json, re

# 读取JSON文件
with open('service.json', 'r') as file:
    data = json.load(file)
# print(data[0]['matches'][0]['pattern'])
print(data)



# for i in range(len(data[0]['matches'])):
    # if str(data[0]['matches'][i]['pattern']).startswith('^SSH-'):
        # print(str(data[0]['matches'][i]['pattern']).replace('\\', '\\\\'))