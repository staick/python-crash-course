places = ['Japan', 'US', 'China', 'Canda', 'Singapore']

# 按字母排序，不修改
print(sorted(places))
print(places)

# 按字母反序，不修改
print(sorted(places, reverse=True))
print(places)

# 使用reverse()，反转
places.reverse()
print(places)

# 再次使用reverse()，恢复
places.reverse()
print(places)

# 使用sort()方法，按字母顺序排序
places.sort()
print(places)

# 使用sort()方法，按字母顺序逆序
places.sort(reverse=True)
print(places)