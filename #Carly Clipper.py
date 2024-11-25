#Carly Clipper

hairstyle = ["a", "b", "c", " d"]
prices = [10, 15 ,20, 40]
las_week_purchases = [1, 2, 3, 4]

total_price = 0
total_revenue = 0

for price in prices:
    total_price += price

avarege_price = total_price / len(prices)
print("Average Haircut Price: %s" %avarege_price)

new_prices = [price - 5 for price in prices]
print(new_prices)

for i in range(len(hairstyle)):
    total_revenue += prices[i] * las_week_purchases[i] 
print("Total Revenue: %s " %total_revenue)

average_daily_revenue = total_revenue / 7
cuts_under_30 = []
# for i in range(len(hairstyle)):
#     if new_prices[i] < 30:
#         cuts_under_30.append(hairstyle[i])
cuts_under_30 = [hairstyle[i] for i in range(len(hairstyle)) if new_prices[i] < 30]

print(cuts_under_30)