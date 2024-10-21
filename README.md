# README

## Overview
This repository contains Python functions for weather data aggregation and prime factorization, along with SQL code to update product prices. Each solution is designed to be clear, efficient, and easy to understand.

## Contents
- Weather Data Aggregation Function
- Prime Factorization Function
- SQL Code for Price Update

### 1. Weather Data Aggregation Function

#### Description
Aggregates weather data from a list of records, calculating the average temperature and humidity for each city while handling missing data.

#### Implementation
```python
def aggregate_weather_data(records):
    city_data = {}
    for record in records:
        city = record.get('city')
        temperature = record.get('temperature')
        humidity = record.get('humidity')

        if city not in city_data:
            city_data[city] = {'total_temp': 0, 'total_humidity': 0, 'count': 0}

        if temperature is not None:
            city_data[city]['total_temp'] += temperature
        if humidity is not None:
            city_data[city]['total_humidity'] += humidity
        
        city_data[city]['count'] += 1
         
    average_weather = {}
    for city, data in city_data.items():
        avg_temp = data['total_temp'] / data['count'] if data['count'] > 0 else None
        avg_humidity = data['total_humidity'] / data['count'] if data['count'] > 0 else None
        average_weather[city] = {
            'average_temperature': avg_temp,
            'average_humidity': avg_humidity
        }

    return average_weather
```
### 2. Prime Factorization Function

#### Description
Performs prime factorization on a given integer and returns a list of tuples containing each prime factor and its corresponding exponent.

#### Implementation
```python
def prime_factorization(n):
    factors = []
    c = 0
    
    while n % 2 == 0:
        n //= 2
        c += 1
        
    if c > 0:
        factors.append((2, c))
        
    for odd_factor in range(3, int(n**0.5) + 1, 2):
        count = 0
        while n % odd_factor == 0:
            n //= odd_factor
            count += 1
            
        if count > 0:
            factors.append((odd_factor, count))
            
    if n > 2:
        factors.append((n, 1))
        
    return factors
```
### 3. SQL Code for Price Update

#### Description
Creates a table named `products`, inserts sample product data, and updates the price of all products by increasing it by 10%.

#### Implementation
```sql
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);

INSERT INTO products VALUES 
(1, 'A', 1000.00),
(2, 'B', 500.00),
(3, 'C', 300.00),
(4, 'D', 150.00),
(5, 'E', 250.00);

UPDATE products 
SET price = price * 1.10;

SELECT name, price AS new_price 
FROM products;
```


## How to Run the Code(For Python)

1. Ensure you have Python installed on your machine (version 3.6 or higher).
2. Create a new Python file (e.g., `problem_1.py`) and copy the implementation code into it.
3. Open the terminal and write `python problem_1.py`
4. The code will execute

## How to Run the Code
1. Open your SQL database management tool (e.g., MySQL Workbench, PostgreSQL, etc.).
2. Create a new database (if needed) and select it.
3. Copy the SQL code provided above and paste it into the query editor.
4. Execute the SQL script to create the products table, insert data, update prices, and retrieve the new prices.

# Conclusion
Feel free to explore the functions and SQL code provided in this repository. They are designed to address common data manipulation tasks effectively while maintaining clarity and simplicity in code design.


