from glassnode import GlassnodeClient
import numpy as np


# glassnode's api key
GLASSNODE_API_KEY = "1zp3jkwRdnE9ZaEUqb95RhmekCY"

# load glass node client
gn = GlassnodeClient()

# setting glassnode's api key
gn.set_api_key(GLASSNODE_API_KEY)

# get realized price
realized_price = gn.get('https://api.glassnode.com/v1/metrics/market/price_realized_usd', 
                        a='BTC', 
                        s='2017-01-01', 
                        i='24h'
)

# get market cap
market_cap = gn.get('https://api.glassnode.com/v1/metrics/market/marketcap_usd',
                    a='BTC', 
                    s='2017-01-01', 
                    i='24h'
)
# get realized cap
realized_cap = gn.get('https://api.glassnode.com/v1/metrics/market/marketcap_realized_usd', 
                      a='BTC', 
                      s='2017-01-01', 
                      i='24h'
)

