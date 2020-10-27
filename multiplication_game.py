import random
import time


class multiplication_game:
    
    #Test yourself on n multiplication questions
    def __init__(self,n):
        self.score = 0
        self.correct_answers = 0
        count = 0
        self.q_num = n
        while count < self.q_num:
            num_1 = random.randrange(1,13)
            num_1_str = str(num_1)
            num_2 = random.randrange(1,13)
            num_2_str = str(num_2)
            correct_answer = num_1 * num_2
            start = time.time()
            question = "What is "+num_1_str+" times "+num_2_str+"? "
            response = int(input(question))
            if response == correct_answer:
                stop = time.time()
                p_time = (stop - start)
                p_score = round(60 - p_time,2)
                self.scoring_function(p_score)
                self.correct_answers += 1
                print("Total score:",self.score)
                print("Correct answers:",self.correct_answers,"\n")
            else:
                print("Incorrect answer. Try the next question\n")
            count+=1
        print("Game over.")
        print("Total score:",self.score,"Maximum score:",self.q_num*60)
        print("Total correct answers:",self.correct_answers,"out of",self.q_num,"questions.")
                
    def scoring_function(self,n):
        self.score += n

#Enter any integer number into the argument to generate that number of multiplication questions.
multiplication_game(12)