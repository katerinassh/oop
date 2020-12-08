class QstTrueFalse:  # клас для виду запитань із двома варіантами відповіді правда/брехня
    def __init__(self):
        self._type = "TrueFalse"
        self._question = None
        self._right_answer = None
        self._answerOptions = ["True", "False"]
        self.user_answer = None
        self.rating = 0

    def setRating(self, rating):
        self.rating = rating

    def userGetAnswer(self):
        self.user_answer = input()

    def userMarkAnswer(self):
        mark = 0
        if self.user_answer == self._right_answer:
            mark = self.rating
        return mark

    def printQ(self):
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        print(str(self._question) + '\n' + options)

    def add(self):
        print('Input question\n')
        self._question = input()
        print('Input the right answer (True or False)\n')
        self._right_answer = input()
        print('Input question valuation\n')
        self.rating = input()

    def save_qst(self, file, indx_qst):
        # *file = "test.txt"
        the_file = open(file, "a")

        the_file.write("\n\n**" + str(indx_qst) + "**\n")
        the_file.write(self._type + "\n" + self._question + "\n" + str(self.rating)+ "\n\n")

        for i in range(2):
            the_file.write(self._answerOptions[i] + "\n")
        the_file.write("\n" + str(self._right_answer))

        the_file.close()

    def save_answ(self, file, indx_qst):
        # *file = "answs.txt"
        the_file = open(file, "a")

        qst = QstTrueFalse()
        the_file.write("\n\n**" + str(indx_qst) + "**\n")
        the_file.write(str(self.user_answer) + "\n" + str(qst.userMarkAnswer()))

        the_file.close()


class QstEnterText:  # клас для виду запитань із введенням текстової відповідді
    def __init__(self):
        self._type = "EnterLongText"
        self._question = None
        self._right_answer = None
        self.rating = 0
        self.user_answer = None

    def setRating(self, rating):
        self.rating = rating

    def userGetAnswer(self):
        self.user_answer = input()[:1000]

    def userMarkAnswer(self):
        mark = 0
        if self.user_answer == self._right_answer:
            mark = self.rating
        return mark

    def printQ(self):
        print(str(self._question))

    def add(self):
        print('Input question\n')
        self._question = input()
        print('Input the right answer\n')
        self._right_answer = input()
        print('Input question valuation\n')
        self.rating = input()

    def save_qst(self, file, indx_qst):
        # *file = "test.txt"
        the_file = open(file, "a")

        the_file.write("\n\n**" + str(indx_qst) + "**\n")
        the_file.write(self._type + "\n" + self._question + "\n" + str(self.rating)+ "\n\n")

        the_file.write("\n" + str(self._right_answer))

        the_file.close()

    def save_answ(self, file, indx_qst):
        # *file = "answs.txt"
        the_file = open(file, "a")

        qst = QstEnterText()
        the_file.write("\n\n**" + str(indx_qst) + "**\n")
        the_file.write(str(self.user_answer) + "\n" + str(qst.userMarkAnswer()))

        the_file.close()


class QstEnterTextShort(QstEnterText):  # клас для виду запитань із введенням короткої текстової відповідді
    def __init__(self):
        super().__init__()
        self._type = "EnterShortText"
        self.rating = 0
        self.user_answer = None

    def userGetAnswer(self):
        self.user_answer = input()[:100]

    def save_answ(self, file, indx_qst):
        # *file = "test.txt"
        the_file = open(file, "a")

        qst = QstEnterTextShort()
        the_file.write("\n\n**" + str(indx_qst) + "**\n")
        the_file.write(str(self.user_answer) + "\n" + str(qst.userMarkAnswer()))

        the_file.close()


class QstOneAnswer:  # запитання з вибором однієї правильної відповіді
    def __init__(self):
        self._question = ''
        self._answerOptions = []
        self._rightAnswer = None
        self.rating = 0
        self.user_answer = None
        self.user_mark = 0

    def enterOption(self, option):
        self._answerOptions.append(option)

    def setRating(self, rating):
        self.rating = rating

    def add(self):
        print('Input question')
        self._question = input()
        print('Input number of options\n')
        numOptions = int(input())
        self._answerOptions = [] * numOptions
        print('Input index of right answer\n')
        self._rightAnswer = int(input())
        print('Input question valuation\n')
        self.setRating(input())
        for i in range(numOptions):
            print('Input option ' + str(i) + ' : ')
            option = input()
            self.enterOption(option)

    def userGetAnswer(self, file):
        self.user_answer = input()
        self.userMark(self.user_answer)

    def userMark(self, choice):
        mark = 0
        if choice == self._rightAnswer:
            mark = self.rating
        self.user_mark = mark

    def writeTestFile(self, file):
        ftest = open('{}.txt'.format(file), "a")
        ftest.write('QstOneAnswer\n')
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        ftest.write(str(self._question) + '\n' + options)
        ftest.close()

    def printQ(self):
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        print(str(self._question) + '\n' + options)


