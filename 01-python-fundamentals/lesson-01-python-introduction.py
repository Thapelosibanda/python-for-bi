# ============================================================
# Lesson 01 — Python Introduction
# ============================================================
# Purpose:
# This script records my introductory Python practice for Business
# Intelligence (BI) and data work. It covers displaying output,
# importing libraries, checking the Python environment, and using
# a simple calculation with business data.
#
# The practice activities at the end are written as prompts followed
# by my example solutions. The original Lesson 1 notebook contained
# demonstrations rather than a separate, formal exercise list.


# ------------------------------------------------------------
# 1. Displaying information with print()
# ------------------------------------------------------------
# print() displays information in the output. Text must be placed
# inside quotation marks so Python recognises it as a string.
print("Hello, world!")


# ------------------------------------------------------------
# 2. Importing modules and libraries
# ------------------------------------------------------------
# import makes code from another module or library available here.
# sys is included with Python and provides information about the
# Python interpreter and the environment running this script.
import sys

# pandas is commonly used to work with structured, tabular data.
# The alias pd is the conventional shorthand used in Python projects.
import pandas as pd

# NumPy provides tools for numerical calculations and array operations.
# The alias np is the conventional shorthand for the NumPy library.
import numpy as np


# ------------------------------------------------------------
# 3. Checking the active Python environment
# ------------------------------------------------------------
# sys.version displays the version of Python currently running.
print("Python version:", sys.version)

# sys.executable displays the location of the Python interpreter.
# This helps me confirm which Python environment is executing the code.
print("Python executable:", sys.executable)

# __version__ is an attribute that reports the installed library version.
# Version checks are useful when investigating compatibility issues.
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)


# ------------------------------------------------------------
# 4. A simple business calculation
# ------------------------------------------------------------
# These variables represent a product, the quantity sold, and its price.
# The values are stored so that they can be reused in a calculation.
product = "Laptop"
quantity_sold = 15
unit_price = 12500.00

# Revenue is calculated by multiplying the quantity sold by the unit price.
total_revenue = quantity_sold * unit_price

# Display each input and the calculated result.
print("Product:", product)
print("Quantity sold:", quantity_sold)
print("Unit price:", unit_price)
print("Total revenue:", total_revenue)


# ------------------------------------------------------------
# 5. Practice activities
# ------------------------------------------------------------
# Activity 1 — Change the greeting
# QUESTION:
# Change the message below so that it introduces a Python project for
# Business Intelligence or data analysis.
#
# MY EXAMPLE SOLUTION:
print("Welcome to my Python for Business Intelligence project!")

# Activity 2 — Inspect the Python environment
# QUESTION:
# Display the Python version, the path to the Python interpreter,
# and the installed versions of pandas and NumPy.
#
# MY EXAMPLE SOLUTION:
print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)

# Activity 3 — Identify a BI use case
# QUESTION:
# Use print() to display one example of how Python could support a
# Business Intelligence or data engineering task.
#
# MY EXAMPLE SOLUTION:
print("Python can automate repetitive data cleaning and validation tasks.")
