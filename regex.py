import re
s = "ipv6"
pattern = "^[a-z]{3}[0-9]{1}$"
res = re.findall(pattern, s)
print(res)
