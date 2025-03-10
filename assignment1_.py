def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)
""" print(data)  # Output the list """

def calcRow(data):
    row_totals = {}

    for row in data[1:]:  # Skipping the first row
        store_name = row[0]  # First column is the store name
        sales = list(map(int, row[1:]))  # Convert sales to numbers
        row_totals[store_name] = round(sum(sales) / len(sales),2)  # Sum up sales for the store and divides by number of days

    return row_totals

totals = calcRow(data)

y = dict(sorted(totals.items(), key=lambda x: x[1:], reverse = True)) 
""" print (y)   """

""" z = sum(y.values())
print (z/10) """

all_added = sum(y.values())
fil_3 = (all_added/10)



for location in y:
    if int(y[location]) < 0.8 * fil_3:
        print (location)


    

