import types_of_questions

class Test(): # клас менеджер-тест, взаємодія і з адміністратором, і зі звичайним користувачем
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.questions = []
        self.qamount = 0

    def add(self, type):# метод додає нове питання у тест
        self.qamount += 1
        if type == 'QstOneAnswer':
            print('Input question')
            question = input()
            print('Input number of options\n')
            numOptions = input()
            print('Input index of right answer\n')
            rightAnswerIndex = input()
            print('Input question valuation\n')
            rating = input()
            qst = types_of_questions.QstOneAnswer(question, int(numOptions), rightAnswerIndex)
            qst.setRating(rating)
            for i in range(int(numOptions)):
                print('Input option ' + str(i) + ' : ')
                option = input()
                qst.enterOption(option)
            self.questions.append(qst)


    def remove(self, number):# метод видаляє певне питання з тесту
        self.questions.pop(number - 1)
        self.qamount -= 1

    def _edit(self, number):# метод редагує питання
        return

    def totalMark(self):# метод рахує повний бал тесту
        sum = 0
        for i in self.questions:
            sum += i.rating()
        return sum

