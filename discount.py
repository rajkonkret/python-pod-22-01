from datetime import date, timedelta, datetime

today = date.today()
print(today)
time = datetime.now()
print(time)
# 2024-01-23
# 2024-01-23 15:30:06.068682
print(type(time))  # <class 'datetime.datetime'>
# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-01-24

print(time.time())
print(today.day)
# 15:32:47.161620
# 23

formatted_date = datetime.now().strftime('%d/%m/%Y')
print(formatted_date)  # 23/01/2024

# 14:16
formated_time = datetime.now().strftime('%H:%M')
print(formated_time)  # 15:36
print(formated_time.removeprefix("0"))

formated_date_12h = datetime.now().strftime('%I:%M %p')
print(formated_date_12h)  # 03:39 PM
print(formated_date_12h.removeprefix("0"))  # 3:39 PM

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 50.0},
    {'sku': 3, 'exp_date': today, 'price': 250.0},
    {'sku': 4, 'exp_date': today, 'price': 90},
]

# print(products)
for p in products:
    # print(p)
    if p['exp_date'] != today:
        continue
    p['price'] *= 0.8
    print(f"""
Price for sku {p['sku']}
is now {p['price']}""")

# Price for sku 1
# is now 80.0
#
# Price for sku 3
# is now 200.0
#
# Price for sku 4
# is now 72.0
