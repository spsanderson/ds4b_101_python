# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# JUMPSTART (Module 1): First Sales Analysis with Python ----

# Important VSCode Set Up:
#   1. Select a Python Interpreter: ds4b_101p
#   2. Delete terminals to start a fresh Python Terminal session

# 1.0 Load Libraries ----

# Core Python Data Analysis
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt



# Plotting
from plotnine import (
    ggplot, 
    aes, 
    geom_col,
    geom_line,
    geom_smooth,
    facet_wrap,
    scale_y_continuous,
    scale_x_continuous,
    scale_x_datetime,
    labs,
    theme,
    theme_minimal,
    theme_matplotlib
)

from mizani.breaks import date_breaks
from mizani.formatters import date_format, currency_format

# Misc
from os import mkdir, getcwd
from rich import pretty
pretty.install()

np.sum([1,2,3])


# 2.0 Importing Data Files ----

help(pd.read_excel)
# - Use "q" to quit

# getcwd()
bikes_df = pd.read_excel("../00_data_raw/bikes.xlsx")
bikes_df

bikeshops_df = pd.read_excel("../00_data_raw/bikeshops.xlsx")
bikeshops_df

orderlines_df = pd.read_excel("../00_data_raw/orderlines.xlsx")
orderlines_df

# 3.0 Examining Data ----



# 4.0 Joining Data ----



# 5.0 Wrangling Data ----

# * No copy


# * Copy



# * Handle Dates


# * Show Effect: Copy vs No Copy


# * Text Columns


# * Splitting Description into category_1, category_2, and frame_material



# * Splitting Location into City and State


# * Price Extended


# * Reorganizing


# * Renaming columns


# 6.0 Visualizing a Time Series ----


# 6.1 Total Sales by Month ----


# Quick Plot ----


# Report Plot ----



# 6.2 Sales by Year and Category 2 ----

# ** Step 1 - Manipulate ----


# Step 2 - Visualize ----


# Simple Plot


# Reporting Plot



# 7.0 Writing Files ----


# Pickle ----


# CSV ----


# Excel ----


# WHERE WE'RE GOING
# - Building a forecast system
# - Create a database to host our raw data
# - Develop Modular Functions to:
#   - Collect data
#   - Summarize data and prepare for forecast
#   - Run Automatic Forecasting for One or More Time Series
#   - Store Forecast in Database
#   - Retrieve Forecasts and Report using Templates