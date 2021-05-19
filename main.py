"""How many months in the 20th century started on Tuesday?""" 

import datetime as dt  
import utils

current_year = 1901
current_month = 1 
total_days = 0
count = 0


while current_year<=2000: 
    total_days = utils.get_total_days(current_month)
    for i in range(1, total_days+1): 
        date  = dt.date(current_year, current_month, i)  
        day = date.strftime("%A")
        if day == "Tuesday": 
            count+=1
    if current_month==12: 
        current_year = utils.update_year(current_year)
        current_month = utils.update_month(current_month)
    else: 
        current_month = utils.update_month(current_month)
 
print(count)