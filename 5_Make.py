
''' 
Tatum Massengill
Exceptions Homework


This code defines the steps_to_miles() function that converts steps to miles (2000 steps= 1 mile) and raises an errorvalue if input is negative. 
The main() function reads user input, converts it to miles using previous function and prints result with 2 decimal places if successful and gives error message if number is negative.
This code was made to  be interactive.
'''
def steps_to_miles(steps):
    if steps < 0:
        raise ValueError ("Exception: Negative step count entered.")
    return steps / 2000

def main():
    print("Step-to-mile Converter")
    print("(2000 steps = 1 mile)")
    
    while True:
        try:
            steps = int(input("Enter number of steps you've taken today: "))
            miles = steps_to_miles(steps)
            print(f"\nYou've walked {miles:.2f} miles today! \n")
            break
        except ValueError as e:
            if "Negative" in str(e):
                print("\nEror:", e)
                print("Please enter positive number. \n")
            else:
                print("\nError: Please enter a valid number. \n")

if __name__ == "__main__":
    main()
