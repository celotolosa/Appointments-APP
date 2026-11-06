appointment_list = []


def appointment_creation(user_input: str):
    user_input = input("What type of appointment would you like to schedule?\nTaper - T\nFade - F\nScissor Cut - S\nCustom - C\n")
    name = ""
    month = 0
    day = 0
    year = 0
    time = 0
    cut_type = ""

    if user_input == 'T':
        name = input("Enter your name: ")
        month = input("Enter month (e.g; April = 04): ")
        day = input("Enter day: ")
        year = input("Enter year: ")
        cut_type = "Taper"
    elif user_input == 'F':
        name = input("Enter your name: ")
        month = input("Enter month (e.g; April = 04): ")
        day = input("Enter day: ")
        year = input("Enter year: ")
        cut_type = "Fade"
    elif user_input == 'S':
        name = input("Enter your name: ")
        month = input("Enter month (e.g; April = 04): ")
        day = input("Enter day: ")
        year = input("Enter year: ")
        cut_type = "Scissor Cut"
    elif user_input == 'C':
        name = input("Enter your name: ")
        month = input("Enter month (e.g; April = 04): ")
        day = input("Enter day: ")
        year = input("Enter year: ")
        cut_type = "Custom"

    date = (month, day, year)
    appointment_data = (name, date, time, cut_type)
    appointment_list.append(appointment_data)

    print(appointment_list)