from asyncio import run
import json
from time import sleep
from datetime import datetime
from api import api

if __name__ == "__main__":
    while True:
        sleep(15)
        res_buy = run(api.send_request('/buyStock', 'GET'))
        with open(f'dump/buy{datetime.now().timestamp()}.json', 'w') as f:
            json.dump(res_buy, f)
        res_sell = run(api.send_request('/sellStock', 'GET'))
        with open(f'dump/sell{datetime.now().timestamp()}.json', 'w') as f:
            json.dump(res_sell, f)
        res_news = run(api.send_request('/news/LatestNews', 'GET'))
        with open(f'dump/news{datetime.now().timestamp()}.json', 'w') as f:
            json.dump(res_news, f)
