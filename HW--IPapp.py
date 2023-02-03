import requests

from os import system
system ("cls")

# HW: make it interactive + exit option

while True:
    
    query = input ("Enter a domain or Ip address:")
    url = f"http://ip-api.com/json/{query}" #enter for ex: fort.md


    response = requests.get(url) 
    data = response.json()    
    if data ['status'] == 'success':
            print (data ['country'])
            print (data ['isp'])
    else:
            print('Not found')

    app = input ("Would you like to continue?:")
    if app == "Yes":
        print ()
    elif app == "No":
        print ("See you next time")
        break 
    else:
        print("Error")
        