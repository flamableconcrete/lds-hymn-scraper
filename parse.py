from bs4 import BeautifulSoup

print('')
print('*****************************')
print('*         parsing!          *')
print('*****************************')


def main():
    html_doc = open('hymns.html', 'r')
    soup = BeautifulSoup(html_doc, 'html.parser')

    for script in soup.find_all('script'):
        print(script)

if __name__ == "__main__":
    main()