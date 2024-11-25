#the nile

# logistic company software to calculate deliverys cost
import math
SHIPPING_PRICES = {
  'Ground': 1,
  'Priority': 1.6,
  'Overnight': 2.3,
}
class Driver:
  def __init__(self, speed, salary):
    self.speed = speed
    self.salary = salary
    

  def __repr__(self):
    return "Nile Driver speed {} salary {}".format(self.speed, self.salary)

driver1 = Driver(4, 10)
driver2 = Driver(7, 20)

class Trip:
  def __init__(self, cost, driver, driver_cost):
    self.cost = cost
    driver.cost = driver_cost
    self.driver = driver

trip1 = Trip(200, driver1, 15)
trip2 = Trip(300, driver2, 40)

def calculate_shipping_cost(from_coords, to_coords, shipping_type = "Overnight"):
    from_lat = from_coords[0]
    from_long = from_coords[1]
    to_lat = to_coords[0]
    to_long = to_coords[1]
    def get_distance(from_lat, from_long, to_lat, to_long):
        distance = math.sqrt((abs(from_lat - to_lat)) ** 2 + (abs(from_long - to_long)) ** 2)
        return distance
    distance = get_distance(from_lat, from_long, to_lat, to_long)

    def shipping_rate(shipping_type):
        if shipping_type in SHIPPING_PRICES:
            rate = SHIPPING_PRICES[shipping_type]
            cost = rate * distance 
            return cost
    cost = shipping_rate(shipping_type)
    return distance, cost 
print(calculate_shipping_cost([1,2],[3,4]))

def calculate_driver_cost(distance, drivers):
    cheapest_driver = None
    cheapest_driver_price = None
    for driver in drivers:
        driver_time = distance / driver.speed 
        driver_for_price = driver.salary * driver_time
        if cheapest_driver == None:
           cheapest_driver = driver
           cheapest_driver_price = driver_for_price
        
        elif driver_for_price < cheapest_driver:
           cheapest_driver = driver
           cheapest_driver_price = driver_for_price
    return cheapest_driver, cheapest_driver_price

def calculate_money(**trips):
   total_money_made = 0
   for trip in trips:
      trip_revenue = trip.cost - trip.driver.cost
      total_money_made += trip_revenue
   return total_money_made
def test_function(fn):
  if fn.__name__ == "calculate_shipping_cost":
    test_shipping(fn)
  if fn.__name__ == "calculate_driver_cost":
    test_driver(fn)
  if fn.__name__ == "calculate_money_made":
    test_money(fn)

def test_shipping(f):
  try:
    costs = f((0, 0), (1, 1))
  except TypeError:
    print("calculate_shipping_cost() did not provide default argument for shipping_type")
    return
  if not type(costs) is str:
    print("calculate_shipping_cost() did not format the result in a string")
    return
  if costs != "$1.04":
    print("calculate_shipping_cost((0, 0), (1, 1)) returned {}. Expected result is {}".format(costs, "$1.04"))
    return
  print("OK! calculate_shipping_cost() passes tests")

def test_driver(f):
  try:
    price, driver = f(80, driver1, driver2)
  except TypeError:
    print("calculate_driver_cost() doesn't expect multiple driver arguments")
    return
  if type(driver) is not Driver:
    print("calculate_driver_cost() did not return driver")
    return
  if price != 200:
    print("calculate_driver_cost() did not provide correct final price (expected {}, received {})".format(200,price))
    return
  if driver is not driver1:
    print("calculate_driver_cost() did not provide least expensive driver")
    return
  print("OK! calculate_driver_cost() passes tests")

def test_money(f):
  try:
    money = f(UEXODI=trip1, DEFZXIE=trip2)
  except TypeError:
    print("calculate_money_made() doesn't expect multiple trip keyword arguments")
    return
  if type(money) not in (int, float):
    print("calculate_driver_cost() did not return a number")
    return
  if money != 445:
    print("calculate_driver_cost() did not provide correct final price (expected {}, received {})".format(445, money))
    return
  print("OK! calculate_money_made() passes tests")
test_money(calculate_money)