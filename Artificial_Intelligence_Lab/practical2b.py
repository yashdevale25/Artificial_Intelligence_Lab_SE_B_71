sub1 = input("Enter subject 1: ")
sub2 = input("Enter subject 2: ")

if sub1 == "Maths" and sub2 == "Physics":
    print("Mechanical Engineering")
elif sub1 == "Programming" and sub2 == "Maths":
    print("Computer Engineering")
elif sub1 == "Biology" and sub2 == "Chemistry":
    print("Biotechnology")
elif sub1 == "Circuits" and sub2 == "Maths":
    print("Electronics Engineering")
elif sub1 == "Programming" and sub2 == "Statistics":
    print("Artificial Intelligence and Data Science")
elif sub1 == "Programming" and sub2 == "AI Concepts":
    print("Artificial Intelligence and Machine Learning Engineering")
else:
    print("Invalid combination of subjects")
