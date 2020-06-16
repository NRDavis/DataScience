'''
https://www.investopedia.com/terms/f/famaandfrenchthreefactormodel.asp

The Fama and French Three-Factor Model (or the Fama French Model for short) is an asset pricing model developed in 1992
that expands on the capital asset pricing model (CAPM) by adding size risk and value risk factors to the market risk
factor in CAPM. This model considers the fact that value and small-cap stocks outperform markets on a regular basis.
By including these two additional factors, the model adjusts for this outperforming tendency, which is thought to make
it a better tool for evaluating manager performance.



The Fama French 3-factor model is an asset pricing model that expands on the capital asset
pricing model by adding size risk and value risk factors to the market risk factors.

The model was developed by Nobel laureates Eugene Fama and his colleague Kenneth French in the 1990s.

The model is essentially the result of an econometric regression of historical stock prices.


The Formula for the Fama French 3 Factor Model Is:
Rit​−Rft​=αit​+β1​(RMt​−Rft​)+β2​SMBt​+β3​HMLt​+ϵit

Rit​=total return of a stock or portfolio i at time t
Rft​=risk free rate of return at time t
RMt​=total market portfolio return at time t
Rit​−Rft​=expected excess return
RMt​−Rft​=excess return on the market portfolio (index)
SMBt​=size premium (small minus big)
HMLt​=value premium (high minus low)
β1,2,3​=factor coefficients​


Three factors:
    Size of Firms
    Book to market values
    excess return on the market



https://blog.quantinsti.com/fama-french-five-factor-asset-pricing-model/
'''

import numpy as np

# we define a dictionary to take our arguments -- simplified calling it later
var = {"Rit":  0,
       "Rft":  0,
       "RMt":  0,
       "SMBt": 0,
       "HMLt": 0,
       "B1":   0,
       "B2":   0,
       "B3":   0
       }

# define Fama and French 3 factor function



