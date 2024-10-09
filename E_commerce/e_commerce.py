import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from mysql.connector import Error

# Optimized connection using context manager to ensure proper closure
with mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="8489",
        database="project") as connection:
    
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()
    
    # Optimize SQL by using SELECT queries with aggregation directly
    # Query customer data
    cursor.execute('SELECT * FROM customers_1')
    customer_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    # Query product data
    cursor.execute('SELECT * FROM products_1')
    product_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    # Query order data
    cursor.execute('SELECT * FROM orders_1')
    order_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

# Helper function to create bar charts
def plot_bar_chart(x, y, title, xlabel, ylabel, rotation=45, color='skyblue'):
    plt.figure(figsize=(10, 5))
    plt.bar(x, y, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.show()

# -------------- Customer Analysis ---------------- #
# Total number of customers city-wise (done using Pandas)
customers_citywise = customer_data.groupby('city').size().reset_index(name='total_customers')
print("Total number of customers city-wise:")
print(customers_citywise)
plot_bar_chart(customers_citywise['city'], customers_citywise['total_customers'],'Total Number of Customers City-wise', 'City', 'Number of Customers')

# -------------- Product Analysis ---------------- #
# Products with low stock levels (threshold: < 10 units)
low_stock_products = product_data[product_data['stock'] < 10]
print("\nProducts with low stock levels:")
print(low_stock_products)
plot_bar_chart(low_stock_products['product_name'], low_stock_products['stock'], 
               'Products with Low Stock Levels', 'Product Name', 'Stock Level', color='red')

# Price statistics using a single call to `.agg()`
price_stats = product_data['selling_price'].agg(['mean', 'max', 'min'])
print("\nProduct price statistics (average, max, min):")
print(price_stats)

# -------------- Order Analysis ---------------- #
# Most frequent customers (Top 10) based on order history
customer_order_count = order_data.groupby('customer_id').size().nlargest(10).reset_index(name='order_count')
print("Most frequent customers:")
print(customer_order_count)
plot_bar_chart(customer_order_count['customer_id'], customer_order_count['order_count'], 'Top 10 Most Frequent Customers', 'Customer ID', 'Order Count')

# Top 10 orders product-wise
print(order_data['total_price'].dtype)
order_data['total_price'] = pd.to_numeric(order_data['total_price'], errors='coerce')
order_data.dropna(subset=['total_price'], inplace=True)
top_10_orders = order_data.groupby('product_id')['total_price'].sum().nlargest(10).reset_index()
print("\nTop 10 orders product-wise:")
print(top_10_orders)
plot_bar_chart(top_10_orders['product_id'], top_10_orders['total_price'], 'Top 10 Orders Product-wise', 'Product ID', 'Total Price', color='green')

# -------------- Sales Analysis ---------------- #
# Merging only once for all category-based analysis
merged_data = pd.merge(order_data, product_data, on='product_id')

# Total revenue generated from orders product-wise
revenue_productwise = merged_data.groupby('product_id')['total_price'].sum().reset_index()
print("\nTotal revenue generated from orders product-wise:")
print(revenue_productwise)
plot_bar_chart(revenue_productwise['product_id'], revenue_productwise['total_price'], 'Revenue Generated Product-wise', 'Product ID', 'Total Revenue', color='purple')

# Total revenue by product category percentage
category_revenue = merged_data.groupby('category')['total_price'].sum()
category_revenue_percentage = (category_revenue / category_revenue.sum()) * 100
print("\nTotal revenue by product category (percentage):")
print(category_revenue_percentage)

# Pie Chart: Revenue by product category (percentage)
plt.figure(figsize=(8, 8))
plt.pie(category_revenue_percentage, labels=category_revenue.index, autopct='%1.1f%%', startangle=140)
plt.title('Revenue by Product Category (Percentage)')
plt.tight_layout()
plt.show()

# -------------- Time-based Analysis ---------------- #
# Month-wise total sales
order_data['order_date'] = pd.to_datetime(order_data['order_date'])
monthwise_sales = order_data.groupby(order_data['order_date'].dt.to_period('M'))['total_price'].sum().reset_index()
print("\nMonth-wise total sales:")
print(monthwise_sales)

# Line Chart: Month-wise total sales
plt.figure(figsize=(10, 5))
plt.plot(monthwise_sales['order_date'].astype(str), monthwise_sales['total_price'], marker='o', color='darkblue')
plt.title('Month-wise Total Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------- Customer Retention Analysis ---------------- #
# Analyzing repeat customers and their order patterns
repeat_customers = customer_order_count[customer_order_count['order_count'] > 1]
print("\nRepeat customers:")
print(repeat_customers)

# Customer retention rate as percentage
customer_retention_rate = (len(repeat_customers) / len(customer_data)) * 100
print("\nCustomer retention rate: {:.2f}%".format(customer_retention_rate))

# -------------- Payment Analysis ---------------- #
# Display successful and pending payments
payment_status_count = order_data['order_status'].value_counts().reset_index(name='count')
print("\nPayment status (successful, pending):")
print(payment_status_count)