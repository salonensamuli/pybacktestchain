#%%
from pybacktestchain.market_data import MarketData
market_data = MarketData()
df = market_data.get_data("AAPL", "2020-01-01", "2021-01-01")
#%%
from pybacktestchain.strategy import MovingAverageCrossoverStrategy
strategy = MovingAverageCrossoverStrategy(short_window=40, long_window=100)

from pybacktestchain.broker import SimulatorBroker
broker = SimulatorBroker(initial_cash=100000, transaction_cost=0.01)

from pybacktestchain.backtest import Backtest
from pybacktestchain.optimizer import MaximizeSharpeRatio
from pybacktestchain.risk_manager import MaxDrawdownConstraint

backtest = Backtest(strategy, market_data, broker, MaxDrawdownConstraint(max_dd=0.1), MaximizeSharpeRatio())


backtest.run("AAPL", "2020-01-01", "2021-01-01")

#%%
    
    
 

