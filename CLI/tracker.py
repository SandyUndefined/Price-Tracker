# TODO : Check url is valid or not
# TODO : To send alert we can use AWS Lambda or wayscript (https://wayscript.com/)
from bs4 import BeautifulSoup
import requests
import re

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"}
search_url = ("https://www.flipkart.com/whirlpool-4-1-convertible-cooling-ton-3-star-split-inverter-ac-white/p/itm0ef091d45778d?pid=ACNFZZYZMJFKXJCY&lid=LSTACNFZZYZMJFKXJCYYWHL4G&marketplace=FLIPKART&store=j9e%2Fabm%2Fc54&srno=b_1_10&otracker=hp_omu_Top%2BOffers_2_3.dealCard.OMU_Q4GBXG45QNVZ_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_2_NA_view-all_3&fm=neo%2Fmerchandising&iid=fcbe2df3-ba74-4bac-acea-9657eaeee562.ACNFZZYZMJFKXJCY.SEARCH&ppt=hp&ppn=homepage&ssid=iqv84z8me0yo2a681622150173921")
set_price = 25000


def flipkart():
    response = requests.get(search_url, headers=user_agent)
    # print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', class_="yhB1nd").text
        price = soup.find('div', class_="_30jeq3 _16Jk6d").text
        # converted_price = float(re.sub(r"[^\d.]", "", price))
        converted_price = 24000
        if converted_price <= float(set_price):
            sendAlert()
        else:
            print("does nothing")


def sendAlert():
    print("alert")


if __name__ == "__main__":
    flipkart()
