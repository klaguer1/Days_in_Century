day_amount = {31:[1, 3, 5, 7, 8, 10, 12], 28:[2], 30:[4, 6, 9, 11]}

def update_month(month):
    if month==12: 
        month=1 
    else: 
        month+=1 

    return month 

def update_year(year): 
    year+=1 

    return year  

def get_total_days(current_month):
    for day, months in day_amount.items():
        if current_month in months:
            total_days=day   
        
    return total_days
