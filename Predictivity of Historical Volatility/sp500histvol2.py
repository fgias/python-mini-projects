import datetime
import pandas as pd
from pandas_datareader import data as web
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')
plt.rcParams['figure.figsize'] = (20,10)

sp500_df = web.DataReader('^GSPC', 'yahoo', datetime.datetime(1950,1,1), datetime.datetime(2019,12,19))
sp500_df.to_csv('sp500_prices.csv')
sp500_df = pd.read_csv('sp500_prices.csv', parse_dates=True)
px = sp500_df.set_index('Date')['Adj Close']
rets = px.pct_change().dropna()
import numpy as np

n_days=252 # trading days in a year
time_periods = [1]# in years
stds = []
for t in time_periods:
    stds.append(rets.rolling(t * n_days).std().shift(-20 * n_days))
std_df = pd.concat(stds, axis = 1)
std_df.columns = [f'{t}y' for t in time_periods]
std_df *= np.sqrt(252) # annualize
std_df.plot()
plt.savefig("std3_plot.png", dpi=400)

