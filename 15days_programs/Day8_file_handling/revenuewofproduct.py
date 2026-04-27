import csv

product_name = input("Enter the product name to calculate revenue for: ")
total_revenue = 0.0

with open("product.csv","r") as file:
    reader = csv.DictReader(file)

        for row in reader:
        print(row)
        if row['Product'] == product_name:  #lets take phone(product) quantity is and price is 5000 per unit
            # Calculate revenue for this row
            quantity = float(row['Quantity'])
            price = float(row['Price'])
            total_revenue += quantity * price #revenue is 3 * 5000 = 15000

print(f"Total sales revenue for '{product_name}': ${total_revenue:.2f}")