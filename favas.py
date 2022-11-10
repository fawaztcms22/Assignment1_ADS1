# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd


world = pd.read_csv("E:/Herts/ADS1/Assignment 1/favas/1990-2021.csv")
plt.figure()

def rate_conversion(currency_name, conversion_multiplier):
    """
        Converts gold rate in different currency to rate in USD. Input must be 
        country name with currency name inside parenthesis and multiplier between that currency and usd.
        Creates dataframe with gold rate of that country in USD.
    """
    currency_name_in_usd = currency_name.partition("(")[0] + "(USD)"
    world[currency_name_in_usd] = world[currency_name]*conversion_multiplier


rate_conversion("Japan(JPY)", 0.0068)
rate_conversion("United Kingdom(GBP)", 1.14)
rate_conversion("Thailand(THB)", 0.027)

plt.figure()
plt.plot(world["Date"],world["United States(USD)"],label="US")
plt.plot(world["Date"],world["Japan(USD)"],label="JP")
plt.plot(world["Date"],world["United Kingdom(USD)"],label="UK")
plt.plot(world["Date"],world["Thailand(USD)"],label="THAI")
plt.legend()

plt.figure()
plt.hist(world["Japan(USD)"],density=True,alpha=0.8,label="JP")
plt.hist(world["United States(USD)"],density=True,alpha=0.8,label="US")
plt.hist(world["United Kingdom(USD)"],density=True,alpha=0.8,label="UK")
plt.hist(world["Thailand(USD)"],density=True,alpha=0.8,label="THAI")
plt.show()


data = [world["United States(USD)"], world["Japan(USD)"],world["United Kingdom(USD)"], world["Thailand(USD)"]]
dlabel = ["US", "JP", "UK", "THAI"]

plt.figure()
plt.boxplot([data[0] , data[1] , data[2], data[3]],labels=["US", "JP", "UK", "THAI"])
plt.ylabel("Price")
plt.show()

