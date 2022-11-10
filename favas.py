# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

#File read into pandas dataframe
world = pd.read_csv("E:/Herts/ADS1/Assignment 1/favas/1990-2021.csv")
plt.figure()

def rate_conversion(currency_name, conversion_multiplier):
    """Converts gold rate in different currency to rate in USD. Input must be 
    country name with currency name inside parenthesis and multiplier between that currency and usd.
    Creates dataframe with gold rate of that country in USD."""

    currency_name_in_usd = currency_name.partition("(")[0] + "(USD)"
    world[currency_name_in_usd] = world[currency_name]*conversion_multiplier

#Calls rate conversion function for the countries required
rate_conversion("Japan(JPY)", 0.0068)
rate_conversion("United Kingdom(GBP)", 1.14)
rate_conversion("Thailand(THB)", 0.027)

def lineplt(y_axis, Country1, Country2, Country3, Country4):
    """Creates a graph of gold prices from 2000 to 2020 of selected countries"""
    plt.figure()
    plt.plot(world[y_axis], world[Country1], label="US")
    plt.plot(world[y_axis], world[Country2], label="JP")
    plt.plot(world[y_axis], world[Country3], label="UK")
    plt.plot(world[y_axis], world[Country4], label="TH")
    plt.xlabel("Year")
    #plt.xlim(2000,2020)
    plt.ylabel("Gold Price in USD")
    plt.legend()
    plt.savefig("lineplt.png")
    plt.show()

def hist(y_axis, Country1, Country2, Country3, Country4):
    """Creates a histogram of gold prices of 4 countries during the time 2000-2020"""

    plt.figure()
    plt.hist(world["United States(USD)"], density=True, alpha=0.8, label="US")
    plt.hist(world["Japan(USD)"], density=True, alpha=0.8, label="JP")
    plt.hist(world["United Kingdom(USD)"], density=True, alpha=0.8, label="UK")
    plt.hist(world["Thailand(USD)"], density=True, alpha=0.8, label="TH")
    plt.xlabel("Gold price")
    plt.legend()
    plt.savefig("hist.png")
    plt.show()


#List of dataframes for box function
countries = [world["United States(USD)"], world["Japan(USD)"], world["United Kingdom(USD)"], world["Thailand(USD)"]]


def box(countries):
    """Creates a box plot of gold prices of some countries withan array of those dataframes as input"""
    plt.figure()
    plt.boxplot([countries[0] , countries[1] , countries[2], countries[3]],labels=["US", "JP", "UK", "TH"])
    plt.ylabel("Gold Price in USD")
    plt.savefig("box.png")
    plt.show()


#Calling the functions for 3 plots
lineplt("Date", "United States(USD)", "Japan(USD)", "United Kingdom(USD)", "Thailand(USD)")
hist("Date", "United States(USD)", "Japan(USD)", "United Kingdom(USD)", "Thailand(USD")
box(countries)