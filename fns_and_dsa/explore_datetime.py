from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formated_date = current_date.strftime("%Y-%m-%d %H:%M: %S")
    
    print("Current Date and time is:", formated_date)


def calculate_future_date(days):
    current_date = datetime.now()

    future_date = current_date + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

def main():
     display_current_datetime()
     try:
        days_input = int(input("Enter number of days to add: "))
        calculate_future_date(days_input)
     except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
