import matplotlib.pyplot as plt
from load_data import *

def plot(data):
    data.plot(figsize=(20,8))
    plt.xlabel('Date')
    plt.ylabel('Proportion')
    plt.title('Relative Unrealized Profit/Loss')
    plt.show()
    
    
cmi = coinmetrics_info(asset = "btc", frequency = "1d")

market_cap = cmi.get_asset_metrics(metric="CapMrktCurUSD")
realized_cap = cmi.get_asset_metrics(metric="CapRealUSD")
rel_unrealized_pl = (market_cap - realized_cap)/market_cap
 

plot(rel_unrealized_pl)



