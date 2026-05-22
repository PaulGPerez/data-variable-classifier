
print("Welcome to the Variable Category Sorter\n")
print("Please classify your variable: Categorical (Nominal/Ordinal) or Numerical (Discrete/Continuous).\n")
print("Is your variable numerical or text based?\n" )
print("1: Numerical\n")
print("2: Text\n")

answer_1 = input("Enter your choice by selecting 1 or 2: ").strip()

if answer_1 == "1":
    print("\nAre your numbers whole numbers or do they have decimals?\n")
    print("1: whole numbers\n")
    print("2: have decimals\n")
    answer_2 = input("Enter your choice by selecting 1 or 2:").strip()

    if answer_2 == "1":

        print("\nClassification: Numerical (Discrete)\n")
        print("\nRecommended Charts: Bar Chart, Histogram\n")
    elif answer_2 == "2":

        print("\nClassification: Numerical (Continuous)\n")
        print("\nRecommended Charts: Histogram, Box Plot\n")
    else:
        print("\nInvalid input. Please restart the program.")

elif answer_1 == "2":
    print("\nDoes your variable have ranking order like 1-5 stars or small/big or have no order such as movie names or colors?\n")
    print("1: Has ranking/logical order\n")
    print("2: Does not have order\n")
    answer_3 = input("Enter your choice by selecting 1 or 2:").strip()

    if answer_3 == "1":

        print("\nClassification: Categorical (Ordinal)\n")
        print("Recommended Charts: Bar Chart")
    elif answer_3 == "2":

        print("\nClassification: Categorical (Nominal)\n")
        print("Recommended Charts: Bar Chart, Pareto Chart")
    else:
        print("\nInvalid input. Please restart the program.")
else:
    print("\nInvalid input. Please restart the program.")