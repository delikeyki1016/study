import sys

total_price = int(sys.stdin.readline())
buy_item = int(sys.stdin.readline())
middle_price = 0
for _ in range(buy_item):
    price, quantity = sys.stdin.readline().split()
    item_price = int(price) * int(quantity)
    middle_price += item_price
if total_price == middle_price:
    print("Yes")
else:
    print("No")
