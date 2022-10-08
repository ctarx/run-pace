print()
print("----------" * 6)
print("\t \t Running Pace Calculator")
print("----------" * 6)
print()

distance = float(
    input(
        "Pick your distance: \n\n (1) 5km | (2) 10km | (3) 1/2 Marathon | (4) Marathon "
    )
)

# Convert hh:mm:ss to seconds
def seconds(time):
    h, m, s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def pace_calculate(distance):
    print()
    time = seconds(input("Give the finishing time (hh:mm:ss) "))
    # calculate time / distance
    pace = int(time / distance)
    # mm = pace // 60
    # ss = pace % 60
    # divmod returns a tuple that contains the quotient and remainder
    mm, ss = divmod(pace, 60)

    print()
    print("----------" * 6)
    print(f"Your running pace is: {mm}:{ss} min/km")
    print("----------" * 6)

if distance == 1:
    # distance = 5
    pace_calculate(5)
elif distance == 2:
    # distance = 10
    pace_calculate(10)
elif distance == 3:
    # distance = 21.097
    pace_calculate(21.097)
elif distance == 4:
    # distance = 42.195
    pace_calculate(42.195)
else:
    print("Wrong Value.")
