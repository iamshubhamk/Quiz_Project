class QuestionBrain:

    def __init__(self,score):
        self.score = score

    def check_answer(self,answer,correct_answer):
        if answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
    