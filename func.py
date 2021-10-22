import numpy as np
import pandas as pd
from glassnode import GlassnodeClient
from coinmetrics.api_client import CoinMetricsClient

# glassnode's api key
GLASSNODE_API_KEY = "1zp3jkwRdnE9ZaEUqb95RhmekCY"
# load glass node client
gn = GlassnodeClient()
# setting glassnode's api key
gn.set_api_key(GLASSNODE_API_KEY)

# get realized price
realized_price = gn.get('https://api.glassnode.com/v1/metrics/market/price_realized_usd', 
                        a='BTC', 
                        s='2011-01-01', 
                        i='24h'
)

# get market cap
market_capa = gn.get('https://api.glassnode.com/v1/metrics/market/marketcap_usd',
                    a='BTC', 
                    s='2011-01-01', 
                    i='24h'
)

# get realized cap
realized_capa = gn.get('https://api.glassnode.com/v1/metrics/market/marketcap_realized_usd', 
                      a='BTC', 
                      s='2011-01-01', 
                      i='24h'
)


###### 
# https://docs.coinmetrics.io/api/v4
# https://coinmetrics.github.io/api-client-python/site/index.html#extended-documentation
# or to use community API:

class coinmetrics_info(object):
    """
    gets any type of deseried information from coinmetrics
    """
    
    def __init__(self, asset, frequency):
        self.asset = asset
        self.frequency = frequency
    
    def get_asset_metrics(self, metric):
        cm = CoinMetricsClient()
        time = []
        value = []
        for trade in cm.get_asset_metrics(assets=self.asset, metrics=[metric], frequency=self.frequency):
            if trade['time'].partition('-')[0] in ["2021", "2020", "2019", "2018", "2017", "2016", 
                                                   "2015", "2014", "2013", "2012", "2011"]:
                time.append(trade['time'].partition('T')[0])
                value.append(float(trade[metric]))
                
        return pd.Series(data=value , index=time).sort_index()




