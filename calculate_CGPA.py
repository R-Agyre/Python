def calculate_gpa():
    grade_dict = {"A": 5, "B": 4, "C": 3, "D": 2, "F": 0}
    total_units = 0
    total_points = 0

    for i in range(1, 7):  # For 6 courses
        unit = int(input(f"How many units was course {i}? "))
        grade = input(f"What was your grade for course {i}? ").strip().upper()

        if grade not in grade_dict:
            print("Invalid grade entered. Please use A, B, C, D, or F.")
            return

        total_units += unit
        total_points += grade_dict[grade] * unit

    gpa = total_points / total_units
    print("Your GPA is:", round(gpa, 2))