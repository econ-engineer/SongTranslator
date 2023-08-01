import plotly.graph_objects as go
import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
bitcoin = cg.get_coin_market_chart_by_id(id = "bitcoin", vs_currency = "usd", days= 30)
prices_dataframe = pd.DataFrame(bitcoin['prices']).rename(columns = {0:'Timestamp', 1:'Prices'})
prices_dataframe['Date'] = pd.to_datetime(prices_dataframe['Timestamp'], unit= "ms")

candlestick_data = prices_dataframe.groupby(prices_dataframe["Date"].dt.date).agg({"Prices": ['min','max',
            'first','last']})


fig = go.Figure(data = [go.Candlestick(x = candlestick_data.index,
                                                    open = candlestick_data['Prices']['first'],
                                                    close = candlestick_data['Prices']['last'],
                                                    high = candlestick_data["Prices"]['max'],
                                                    low = candlestick_data['Prices']['min'])
                                                        ])


