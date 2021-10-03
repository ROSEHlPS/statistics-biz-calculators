#per 30 days
#program prints standard deviations

#NUMBER OF SALES PER DAY
entered_sales = input("Enter each sale per day, separated by a space: ").split()
sales = list(map(int,entered_sales))
#sales = [2, 10, 9, 4, 8, 1, 8, 7, 9, 6, 9, 5, 5]

#sales
#sales and orders
def print_sales(sales_input):
  for sale in sales_input:
    print (sale)

#def sales_sum(orders):
  #total = 0
  #for order in orders: 
    #total += order
  #return total
    
sales_sum = (sum(sales))
print ("Total number of sales made = ", sales_sum)

def sales_average(sales_input):
  average = sales_sum / float(len(sales_input))
  return average

print ("Average number of sales: ", sales_average(sales))

#how sales varied against the average
#large variance- differed
#small- majority were close to avg/similar

def sales_variance(orders):
  average = sales_average(orders)
  variance = 0
  for order in orders:
      variance += (average - order) ** 2
  return variance / len(orders)

print ("Variance of sales: ", sales_variance(sales))

def sales_std_deviation(variance):
  return variance ** 0.5

variance = sales_variance(sales)

print ("Standard deviation of number of sales: ", sales_std_deviation(variance))

#print (sales_sum(sales))
#print (sales_average(sales))
#print (sales_variance(sales))


#------------------------------
print ("------")

#VALUE OF EACH SALE'S TOTAL $$

entered_revenue = input("Enter the amount made per sale, separated by a space: ").split()
revenue = list(map(int,entered_revenue))

#sales
def print_revenues(revenue_input):
  for revenue in revenue_input:
    print (revenue)


def revenue_sum(profits):
  total = 0
  for profit in profits: 
    total += profit
  return total
    

print ("Total sum of profit made: ", revenue_sum(revenue))


def revenues_average(revenue_input):
  sum_of_revenues = revenue_sum(revenue_input)
  average = sum_of_revenues / float(len(revenue_input))
  return average


print ("Average profit made per day: ", (revenues_average(revenue)))

def revenues_variance(profits):
  average = revenues_average(profits)
  variance = 0
  for profit in profits:
      variance += (average - profit) ** 2
  return variance / len(profits)

print ("Revenue variance: ", revenues_variance(revenue))



#print (revenues_sum(revenue))
#print (revenues_average(revenue))
#print (revenues_variance(revenue))
#print (revenues_std_deviation(variance))

print ("-------------------------------")
#goal reevenue calculator
goal_profit = float(input("Enter Goal for this Month: "))
actual_profit = (revenue_sum(revenue))

if (goal_profit > actual_profit):
  revenue = goal_profit - actual_profit
  print ("Difference from goal = {0}".format(revenue))
elif (actual_profit > goal_profit):
  revenue = actual_profit - goal_profit
  print ("Met/Over goal = {0}".format(revenue))
else:
  print ("Met Goal")
