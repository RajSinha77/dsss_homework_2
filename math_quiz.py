import random

#returns random integer for a specified range min and max 
def Generate_Random_Integer(min_val, max_val):
    """
    Random integer between min and max  value.
    """
    return random.randint(min_val, max_val)

#returns random mathematical operator between +,- or *
def Generate_Random_Operator():
    return random.choice(['+', '-', '*'])

#performs arithmatic operation on two numbers and return expression and result
def Generate_Expression_Result(num_1, num_2, operator):
    expression = f"{num_1} {operator} {num_2}"
    if operator == '-': 
        output = num_1 - num_2
    elif output == '+': 
        a = num_1 + num_2
    else: 
        output = num_1 * num_2
        #returns expression with its result
    return expression, output

def math_quiz():
    #setting initial score 0
    score = 0
    #setting total questions to be asked = 3
    total_question = 3
     
    # welcome message on screen 
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    # to generate random number and operator, performing arithmatic operation and returning results
    for _ in range(total_question):
        num_1 = Generate_Random_Integer(1, 10);
        num_2 = Generate_Random_Integer(1, 5); 
        operator = Generate_Random_Operator()

        
        PROBLEM, ANSWER = Generate_Expression_Result(num_1, num_2, operator)
        #users answer
        print(f"\nQuestion: {PROBLEM}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)
        
        #Exception handling when input is not an integer or invalid
        try: 
            user_answer == int(user_answer)    
        except ValueError:
            print("Invalid Input ! Please enter an integer")
            continue
        
        #if answer provided by user is correct
        if user_answer == ANSWER:
            print("congratulations! correct answer, you earned a point")
            score +=1    #Incrementing score if correct by 1
        else: 
            #if user's answer is wrong
            print(f"Sorry wrong answer. The correct answer is {ANSWER}.")
    print(f"\nGame over! Your score is: {score}/{total_question}")

if __name__ == "__main__":
    math_quiz()
