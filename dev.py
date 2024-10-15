#%%
from pybacktestchain.data_module import  FirstTwoMoments
from pybacktestchain.broker import Backtest, StopLoss
from datetime import datetime

backtest = Backtest(
    initial_date = datetime(2010, 1, 1),
    final_date = datetime(2020, 1, 1),
    information_class = FirstTwoMoments,
    risk_model=StopLoss
    )

backtest.run_backtest()


# %%
