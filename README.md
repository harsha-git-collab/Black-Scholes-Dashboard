# Black-Scholes Option Pricing Dashboard

An advanced financial analytics project that implements the Black–Scholes model, Monte Carlo simulation, and implied volatility estimation to price options and analyze risk using real-time market data.


##  Features

Black–Scholes option pricing (Call & Put)
Monte Carlo simulation for validation
Implied volatility calculation
Greeks (Delta, Gamma, Vega, Theta)
Real-time stock data using Yahoo Finance API
Interactive Streamlit dashboard
Payoff diagrams (Call & Put)
Heatmap visualization (Price vs Volatility)

## Dashboard Capabilities

- Compare **Black–Scholes vs Monte Carlo pricing**
- Analyze **option sensitivity using Greeks**
- Visualize **payoff structures**
- Explore **impact of volatility and stock price**
- Compute **implied volatility from market prices**

## Models Used

### Black–Scholes Model
Used for analytical pricing of European options.

### Monte Carlo Simulation
Simulates multiple price paths to estimate option value.

### Implied Volatility
Calculated numerically using root-finding methods.



##  Tech Stack

- Python  
- NumPy  
- Pandas  
- SciPy  
- Matplotlib  
- yFinance  

## How to run
pip install -r requirements.txt

streamlit run app.py  

