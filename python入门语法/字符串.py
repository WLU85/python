""""
字符串的三种表达方式
|转义字符
字符串拼接 +
字符串格式化
"""
name = '1'
print(name)
name = "2"
print(name)
name = """3"""
print(name)
print("1"+name)
zifu = "dada sda AsDA"
print(zifu.title())# 首字母大写 其余小写
print(zifu.lower())# 全小写
print(zifu.upper())# 全大写

la = "    sds    "
la = la.rstrip()
# 删除右空白
la = la.lstrip()
# 删除左空白
print(la)
la = "    asda    "
la = la.strip()
# 删除空白
print(la)
