def make_album(artist, title, number=None):
    album = {}
    album[artist] = title
    if number:
        album['number']=number
    return album

while True:
    artist = input("Enter the artist: ")
    if artist == 'quit':
        break
    title = input("Enter the title: ")
    print(make_album(artist, title))
