import types_of_questions

class Test(): # клас менеджер-тест, взаємодія і з адміністратором, і зі звичайним користувачем
    def __init__(self, title, description):
        self.title = title
        self.decription = description
        self.questions = []
        self.qamount = 0
        self.total_mark = 0
        self.mark = 0

    def workTestFile(self):# метод створює файл, у який записуються питання тесту
        self.ftest = open('{}.txt'.format(self.title), "w")
        self.ftest.write(self.title + "\n")
        self.ftest.write(self.decription + "\n")
        for i in range(len(self.questions)):
            self.questions[i].writeTestFile(self.ftest)
        self.ftest.close()

    def workAnswerFile(self):# метод створює файл, у який записуються відповіді користувача
        self.fanswers = open('{} answers.txt'.format(self.title), "w")
        self.fanswers.close()

    def add(self, type):# метод додає нове питання у тест
        self.qamount += 1
        if type == 'QstTrueFalse':
            qst = types_of_questions.QstTrueFalse()
        if type == 'QstEnterText':
            qst = types_of_questions.QstEnterText()
        if type == 'QstEnterTextShort':
            qst = types_of_questions.QstEnterTextShort()
        if type == 'QstOneAnswer':
            qst = types_of_questions.QstOneAnswer()
        if type == 'QstSomeAnswer':
            qst = types_of_questions.QstSomeAnswer()
        if type == 'QstTable':
            qst = types_of_questions.QstTable()
        if type == 'QstScale':
            qst = types_of_questions.QstScale()
        if type == 'QstTableOne':
            qst = types_of_questions.QstTableOne()
        qst.add()
        qst.writeTestFile(self.ftest)
        self.questions.append(qst)

    def remove(self, number):# метод видаляє певне питання з тесту
        self.questions.pop(number - 1)
        self.qamount -= 1
        self.workTestFile()

    def rewrite(self, number):# метод переписує певне питання
        self.remove(number)
        print('Input type of new question')
        type = input()
        if type == 'QstTrueFalse':
            qst = types_of_questions.QstTrueFalse()
        if type == 'QstEnterText':
            qst = types_of_questions.QstEnterText()
        if type == 'QstEnterTextShort':
            qst = types_of_questions.QstEnterTextShort()
        if type == 'QstOneAnswer':
            qst = types_of_questions.QstOneAnswer()
        if type == 'QstSomeAnswer':
            qst = types_of_questions.QstSomeAnswer()
        if type == 'QstTable':
            qst = types_of_questions.QstTable()
        if type == 'QstScale':
            qst = types_of_questions.QstScale()
        if type == 'QstTableOne':
            qst = types_of_questions.QstTableOne()
        qst.add()
        self.questions.insert(number - 1, qst)
        self.workTestFile()

    def totalUserMark(self):# метод рахує бал користувача за всі питання разом
        for i in self.questions:
            self.mark += i.user_mark
        return self.mark


    def totalTestMark(self):# метод рахує повний бал тесту
        for i in self.questions:
            self.total_mark += i.rating()
        return self.total_mark

