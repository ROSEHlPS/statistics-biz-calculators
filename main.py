#per 30 days
#program prints standard deviations

#daily

#sales per day, each interval is one day of the month
sales = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#sales
#sales and orders
def print_sales(sales_input):
  for sale in sales_input:
    print (sale)

def sales_sum(orders):
  total = 0
  for order in orders: 
    total += order
  return total
    
def sales_average(sales_input):
  sum_of_sales = sales_sum(sales_input)
  average = sum_of_sales / float(len(sales_input))
  return average


#how sales varied against the average
#large variance- differed
#small- majority were close to avg/similar

def sales_variance(orders):
  average = sales_average(orders)
  variance = 0
  for order in orders:
      variance += (average - order) ** 2
  return variance / len(orders)

def sales_std_deviation(variance):
  return variance ** 0.5

variance = sales_variance(sales)


print (sales_sum(sales))
print (sales_average(sales))
print (sales_variance(sales))
print (sales_std_deviation(variance))

#------------------------------

#change variables so it fits the shop

#profit, earnings
#revenue


#net income
#change variables
#sale--> revenue (amount made per sale)
#scores--> profit (individual sale amount)

#amount totaled revenue per day of the month

revenue = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#sales
def print_revenues(revenues_input):
  for revenue in revenues_input:
    print (revenue)

def revenues_sum(profits):
  total = 0
  for profit in profits: 
    total += profit
  return total
    
def revenues_average(revenues_input):
  sum_of_revenues = revenues_sum(revenues_input)
  average = sum_of_revenues / float(len(revenues_input))
  return average

def revenues_variance(profits):
  average = revenues_average(profits)
  variance = 0
  for profit in profits:
      variance += (average - profit) ** 2
  return variance / len(profits)


def revenues_std_deviation(variance):
  return variance ** 0.5

variance = revenues_variance(revenue)


print (revenues_sum(revenue))
print (revenues_average(revenue))
print (revenues_variance(revenue))
print (revenues_std_deviation(variance))

#-------------------------------
#goal reevenue calculator
goal_profit = float(input("Enter Goal for this Month: "))
actual_profit = (revenues_sum(revenue))

if (goal_profit > actual_profit):
  revenue = goal_profit - actual_profit
  print ("Difference from goal = {0}".format(revenue))
elif (actual_profit > goal_profit):
  revenue = actual_profit - goal_profit
  print ("Met/Over goal = {0}".format(revenue))
else:
  print ("Met Goal")