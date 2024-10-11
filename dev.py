#%%
from pybacktestchain.data_module import  FirstTwoMoments
from pybacktestchain.broker import Backtest
from datetime import datetime, timedelta
import pandas as pd
backtest = Backtest(
    initial_date = datetime(2010, 1, 1)+pd.offsets.BMonthEnd(0),
    final_date = datetime(2020, 1, 1)+pd.offsets.BMonthEnd(0),
    information_class = FirstTwoMoments,
    )

# %%
backtest.run_backtest()
# %%
