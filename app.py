import streamlit as st
import numpy as np
from scipy.optimize import brentq

# Import modules
from data_fetch import get_stock_price
from black_scholes import call_price, put_price
from greeks import delta, gamma, vega, theta
from visualization import (
    plot_price_vs_stock,
    plot_volatility,
    plot_payoff,
    plot_heatmap
)

# Monte Carlo

def monte_carlo_call(S, K, T, r, sigma, simulations=10000):
    np.random.seed(42)
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0)
    return np.exp(-r * T) * np.mean(payoff)


# Implied volatility (Fixed)

def implied_volatility_call(market_price, S, K, T, r):
    intrinsic = max(S - K, 0)

    # Invalid case
    if market_price < intrinsic:
        return np.nan

    try:
        func = lambda sigma: call_price(S, K, T, r, sigma) - market_price
        return brentq(func, 1e-5, 3)
    except ValueError:
        return np.nan


# Streamlit

st.title("📊 Advanced Option Pricing Dashboard")

st.sidebar.header("Inputs")

# Ticker selection
ticker = st.sidebar.selectbox(
    "Select Stock",
    ["AAPL", "TSLA", "MSFT", "GOOGL", "RELIANCE.NS", "TCS.NS"]
)

# Custom ticker override
custom = st.sidebar.text_input("Or enter custom ticker")
if custom:
    ticker = custom

# Inputs
K = st.sidebar.number_input("Strike Price", value=100.0)
T = st.sidebar.number_input("Time to Maturity (years)", value=1.0)
r = st.sidebar.number_input("Risk-Free Rate", value=0.05)
sigma = st.sidebar.number_input("Volatility (σ)", value=0.2)

# Fetch stock price
S = get_stock_price(ticker)

if S is None:
    st.warning("Using default stock price (100)")
    S = 100

st.write(f"### Current Stock Price: {S:.2f}")

# Default market price from BS
default_price = call_price(S, K, T, r, sigma)

market_price = st.sidebar.number_input(
    "Market Option Price (for IV)",
    value=float(default_price)
)


#Calculations

call = call_price(S, K, T, r, sigma)
put = put_price(S, K, T, r, sigma)
mc = monte_carlo_call(S, K, T, r, sigma)
iv = implied_volatility_call(market_price, S, K, T, r)


st.subheader("Option Prices")
st.write(f"Call Price (Black-Scholes): {call:.2f}")
st.write(f"Call Price (Monte Carlo): {mc:.2f}")
st.write(f"Put Price: {put:.2f}")

st.subheader("Implied Volatility")
st.write(f"IV: {iv:.4f}")

# Debug info
st.write(f"Intrinsic Value: {max(S-K,0):.2f}")
st.write(f"Market Price: {market_price:.2f}")

st.subheader("Greeks")
st.write(f"Delta: {delta(S,K,T,r,sigma):.4f}")
st.write(f"Gamma: {gamma(S,K,T,r,sigma):.4f}")
st.write(f"Vega: {vega(S,K,T,r,sigma):.4f}")
st.write(f"Theta: {theta(S,K,T,r,sigma):.4f}")

st.subheader("Price vs Stock Price")
st.pyplot(plot_price_vs_stock(S, K, T, r, sigma))

st.subheader("Volatility Impact")
st.pyplot(plot_volatility(S, K, T, r))

st.subheader("Payoff Diagrams")
st.pyplot(plot_payoff(K))

st.subheader("Heatmap (Price vs Volatility)")
st.pyplot(plot_heatmap(S, K, T, r))