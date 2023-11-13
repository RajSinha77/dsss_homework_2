import random

#Generates Random integer within range of two numbers including minimum value and maximum value itself.
def Generate_Random_Integer(min_value, max_value):
    
    return random.randint(min_value, max_value)


# Chooses random mathematical operator where the given choice is ('+', '-', '*').

def Generate_Random_Operator():
    return random.choice(['+', '-', '*'])

#Performs mathematical operation and return the calulated value of the expression.
def Evaluate_Mathematical_Expression(num_1, num_2, operator):
    if operator == '+': result = num_1 + num_2
    elif operator == '-': result = num_1 - num_2
    elif operator =='*' : result= num_1 * num_2
    else:
        raise ValueError("Invalid operator. Valid Choices are (+,-,*)")

    expression = f"{num_1} {operator} {num_2}"    #operation format
    return expression, result
 

#Gives the user with a set of math problems and calculates their answers.
def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

# iterate overs total number of questions"
    for _ in range(total_questions):
        random_number1 = Generate_Random_Integer(1, 10); 
        random_number2 = Generate_Random_Integer(1, 5); 
        random_operator = Generate_Random_Operator()

        problem, answer = Evaluate_Mathematical_Expression(random_number1, random_number2, random_operator)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        
        if user_answer == answer:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
