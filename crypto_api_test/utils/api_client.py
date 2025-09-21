
import os
from decouple import config
import requests

class APIClient:
    def __init__(self):
        # 从 .env 文件获取 API 根 URL
        self.base_url = config('API_ROOT_URL', default='https://api.crypto.com/v2')

    def get_candlestick(self, instrument_name, timeframe, **kwargs):
        """
        调用 public/get-candlestick 接口

        :param instrument_name: 交易对，如 BTC_USDT
        :param timeframe: 时间框架，如 1m, 5m, 1h, 1d
        :param kwargs: 其他可选参数，如 limit, start_ts, end_ts
        :return: API 响应
        """
        endpoint = "/public/get-candlestick"
        url = f"{self.base_url}{endpoint}"
        params = {
            'instrument_name': instrument_name,
            'timeframe': timeframe,
            **kwargs
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # if如果响应状态码不是 200，抛出异常
        return response.json()