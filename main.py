Ron_points = 0
Hermione_points = 0
Neville_points = 0

questions = {
    "If you have 10 min before a test, what do you do?":
        ["study", "just relax", "panic"],
    "If a teacher asks a question and you know the answer, what do you do?":
        ["Raise your hand", "Hide and hope no one notices you",
            "There was a question?"],
    "What is your prefered dessert?": ["Chocolate", "Ice cream", "Cookie"]
}


for question, answers in questions.items():
    print(question)
    answer_number = 1
    for answer in answers:
        print(str(answer_number) + "." + answer)
        answer_number += 1

    print("")
    Selection = input("Choose your answer ")
    while (Selection != "1" and Selection != "2" and Selection != "3"):
            Selection = input("Invalid answer, try again ")
    if Selection == "1":
        Hermione_points += 1
    elif Selection == "2":
        Ron_points += 1
    elif Selection == "3":
        Neville_points += 1
    else:
        print("Invalid answer, try again")
if Ron_points > Hermione_points and Ron_points > Neville_points:
    print("You are more like Ron")
elif Hermione_points > Ron_points and Hermione_points > Neville_points:
    print("You are more like Hermione")
elif Neville_points > Hermione_points and Neville_points > Hermione_points:
    print("You are more like Neville")
elif Hermione_points == Ron_points == Neville_points:
    print("You are similar to all three characters")