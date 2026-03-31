import numpy as np
import matplotlib.pyplot as plt
from black_scholes import call_price


# ==============================
# Price vs Stock
# ==============================
def plot_price_vs_stock(S, K, T, r, sigma):
    S_range = np.linspace(0.5 * S, 1.5 * S, 100)
    prices = [call_price(s, K, T, r, sigma) for s in S_range]

    fig, ax = plt.subplots()
    ax.plot(S_range, prices)
    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Call Price")

    return fig


# ==============================
# Volatility Curve
# ==============================
def plot_volatility(S, K, T, r):
    vol_range = np.linspace(0.1, 0.5, 50)
    prices = [call_price(S, K, T, r, v) for v in vol_range]

    fig, ax = plt.subplots()
    ax.plot(vol_range, prices)
    ax.set_xlabel("Volatility")
    ax.set_ylabel("Call Price")

    return fig


# ==============================
# Payoff Diagrams
# ==============================
def payoff_call(S_range, K):
    return np.maximum(S_range - K, 0)


def payoff_put(S_range, K):
    return np.maximum(K - S_range, 0)


def plot_payoff(K):
    S_range = np.linspace(0.5 * K, 1.5 * K, 100)
    call = payoff_call(S_range, K)
    put = payoff_put(S_range, K)

    fig, ax = plt.subplots()
    ax.plot(S_range, call, label="Call Payoff")
    ax.plot(S_range, put, label="Put Payoff")
    ax.legend()

    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Payoff")

    return fig


# ==============================
# Heatmap
# ==============================
def plot_heatmap(S, K, T, r):
    S_vals = np.linspace(0.8 * S, 1.2 * S, 20)
    vol_vals = np.linspace(0.1, 0.5, 20)

    heatmap = np.zeros((len(vol_vals), len(S_vals)))

    for i, v in enumerate(vol_vals):
        for j, s in enumerate(S_vals):
            heatmap[i, j] = call_price(s, K, T, r, v)

    fig, ax = plt.subplots()
    c = ax.imshow(heatmap, aspect='auto')
    fig.colorbar(c)

    ax.set_xlabel("Stock Price Index")
    ax.set_ylabel("Volatility Index")

    return fig