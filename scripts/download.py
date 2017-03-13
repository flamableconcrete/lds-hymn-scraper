import requests

print('')
print('*****************************')
print('*         downloading!      *')
print('*****************************')

with open('hymns.html', 'wb') as _file:
    response = requests.get('https://www.lds.org/music/library/hymns?lang=eng#d')

    if not response.ok:
        print 'mega fail'

    _file.write(response.content)