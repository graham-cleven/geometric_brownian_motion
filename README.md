# geometric_brownian_motion
Several Python functions for generating GBN and BM for use in financial analysis

## overview
This program will take a given stock symbol, reach out to the Yahoo finance API and grab the historical data.   
It will build a probability distribution function (PDF) of the data and sample the PDF with geometric brownian motion (GBM).    
The resulting GBM is plotted graphically.  
The idea is that this could eventually be applied to a back-testing pipeline. 

## example usage
get_gbm_for_symbol(symbol="SPY", period="1D")
