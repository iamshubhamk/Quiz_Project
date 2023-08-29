from question_model import Question
from data import question_data
from question_brain import QuestionBrain

question_bank = []

def question_object_list():
    for question in question_data:
        question_text = question["question"]
        answer = question["correct_answer"]
        q_object = Question(question_text,answer)
        question_bank.append(q_object)

def start_quiz():
        question_index = 0
        question_brain = QuestionBrain(0)
        while question_index<len(question_bank):
            answer = input(f"Q.no.{question_index+1}- {question_bank[question_index].question}")
            if question_brain.check_answer(answer, question_bank[question_index].answer) == True:
                print (f"You got it right! your current score is {question_brain.score}/{question_index+1}")
            else:
                print(f"You got it wrong!, your current score is {question_brain.score}/{question_index+1}")
            question_index+=1
        print("\n")
        print(f"You completed the Quiz_Game! Your final score is {question_brain.score}/{len(question_bank)}")
question_object_list()
start_quiz()

