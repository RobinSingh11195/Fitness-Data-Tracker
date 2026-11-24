# Fitness Data Tracker
# PS No. 77
# Python 3

import matplotlib.pyplot as plt

# Lists used to store daily fitness records
steps_list = []
calories_list = []

DAILY_STEP_GOAL = 10000


def get_non_negative_number(message):
    """Read a non-negative whole number from the user."""
    value = input(message)

    try:
        number = int(value)
        if number < 0:
            return None
        return number
    except ValueError:
        return None


def add_record():
    """Take steps and calories and save one daily record."""
    steps = get_non_negative_number("Enter steps: ")

    if steps is None:
        print("Invalid steps. Enter a non-negative whole number.")
        print("Record not saved.")
        return

    calories = get_non_negative_number("Enter calories: ")

    if calories is None:
        print("Invalid calories. Enter a non-negative whole number.")
        print("Record not saved.")
        return

    steps_list.append(steps)
    calories_list.append(calories)

    day_number = len(steps_list)
    goal_percentage = (steps / DAILY_STEP_GOAL) * 100

    print(f"Record saved for Day {day_number}.")
    if steps >= DAILY_STEP_GOAL:
        print("Goal achieved: Yes")
    else:
        print("Goal achieved: No")

    print(f"({goal_percentage:.2f}% of goal)")


def calculate_average_steps():
    """Return the average number of steps recorded."""
    if len(steps_list) == 0:
        return 0
    return sum(steps_list) / len(steps_list)


def calculate_total_calories():
    """Return the total calories burned."""
    return sum(calories_list)


def find_best_day():
    """Return the day number and steps for the highest step count."""
    if len(steps_list) == 0:
        return None, 0

    best_steps = max(steps_list)
    best_day = steps_list.index(best_steps) + 1
    return best_day, best_steps


def display_summary():
    """Display the fitness summary for all saved records."""
    if len(steps_list) == 0:
        print("No fitness records available. Add a record first.")
        return

    average_steps = calculate_average_steps()
    total_calories = calculate_total_calories()
    best_day, best_steps = find_best_day()

    goal_days = 0
    for steps in steps_list:
        if steps >= DAILY_STEP_GOAL:
            goal_days += 1

    print("\n----- FITNESS SUMMARY -----")
    print(f"Average steps: {average_steps:.2f}")
    print(f"Total calories: {total_calories}")
    print(f"Best day: Day {best_day} ({best_steps} steps)")
    print(f"Goal days: {goal_days}/{len(steps_list)}")


def calculate_bmi(weight, height):
    """Calculate BMI and return its category."""
    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


def bmi_calculator():
    """Take weight and height and display BMI."""
    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in metres: "))

        if weight <= 0 or height <= 0:
            print("Invalid input. Weight and height must be positive.")
            return

        bmi, category = calculate_bmi(weight, height)
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Enter numeric values for weight and height.")


def show_chart():
    """Display a bar chart of daily steps with the goal line."""
    if len(steps_list) == 0:
        print("No fitness records available to display.")
        return

    days = []
    for i in range(len(steps_list)):
        days.append(f"Day {i + 1}")

    plt.figure(figsize=(9, 5))
    bars = plt.bar(days, steps_list, label="Daily Steps")
    plt.axhline(
        y=DAILY_STEP_GOAL,
        linestyle="--",
        linewidth=2,
        label="10,000 Step Goal"
    )

    # Show the step count above each bar.
    for bar, steps in zip(bars, steps_list):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{steps:,}",
            ha="center",
            va="bottom"
        )

    plt.title("Daily Steps")
    plt.xlabel("Days")
    plt.ylabel("Number of Steps")
    plt.grid(axis="y", linestyle=":", alpha=0.5)
    plt.ylim(0, max(max(steps_list), DAILY_STEP_GOAL) * 1.15)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    """Display the menu and run the selected operation."""
    while True:
        print("\n===== FITNESS DATA TRACKER =====")
        print("1. Add Record")
        print("2. Summary")
        print("3. BMI")
        print("4. Chart")
        print("0. Exit")

        choice = input("Enter menu option: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            bmi_calculator()
        elif choice == "4":
            show_chart()
        elif choice == "0":
            print("Thank you for using Fitness Data Tracker.")
            break
        else:
            print("Invalid menu option. Please choose 0 to 4.")


if __name__ == "__main__":
    main()
