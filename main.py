import handle_appointment as app
import handle_review as review


def main():
    while True:
        user_input = input('Welcome to the appointment app!\nWhat would you like to do?\nSchedule an appointment - A\nLeave a review - R\nQuit - Q\n')

        try:
            if user_input == 'A':
                app.appointment_creation(user_input)
            elif user_input == 'R':
                review.review_creation(user_input)
            elif user_input == 'Q':
                return
        except Exception as e:
            print("ERROR wrong input", e)

if __name__ == '__main__':
    main()