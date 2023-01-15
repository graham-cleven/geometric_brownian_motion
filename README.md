# geometric_brownian_motion

This program will take a given stock symbol and time-frame, reach out to the Yahoo finance API and grab the required historical data.  
From these results, the program will generate a variable length series of Geometric Brownian Motion (GBM) data-points. based on the mu and sigma values of the underlying security.    
The resulting GBM is plotted graphically.  
The idea is that this could eventually be applied to a back-testing pipeline.
