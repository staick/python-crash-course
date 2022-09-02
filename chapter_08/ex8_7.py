# 8-7. Album
def make_album(artist, title, number=None):
    album = {}
    album[artist] = title
    if number:
        album['number']=number
    return album

print(make_album('Miku', "Miku"))
print(make_album('LuoTianyi', 'LuoTianyi'))
print(make_album('Jay Zhou', 'blue and white pocelain'))
print(make_album('Staick', 'None', '1'))
