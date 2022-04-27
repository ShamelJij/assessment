initial_stock_level = int(input("Please enter the initial stock level: "))
number_months = int(input("Please enter the number of months: "))


# Initializing the range for the planned quantity
planned_sales_quantity = []
for number in range(number_months):
    value_for_month = int(input("Please enter the planned sales quantity for each month: "))
    planned_sales_quantity.append(value_for_month)

# Initializing the new_stock_level
new_stock_level = initial_stock_level
production_quantity = 0
for number in range(number_months):
    if number == 0:
        new_stock_level = initial_stock_level
        if planned_sales_quantity[number] < new_stock_level:
            production_quantity == 0
            new_stock_level = initial_stock_level - planned_sales_quantity[number]
        elif planned_sales_quantity[number] > new_stock_level:
            production_quantity -= new_stock_level
        print("new stock level: ", new_stock_level)
        print("production quantity = " , production_quantity)
    elif number > 0:
        production_quantity = planned_sales_quantity[number] - new_stock_level
        if planned_sales_quantity[number] < new_stock_level:
            production_quantity == 0
        elif planned_sales_quantity[number] > new_stock_level:
            production_quantity = planned_sales_quantity[number] - new_stock_level  
            new_stock_level = 0
        print("new stock level: ", new_stock_level)
        print("production quantity = " , production_quantity)