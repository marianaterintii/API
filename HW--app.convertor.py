import requests
from os import system
system ("cls")

date = "02.02.2023"
url = f"https://www.bnm.md/ro/export-official-exchange-rates?date={date}"

res = requests.get(url)
data = res.text

lines = data.split("\r\n") # trecere din rind nou "\n"
usd_rate = 0.0
eur_rate = 0.0
for l in lines [3: -5]: # sublist [startindex: endindex]
    currency = l.split(";")
    if currency[2] == "USD":
        usd_rate = float ( currency[4].replace(",", "."))
    if currency[2] == "EUR":
        eur_rate = float ( currency[4].replace(",", "."))
    #print (currency)

print ("USD:", usd_rate)
print ("EUR:", eur_rate)

# HW: add intereactivity

while True:
    source_currency = input("Choose source currency USD/EUR/MDL >>")
    user_amount = int( input("Amount?>>"))
    destination_currency = input("Choose destination currency USD/EUR/MDL>> ")
    if source_currency == "USD" and destination_currency == "MDL":
        exchanged_amount =  user_amount * usd_rate
        print (exchanged_amount)
    elif source_currency == "EUR" and destination_currency == "MDL":
        exchanged_amount =  user_amount * eur_rate
        print (exchanged_amount)
    elif source_currency == "MDL" and destination_currency == "USD":
        exchanged_amount =  user_amount / usd_rate
        print (exchanged_amount)
    elif source_currency == "MDL" and destination_currency == "EUR":
        exchanged_amount =  user_amount / eur_rate
        print (exchanged_amount)
    else:
        print("Error")

    app = input ("Would you like to continue?:")
   
    if app == "Yes":
        print ()
    elif app == "No":
        print ("See you next time")
        break 
    else:
        print("Error")
