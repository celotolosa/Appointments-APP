appointment_list = []
available_dates_list = []

def appointment_creation(user_input: str):
    current_date = ""
    name = input("Please enter your name: ")
    month = 0
    day = 0
    year = 0 
    cut_type = ""
    time = ""

    date = (month, day, year)
    data = (name, date, time, cut_type)
    

    try:
        if len(available_dates_list) == 0:
            return
        
        for chosen_day in available_dates_list:
            print(chosen_day)
            
        chosen_date = input("Please select date for appointment from the list above:")    
        if chosen_date in available_dates_list:
            current_date = chosen_date
    
    except Exception as e:
        print("ERORR", e)

def fetch_dates():
    password = input("Please enter password:\n")

    if password != '1447':
        return
    
    available_dates = input("Please enter your current availabilities: (11/6 for November 6)\n")
    dates = available_dates.split()

    for date in dates:
        if date in available_dates_list:
            print(f"Your selection, {date} is already in the list")
        else:
            available_dates_list.append(date)
    
    
    print(available_dates_list)

    