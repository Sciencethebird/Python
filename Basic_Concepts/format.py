
#code credit http://www.runoob.com/python/att-string-format.html

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# use *args
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0}, 地址 {1}".format(*my_list))  

pi = 3.14159
print("Pi value is {:.2f}".format(pi))

my_str = "Pi value is {:.2f}".format(pi) #format returns a string
my_str += '.'
print(my_str)