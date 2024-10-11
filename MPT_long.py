# -*- coding: utf-8 -*-
"""
This code makes use of pypoft:
    
    Martin, R. A., (2021). PyPortfolioOpt: portfolio optimization in Python. Journal of Open Source Software, 6(61), 3066, https://doi.org/10.21105/joss.03066
    
MPT Long
"""


import pandas as pd
import numpy as np
from typing import List, Dict
from dataclasses import dataclass

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.expected_returns import mean_historical_return

class MPT:
    
    def __init__(
            self,
            stocks: List[StockInfo],
            risk_free_rate: float,
            ):
            self.stocks = stocks
            self.risk_free_rate = risk_free_rate
    
    def stocks(self):
        return self._stocks
    
    def stocks(self, s):
        if len(s) <4:
            raise TypeError(f"Stock list has length {len(stocks)}, minimal lenght required is 4")
        self._stocks = s
        
    def _stocks_data_frame(self) -> pd.DataFrame:
        return get_stocks_data_frame(stocks = self.stocks)
    
    def _weighting_allocation_max_sharpe(df: pd.DataFrame) -> Dict[StockInfo,float]:
        
        efficient_frontier = EfficientFrontier(
            expected_returns = ,
            cov_matrix = ,
            )
        return dict(efficient_frontier.max_sharpe())
    
    def _expected_returns_per_anum(weighting_allocation_max_sharpe: Dict[StockInfo, float], df: pd.DataFrame) -> float:
        
        weighting = np.array(list(weighting_allocation_max_sharpe.values()))
        expected_returns = .to_numpy()
        #TODO: check if this will return % rtn or growht factors
        return np.dot(weighting, expected_returns)
    
    def _annualised_std(weighting_allocation_max_sharpe: Dict[StockInfo, float], df: pd.DataFrame) -> float:
        
        weighting = np.array(list(weighting_allocation_max_sharpe.values()))
        pct_rtns = df.pct_change(df)
        
        #corrected
        cov_matrix = covariance(df)
        weighting = np.array(list(weighting.values())) * 100
        
        port_var = np.dot(np.dot(np.array(weighting).T,cov_matrix), weighting)
        port_std = np.sqrt(port_var)
        annualised_volatility = port_std * np.sqrt(252)
        
        return annualised_volatility
    
    def _sharpe_ratio(self, expected_returns: float, annualised_std: float) -> float:
        return (
            
            
            )
    
                                             