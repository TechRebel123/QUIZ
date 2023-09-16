score = 0

name = input("YOUR NAME: ")
print("-------------------------")
print("GREAT LETS GOOOO", name)
print("-------------------------")

question1 = "1.How many planets are in the solar system?"
print(question1)
options = "A. 4", "B. 6", "C. 8", "D. none of the above"
for x in options:
    print(x)
print("------------------")
answer = input("Enter A, B, C, D: ").upper()

if answer=="C":
    print("--------------------")
    print("Correct Answer")
    print("--------------------")
    score += 1
else:
    print("--------------------")
    print("INCORRECT")
    print("--------------------")




question2 = "2. How many stars are in the universe?"
print(question2)
options = "A. 4", "B. 6", "C. 8", "D. none of the above"
for x in options:
    print(x)
print("------------------")
answer = input("Enter A, B, C, D: ").upper()

if answer=="D":
    print("--------------------")
    print("Correct Answer")
    print("--------------------")
    score += 1
else:
    print("--------------------")
    print("INCORRECT")
    print("--------------------")



question3 = "3. Which school are u studying in?"
print(question3)
options = "A. OXFORD", "B. MVJ", "C. KNCS", "D. none of the above"
for x in options:
    print(x)
print("------------------")
answer = input("Enter A, B, C, D: ").upper()

if answer=="C":
    print("--------------------")
    print("Correct Answer")
    print("--------------------")
    score += 1
else:
    print("--------------------")
    print("INCORRECT")
    print("--------------------")



question4 = "4. what is the name of the creator of this quiz?"
print(question4)
options = "A. GOVERNMENT", "B. LIKITH", "C. DONALD TRUMP", "D. none of the above"
for x in options:
    print(x)
print("------------------")
answer = input("Enter A, B, C, D: ").upper()

if answer=="B":
    print("--------------------")
    print("Correct Answer")
    print("--------------------")
    score += 1
else:
    print("--------------------")
    print("INCORRECT")
    print("--------------------")

question5 = "5. Is the Sky Blue?"
print(question5)
options = "A. Yes", "B. No", "C. Maybe", "D. none of the above"
for x in options:
    print(x)
print("------------------")
answer = input("Enter A, B, C, D: ").upper()

if answer=="A":
    print("--------------------")
    print("Correct Answer")
    print("--------------------")
    score += 1
else:
    print("--------------------")
    print("INCORRECT")
    print("--------------------")

questions = question1, question2, question3, question4, question5

total_score = "YOUR PERCENTAGE:", score / len(questions) * 100
for i in total_score:
    print(i)

print("GOODBYE!")