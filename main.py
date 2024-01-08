from bs4 import BeautifulSoup
from selenium import webdriver
import time

#search = ('yeezy 350')
#search = search.replace(' ', '%20')

url = 'https://www.goat.com/en-ca/search?query='+search+'&size_converted=us_sneakers_men_10'
#url = 'https://www.goat.com/en-ca/search?web_groups=sneakers&size_converted=us_sneakers_men_10'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)


scrollCount = 0
endVar = True

endVar = True

while endVar:
    currentHeight = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    time.sleep(1)
    newHeight = driver.execute_script("return document.body.scrollHeight")

    if currentHeight == newHeight:
        startTimer = time.time()
        while True:

            driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(1)
            newHeight = driver.execute_script("return document.body.scrollHeight")

            if newHeight != currentHeight:
                break

            if time.time() - startTimer >= 15:
                endVar = False
                break



html_text = driver.page_source
driver.quit()

soup = BeautifulSoup(html_text, 'lxml')
shoes = soup.findAll('div', class_='GridStyles__GridCellWrapper-sc-1cm482p-0 hiXKdk')

count = 0;

for shoe in shoes:
    # Extract name, picture, and price information and print or store them as needed
    name = shoe.find('div', class_='GridCellProductInfo__Name-sc-17lfnu8-3 iPovsV').text.strip()
    picture = shoe.find('img')['src']
    price = shoe.find('span', class_='LocalizedCurrency__Amount-sc-yoa0om-0 jDDuev').text.strip()
    count = count + 1
    print(f"Name: {name}\nPicture: {picture}\nPrice: {price}\n{'||'*30}")

print(count)

#git add .
#git commit -m "second commit"
#git push