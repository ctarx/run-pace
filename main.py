LINES = "-" * 60

print(LINES)
print("\t \t Running Pace Calculator")
print(f"{LINES} \n")

# Get and validate distance choice
choice = int(
    input(
        "Pick your distance: \n\n (1) 5km | (2) 10km | (3) 1/2 Marathon | (4) Marathon \n\n : "
    )
)

# Assign distance based on user choice
if choice == 1:
    distance = 5
elif choice == 2:
    distance = 10
elif choice == 3:
    distance = 21.097
elif choice == 4:
    distance = 42.195
else:
    print(LINES)
    print("Wrong Value. Pick 1-4")
    print(LINES)
    exit()  # Exit the program if an invalid choice is made


# Function to convert time (hh:mm:ss) to seconds
def seconds(time):
    h, m, s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


# Function to calculate running pace
def pace_calculate(distance):
    print()
    time = seconds(input("Give the finishing time (hh:mm:ss) \n\n : "))
    # Calculate pace (time / distance)
    pace = time / distance
    # divmod returns a tuple with the quotient and remainder (minutes and seconds)
    mm, ss = divmod(int(pace), 60)

    print()
    print(LINES)
    print(f"Your running pace is: {mm}:{ss:02d} min/km")
    print(LINES)


# Call the pace calculation function
pace_calculate(distance)
