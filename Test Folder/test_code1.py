import datetime as dt
import time as sleep

class Backtester:

    def __init__(self, symbol, start_date, end_date, data_source="google"):
        print('in __init__ in Backtester class')
        sleep.sleep(2.0)
        self.target_symbol = symbol
        self.data_source = data_source
        self.start_dt = start_date
        self.end_dt = end_date
        self.strategy = None
        self.unfilled_orders = []
        self.positions = dict()
        self.current_prices = None

    def start_backtest(self):
        print('in start_backtest in Backtester class')
        sleep.sleep(2.0)

        mds.event_tick = self.evthandler_tick
        mds.ticker = self.target_symbol
        mds.source = self.data_source
        mds.start, mds.end = self.start_dt, self.end_dt

        print("Backtesting started...")
        mds.start_market_simulation()
        print("Completed.")


backtester = Backtester("XBTUSD", dt.datetime(2017, 7, 20),
                        dt.datetime(2020, 1, 1), data_source="csv_file")
backtester.start_backtest()