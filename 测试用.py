import re
r = '炼狱篇1'
res = re.search("炼狱篇(\d)",r).group(1)
print(res)