class QstSomeAnswer(QstOneAnswer):  # запитання з вибором декількох правильних відповідей, наслідує клас з одним правильним
    def __init__(self):
        super().__init__()

    def add(self):
        print('Input question')
        self._question = input()
        print('Input number of options\n')
        numOptions = int(input())
        self._answerOptions = [] * numOptions
        print('Input indexes of right answers in format [[i],[i1,i]]\n')
        self._rightAnswer = input()
        print('Input question valuation\n')
        self.setRating(input())
        for i in range(numOptions):
            print('Input option ' + str(i) + ' : ')
            option = input()
            self.enterOption(option)

    def userMark(self, choice):
        mark = 0
        markForPoint = self.rating / len(self._rightAnswer)
        for i in range(len(choice)):
            for j in range(len(self._rightAnswer)):
                if choice[i] == self._rightAnswer[j]:
                    mark += markForPoint
                    break
        self.user_mark = mark

    def writeTestFile(self, file):
        ftest = open('{}.txt'.format(file), "a")
        ftest.write('QstSomeAnswer\n')
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        ftest.write(str(self._question) + '\n' + options)


class QstTable(QstSomeAnswer):  # запитання з кількома варіантами відповіді в таблиці, наслідує клас з декількома варіантами відповідей
    def __init__(self):
        self.questions = []
        self.options = []
        self.sizeHeight = len(self.questions)
        self.table = [] * self.sizeHeight
        self.user_answer = None

    def add(self):
        print('Input main question')
        self._question = input()
        print('Input local questions in format ['',''...]')
        self.questions = input()
        print('Input options in format ['',''...]\n')
        self.options = input()
        print('Input indexes of right answers in format [[i],[i1,i]]\n')
        self._rightAnswer = input()
        print('Input question valuation\n')
        self.formTable(int(input()))

    def formTable(self, rating):
        for i in range(self.sizeHeight):
            qRow = QstSomeAnswer(self.questions[i], len(self.options), self._rightAnswer[i])
            self.table.append(qRow)
            self.table[i].setRating(rating / self.sizeHeight)

    def userMark(self, choice):
        mark = 0
        for i in range(self.sizeHeight):
            if len(choice[i]) > len(self._rightAnswer[i]):
                break
            else:
                mark += self.table[i].userMarkPerSomeQ(choice[i])
        self.user_mark = mark

    def userGetAnswer(self, file):
        self.user_answer = input()
        self.userMark(self.user_answer)

    def writeTestFile(self, file):
        ftest = open('{}.txt'.format(file), "a")
        ftest.write('QstTable\n')
        ftest.write(self._question)
        row = ''
        for i in range(self.sizeHeight):
            row += str(self.questions[i]) + ': '
            for j in range(len(self.options)):
                row += str(self.options[j]) + ' '
            ftest.write(row)
            row = ''
        ftest.close()

    def printTable(self):
        print(self._question)
        row = ''
        for i in range(self.sizeHeight):
            row += str(self.questions[i]) + ': '
            for j in range(len(self.options)):
                row += str(self.options[j]) + ' '
            print(row)
            row = ''


class QstScale:  # запитання з відповіддю на шкалі
    def __init__(self, question, right_answer):
        self._question = question
        self._right_answer = right_answer
        self.rating = 0
        self.start = 0
        self.end = 100
        self.user_answer = None

    def setRating(self, rating):
        self.rating = rating

    def getMark(self, answer):
        mark = 0
        if answer == self._right_answer:
            mark += self.rating
        return mark

    def printQ(self):
        print(str(self._question),end = "\n")
        for i in range(10):
            if i!=1:
                print (str(i*10)+"_")
            else:
                print(str(i * 10))

    def userGetAnswer(self):
        self.user_answer = int(input())

class QstTableOne:  # встановлення відповідності
    def __init__(self, question, num_answers, num_questions):
        self.question = question
        self.num_answers = num_answers
        self.num_questions = num_questions
        self.text_answers = [] * num_answers
        self.text_questions = [] * num_questions
        self.rating = 0
        self._user_answer = [] * num_questions
        self._right_answer = [] * num_questions

    def setRating(self, rating):
        self.rating = rating

    def getTextAnswers(self):
        for i in range(self.num_answers):
            self.text_answers[i-1] = str(input())

    def getTextQuestions(self):
        for i in range(self.num_questions):
            self.text_questions[i-1] = str(input())

    def setRightAnswer(self):
        for i in range(self.num_questions):
            self._right_answer[i-1] = int(input())

    def userGetAnswer(self):
        for i in range(self.num_questions):
            ans = int(input())
            while (ans > self.num_answers) or (ans<0):
                print('Оберіть номер з перелічених або 0, якщо відповіді немає')
                ans = int(input())
            self._user_answer[i - 1] = ans

    def getMark(self):
        mark = 0
        for i in range(self.num_questions):
            if self._right_answer[i]==self._user_answer[i]:
                mark += self.rating/self.num_questions
        return mark

    def printQ(self):
        print (self.question, end = '\n\n')
        for i in range(self.num_questions):
            print (str(i+1)+self.text_questions[i],end = '\n')
        print (end = '\n')
        for i in range(self.num_answers):
            print (str(i+1)+self.text_answers[i], end = '\n')