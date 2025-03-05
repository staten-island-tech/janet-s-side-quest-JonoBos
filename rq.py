""" temperatures = ["Label", 32, 50, 77, 104]
celc= list(map(lambda f: (f-32)*5/9,temperatures[2:]))
print (celc) """

def calcRow(data):
    row_totals = {}

    for row in data[1:]:  # Skipping the first row
        store_name = row[0]  # First column is the store name
        sales = map(int, row[1:])  # Convert sales to numbers
        row_totals[store_name] = sum(sales)  # Sum up sales for the store

    return row_totals

# Example Data
sales_data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

totals = calcRow(sales_data)
print(totals)