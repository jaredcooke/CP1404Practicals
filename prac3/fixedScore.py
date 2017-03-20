def main():
    score = float(input("Enter score: "))
    text = calculate_grade(score)
    print(text)


def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

main()