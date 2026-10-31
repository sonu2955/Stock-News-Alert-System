import requests
from twilio.rest import Client
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


##TODO STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
AV_Endpoint = "https://www.alphavantage.co/query"
AV_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey"  : os.getenv("AV_API_KEY") # Remember there is 25 request per day Limit on per API_key
}
#TODO : Remember there is 25 request per day Limit on per API_key. so if limit reached try another api key


response = requests.get(url=AV_Endpoint, params=AV_params)
response.raise_for_status()


tesla_stock_data = response.json()
print(tesla_stock_data)
#todo : un-comment below code once api key daily limit is restarted
dates = list(tesla_stock_data["Time Series (Daily)"].keys())
closing_today = float(tesla_stock_data["Time Series (Daily)"][dates[0]]["4. close"])
closing_yesterday = float(tesla_stock_data["Time Series (Daily)"][dates[1]]["4. close"])
print(closing_today)
print(closing_yesterday)

difference = closing_today - closing_yesterday
percentage = (difference/closing_today) * 100
print(difference, percentage)



##TODO STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
Newsapi_Endpoint = ("https://newsapi.org/v2/everything")

today = datetime.now()
print(int(today.strftime('%d'))-1)
Newsapi_params = {
    "q" : COMPANY_NAME,
    "from" : f"{today.strftime('%Y')}-{today.strftime('%m')}-{int(today.strftime('%d'))-2}",
    "sortBy" : "Relevancy",
    "apikey" : os.getenv("Newapi_API_KEY")
}

news_response = requests.get(url=Newsapi_Endpoint, params=Newsapi_params)
news_response.raise_for_status()
news_data = news_response.json()["articles"]
print(news_data)



##TODO STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

account_sid = os.getenv("Twilio_account_sid")
auth_token = os.getenv("Twilio_auth_token")

if percentage > 0:
    logo = "🔺"
else:
    logo = "🔻"

news = news_data[0]
print(f"{STOCK} : 🔺{percentage}%\nHeadline : {news['title']}\nContent : {news['content']}\n{news['url']}")

# TODO : You can use below send message to yourself as alart
# client = Client(account_sid, auth_token)
# messages = client.messages \
#         .create(
#         body = f"{STOCK} : {logo}{percentage}%\n{news['url']}",
#         from_= "+13527803863",
#         to= f"+91{Your Number}",
#     )
# print(messages.status)


