student_names = ["Juan", "Maria", "Joseph"]
student_scores = [70, 90, 81]
highest = 0

print("Student Records:")
for name, score in zip(student_names, student_scores):
    print(f"Record: {name} scored {score} in the exam.")

    if score > highest:
        highest = score

print(f"Highest score is {highest}")