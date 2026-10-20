import re

a = '两点水|twowater|liangdianshui|草根程序员'
print(re.findall('[a-z]+', a))
# ['twowater', 'liangdianshui']