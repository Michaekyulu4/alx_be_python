from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date


def calculate_future_date(days):
    current_date = datetime.now()

    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

def main():

     print("Current Date and time is:", display_current_datetime())
     try:
        days_input = int(input("Enter number of days to add to the current date: "))
        print("Future Date:", calculate_future_date(days_input))
     except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
