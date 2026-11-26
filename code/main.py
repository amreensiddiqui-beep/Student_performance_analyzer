import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------
# 1. Load Student Dataset
# --------------------------------

try:
    df = pd.read_csv(
        "students.csv",
        header=None,
        names=["Name", "Maths", "Physics", "Chemistry"],
        dtype=str,
        keep_default_na=False,
        on_bad_lines="skip"
    )
except FileNotFoundError:
    print("Error: students.csv file not found!")
    exit()


# --------------------------------
# 2. Validate Student Marks
# --------------------------------

valid_students = []

for index, row in df.iterrows():

    name = row["Name"].strip()

    if not name:
        continue

    valid = True
    marks = []

    subjects = ["Maths", "Physics", "Chemistry"]

    for subject in subjects:

        value = row[subject].strip()

        try:
            mark = float(value)

            if not 0 <= mark <= 100:
                raise ValueError

            marks.append(mark)

        except ValueError:
            print(
                f"Invalid marks for {name} in {subject}: "
                f"'{value}'. Row skipped."
            )
            valid = False
            break

    if valid:
        valid_students.append([name] + marks)


# --------------------------------
# 3. Create DataFrame
# --------------------------------

if not valid_students:
    print("No valid student records found!")
    exit()

data = pd.DataFrame(
    valid_students,
    columns=["Name", "Maths", "Physics", "Chemistry"]
)


# --------------------------------
# 4. Calculate Total and Percentage
# --------------------------------

subjects = ["Maths", "Physics", "Chemistry"]

data["Total"] = data[subjects].sum(axis=1)

data["Percentage"] = (data["Total"] / 300) * 100


# --------------------------------
# 5. Calculate Grades
# --------------------------------

def calculate_grade(percentage):

    if percentage >= 90:
        return "A"

    elif percentage >= 75:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 40:
        return "D"

    else:
        return "F"


data["Grade"] = data["Percentage"].apply(calculate_grade)


# --------------------------------
# 6. Display Student Results
# --------------------------------

def display_results():

    print("\n========== STUDENT RESULTS ==========")

    for index, row in data.iterrows():

        print(
            f"{row['Name']} | "
            f"{row['Total']:.0f} | "
            f"{row['Percentage']:.2f}% | "
            f"{row['Grade']}"
        )


# --------------------------------
# 7. Display Class Statistics
# --------------------------------

def display_statistics():

    percentages = data["Percentage"]

    mean = np.mean(percentages)
    median = np.median(percentages)

    # Population standard deviation
    std_dev = np.std(percentages)

    topper = data.loc[data["Percentage"].idxmax()]

    print("\n========== CLASS STATISTICS ==========")

    print(f"Mean %: {mean:.2f}")
    print(f"Median %: {median:.2f}")
    print(f"Std Dev: {std_dev:.2f}")

    print(
        f"Topper: {topper['Name']} "
        f"({topper['Percentage']:.2f}%)"
    )

    print("\nSubject Averages:")

    for subject in subjects:

        average = data[subject].mean()

        print(f"{subject}: {average:.2f}")


# --------------------------------
# 8. Display Charts
# --------------------------------

def display_charts():

    # Bar Chart: Subject-wise Average

    averages = data[subjects].mean()

    plt.figure(figsize=(8, 5))

    plt.bar(averages.index, averages.values)

    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()


    # Histogram: Student Percentages

    plt.figure(figsize=(8, 5))

    plt.hist(
        data["Percentage"],
        bins=5,
        edgecolor="black"
    )

    plt.title("Distribution of Student Percentages")
    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# --------------------------------
# 9. Main Menu
# --------------------------------

while True:

    print("\n========== STUDENT PERFORMANCE ANALYZER ==========")

    print("1. Display Student Results")
    print("2. Display Statistics and Charts")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        display_results()

    elif choice == "2":

        display_statistics()
        display_charts()

    elif choice == "3":

        print("Thank you for using Student Performance Analyzer!")
        break

    else:

        print("Invalid choice! Please try again.")