def calculate_average_score(test1, test2, test3):
    return (test1 + test2 + test3) / 3

def calculate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    try:
        test1 = float(input("Enter score for test 1: "))
        test2 = float(input("Enter score for test 2: "))
        test3 = float(input("Enter score for test 3: "))

        average_score = calculate_average_score(test1, test2, test3)
        grade = calculate_grade(average_score)

        print(f"Average score: {average_score:.2f}")
        print(f"Grade: {grade}")

    except ValueError:
        print("Invalid input. Please enter numeric scores.")

if __name__ == "__main__":
    main()

