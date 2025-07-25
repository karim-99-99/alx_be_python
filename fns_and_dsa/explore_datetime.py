from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the result
    print("Current Date and Time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Prompt user for number of days
        add_days = int(input("Enter the number of days to add to the current date: "))
        
        # Create timedelta and add it to the current date
        future_date = datetime.now() + timedelta(days=add_days)
        
        # Print the future date in YYYY-MM-DD format
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Example usage
display_current_datetime()
calculate_future_date()
