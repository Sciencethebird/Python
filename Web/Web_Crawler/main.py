import urllib.request as magic

def download_image(URL, file_name):
    file_name += '.jpg'
    magic.urlretrieve(URL, file_name)



url = 'https://i.kym-cdn.com/entries/icons/original/000/017/618/pepefroggie.jpg'
download_image(url, 'froggif')