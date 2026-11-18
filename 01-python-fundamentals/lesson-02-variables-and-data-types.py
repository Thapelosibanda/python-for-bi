# ============================================================
# Lesson 02 — Variables and Data Types
# ============================================================
# Purpose:
# This script demonstrates how I store values in variables, identify
# common data types, perform arithmetic and comparisons, and convert
# values when business data is stored in an unsuitable type.


# ------------------------------------------------------------
# 1. Variables and assignment
# ------------------------------------------------------------
# A variable is a name used to refer to a value.
# The = symbol is the assignment operator. It assigns the value on
# the right to the variable name on the left.
product_name = "Laptop"
quantity_sold = 15
unit_price = 12500.00

# print() displays the values currently stored in these variables.
print(product_name)
print(quantity_sold)
print(unit_price)


# ------------------------------------------------------------
# 2. Common data types
# ------------------------------------------------------------
# str stores text, int stores whole numbers, float stores numbers
# with decimal places, and bool stores either True or False.
product_name = "Laptop"       # str: a text value
quantity_sold = 15             # int: a whole number
unit_price = 12500.50          # float: a number with decimals
is_available = True            # bool: a True/False value

# type() reports the data type of the value held by each variable.
print(type(product_name))
print(type(quantity_sold))
print(type(unit_price))
print(type(is_available))


# ------------------------------------------------------------
# 3. Arithmetic operators
# ------------------------------------------------------------
# Arithmetic operators perform calculations on numeric values.
a = 10
b = 3

print("Addition:", a + b)             # + adds the two values: 13
print("Subtraction:", a - b)          # - subtracts b from a: 7
print("Multiplication:", a * b)       # * multiplies the values: 30
print("Division:", a / b)             # / divides and returns a decimal result
print("Floor division:", a // b)      # // divides and rounds down: 3
print("Remainder:", a % b)             # % returns the remainder: 1
print("Exponentiation:", a ** b)      # ** raises a to the power: 1000


# ------------------------------------------------------------
# 4. Practical sales calculation
# ------------------------------------------------------------
# Example: 24 wireless mice are sold at R349.99 each, with a 10% discount.
product_name = "Wireless Mouse"
quantity_sold = 24
unit_price = 349.99
discount_rate = 0.10  # 10% is represented as the decimal 0.10.

# Gross revenue is quantity sold multiplied by unit price.
gross_revenue = quantity_sold * unit_price

# The discount amount is 10% of the gross revenue.
discount_amount = gross_revenue * discount_rate

# Net revenue is the amount remaining after subtracting the discount.
net_revenue = gross_revenue - discount_amount

print("Product:", product_name)
print("Gross revenue:", gross_revenue)
print("Discount:", discount_amount)
print("Net revenue:", net_revenue)


# ------------------------------------------------------------
# 5. Type conversion
# ------------------------------------------------------------
# Values imported from files or other systems may be stored as text,
# even when they represent numbers. The value below is initially a str.
quantity = "25"
print("Original quantity type:", type(quantity))

# Multiplying a string by 2 repeats the text; it does not perform
# numeric multiplication. This demonstrates why data types matter.
print("Repeating the string:", quantity * 2)

# int() converts suitable numeric text into a whole-number integer.
quantity = int(quantity)
print("Converted quantity:", quantity)
print("Converted quantity type:", type(quantity))

# float() converts suitable numeric text into a decimal number.
unit_price = "45.75"
unit_price = float(unit_price)

# Customer IDs identify customers; they are not used as quantities.
# Keeping an ID as a string preserves leading zeros such as 000789.
customer_id = "000789"

total_transaction = quantity * unit_price

print("Unit price:", unit_price)
print("Customer ID:", customer_id)
print("Customer ID data type:", type(customer_id))
print("Total transaction value:", total_transaction)


# ------------------------------------------------------------
# 6. Comparison operators
# ------------------------------------------------------------
# Comparison operators compare values and return a Boolean result:
# True when the comparison is correct, or False when it is not.
sales_target = 100000
actual_sales = 125000

print("Above target:", actual_sales > sales_target)          # > greater than
print("Exactly on target:", actual_sales == sales_target)   # == equal to
print("Below target:", actual_sales < sales_target)         # < less than

# Important distinction: = assigns a value; == compares two values.


# ------------------------------------------------------------
# 7. Exercise 1 — Employee information
# ------------------------------------------------------------
# QUESTION:
# Create variables for an employee's name, age, monthly salary and
# permanent employment status. Display each value, use type() to check
# each data type, and calculate the employee's annual salary.
#
# MY SOLUTION:
employee_name = "Thabo"       # Employee name is text (str).
employee_age = 28              # Age is a whole number (int).
monthly_salary = 18500.50      # Salary includes decimals (float).
is_permanent = True            # Employment status is Boolean (bool).

print("Employee name:", employee_name)
print("Employee age:", employee_age)
print("Monthly salary:", monthly_salary)
print("Permanent employee:", is_permanent)

# type() checks that each value has the intended data type.
print("Name data type:", type(employee_name))
print("Age data type:", type(employee_age))
print("Salary data type:", type(monthly_salary))
print("Employment status data type:", type(is_permanent))

# Annual salary is monthly salary multiplied by 12 months.
annual_salary = monthly_salary * 12
print("Annual salary:", annual_salary)


# ------------------------------------------------------------
# 8. Exercise 2 — Retail sales calculation
# ------------------------------------------------------------
# QUESTION:
# A store sells 18 keyboards at R249.50 each and applies a 5% discount.
# Store the product, quantity, unit price and discount rate in variables.
# Calculate and display gross revenue, the discount amount and net revenue.
#
# MY SOLUTION:
product = "Keyboard"
quantity_sold = 18
unit_price = 249.50
discount_rate = 0.05  # 5% represented as a decimal.

gross_revenue = quantity_sold * unit_price
discount_amount = gross_revenue * discount_rate
net_revenue = gross_revenue - discount_amount

print("Gross revenue:", gross_revenue)
print("Discount amount:", discount_amount)
print("Net revenue:", net_revenue)


# ------------------------------------------------------------
# 9. Exercise 3 — Data type conversion
# ------------------------------------------------------------
# QUESTION:
# The quantity "150" and unit price "45.75" are stored as strings.
# Convert the quantity to int and the unit price to float, then calculate
# the transaction value. Keep customer ID "000789" as a string so its
# leading zeros are preserved. Display the resulting data types and value.
#
# MY SOLUTION:
quantity = "150"
unit_price = "45.75"
customer_id = "000789"

quantity = int(quantity)
unit_price = float(unit_price)

# The converted numeric values can now be used in a calculation.
total_transaction = quantity * unit_price

print("Quantity data type:", type(quantity))
print("Unit price data type:", type(unit_price))
print("Customer ID:", customer_id)
print("Customer ID data type:", type(customer_id))
print("Total transaction value:", total_transaction)
