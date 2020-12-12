import types_of_questions

class Test(): # клас менеджер-тест, взаємодія і з адміністратором, і зі звичайним користувачем
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.questions = []
        self.qamount = 0
        self.total_mark = 0
        self.mark = 0
        self.ftest = None
        self.fanswers = None

    def workTestFile(self):# метод створює файл, у який записуються питання тесту
        self.ftest = open('{}.txt'.format(self.title), "w")
        self.ftest.write(self.title + "\n")
        self.ftest.write(self.description + "\n" + "\n")
        self.ftest.close()
        self.ftest = open('{}.txt'.format(self.title), "a")
        for i in range(len(self.questions)):
            self.questions[i].writeTestFile(self.ftest)
        self.ftest.close()

    def createAnswerFile(self):# метод створює файл, у який будуть записуватись відповіді респондентів
        self.fanswers = open('{} answers.txt'.format(self.title), "w")
        self.fanswers.write(self.title + "\n")
        self.fanswers.close()

    def workAnswerFile(self):  # метод записує усі відповіді певного респондента
        self.fanswers = open('{} answers.txt'.format(self.title), "a")
        self.fanswers.write(self.questions[0].user_answer + "\n")
        i = 1
        while i < (len(self.questions)):
            self.fanswers.write(str(i) + "\n")
            self.fanswers.write(self.questions[i].user_answer)
            self.fanswers.write(self.questions[i].user_mark)
            i += 1
        self.fanswers.write("\n" + self.totalUserMark())
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

    def passingTest(self):# метод відображає кожне питання для проходження, зберігає відповідь користувача

        return
