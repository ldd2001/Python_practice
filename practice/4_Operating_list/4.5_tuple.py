# 不可改变的列表叫做元组 也是列表的一种，
# 元组使用()标识，不可修改

# 一个不变的矩形
dimensions = (100,50)
print(dimensions[0])
print(dimensions[-1])

#修改dimension,不可以对tuple进行修改，只能重新赋值

dimensions = (200,100)
print(dimensions)

#如果一个元组只包含一个元素，那么需要加上, 例如

new_dimensions = (3,)
print(new_dimensions)
#但是，元组中有很多元素，一个元素没意义

#元组中的顺序很重要，输出元组数据需要记好元组中的元素索引