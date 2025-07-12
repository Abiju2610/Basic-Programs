import random

quiz_qs = {"What is the value of pi to 2 decimal places?" : "3.14",
           "What is the capital of the UK?" : "London",
           "What is the largest country in the world?" : "Russia"}

"""
quizListKeys = []

point = 0

for i in quiz_qs.keys():
    quizListKeys.append(i)



def genQuestion():
    return quizListKeys[random.randint(0, len(quizListKeys) - 1)]
    

for i in range(3):

    print(f"Points: {point}\n")
    randomQuestion = genQuestion()
    askQuestion = input(f"{randomQuestion}: ")

    if askQuestion == quiz_qs[randomQuestion]:
        print("Correct!")
        point += 1
    else:
        print("Incorrect!")

print(f"Total points: {point}")

"""

def main():
    score = 0
    questions = list(quiz_qs.items())
    random.shuffle(questions)

    for i, (question, answer) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        userAnswer = input("Your answer: ").strip().lower()

        if userAnswer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {answer}")
        
        print(f"Score: {score}/{i}")

    print(f"\nQuiz complete! Final score: {score}/{len(quiz_qs)}")


if __name__ == "__main__":
        main() 

