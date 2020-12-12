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
        self.user_answer = input("Enter your answer:\n")
        self.user_mark()

    def user_mark(self):
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

        the_file.write("\n\n" + str(indx_qst) + "\n")
        the_file.write(self._type + "\n" + self._question + "\n" + str(self.rating) + "\n\n")

        for i in range(2):
            the_file.write(self._answerOptions[i] + "\n")
        the_file.write("\n" + str(self._right_answer))

        the_file.close()

    def save_answ(self, file, indx_qst):
        # *file = "answs.txt"
        the_file = open(file, "a")

        qst = QstTrueFalse()
        the_file.write("\n\n" + str(indx_qst) + "\n")
        the_file.write(str(self.user_answer) + "\n" + str(qst.user_mark()))

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
        self.user_mark()

    def user_mark(self):
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

        the_file.write("\n\n" + str(indx_qst) + "\n")
        the_file.write(self._type + "\n" + self._question + "\n" + str(self.rating)+ "\n\n")

        the_file.write("\n" + str(self._right_answer))

        the_file.close()

    def save_answ(self, file, indx_qst):
        # *file = "answs.txt"
        the_file = open(file, "a")

        qst = QstEnterText()
        the_file.write("\n\n" + str(indx_qst) + "\n")
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
        the_file.write("\n\n" + str(indx_qst) + "\n")
        the_file.write(str(self.user_answer) + "\n" + str(qst.user_mark()))

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
        file.write('QstOneAnswer\n')
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        file.write(str(self._question) + '\n' + str(len(self._answerOptions)) + '\n' + options +
                   self._rightAnswer + '\n' + self.rating + '\n')

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
        file.write('QstSomeAnswer\n')
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        file.write(str(self._question) + '\n' + str(len(self._answerOptions)) + '\n' + options +
                   self._rightAnswer + '\n' + self.rating + '\n')


class QstTable(QstSomeAnswer):  # запитання з кількома варіантами відповіді в таблиці, наслідує клас з декількома варіантами відповідей
    def __init__(self):
        self.questions = []
        self.options = []
        self.sizeHeight = len(self.questions)
        self.table = [] * self.sizeHeight
        self.user_answer = None
        self.rating = 0

    def add(self):
        print('Input main question')
        self._question = input()
        print('Input local questions in format ['',''...]')
        self.lquestions = input()
        print('Input options in format ['',''...]\n')
        self.options = input()
        print('Input indexes of right answers in format [[i],[i1,i]]\n')
        self._rightAnswer = input()
        print('Input question valuation\n')
        self.rating = int(input())
        self.formTable(self.rating)

    def formTable(self, rating):
        for i in range(self.sizeHeight):
            qRow = QstSomeAnswer(self.lquestions[i], len(self.options), self._rightAnswer[i])
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
        file.write('QstTable\n')
        file.write(self._question)
        row = ''
        for i in range(self.sizeHeight):
            row += str(self.lquestions[i]) + ': '
            for j in range(len(self.options)):
                row += str(self.options[j]) + ' '
            file.write(row)
            row = ''
        file.write(str(self._rightAnswer) + '\n' + str(self.rating) + '\n')

    def printTable(self):
        print(self._question)
        row = ''
        for i in range(self.sizeHeight):
            row += str(self.questions[i]) + ': '
            for j in range(len(self.options)):
                row += str(self.options[j]) + ' '
            print(row)
            row = ''

class QstScale:  # запитання з відповіддю числом (передбачало шкалу з повзунком)
    def __init__(self):
        self._question = question
        self._right_answer = right_answer
        self.rating = 0
        #self.start = 0
        #self.end = 100
        self.user_answer = None
        self.user_mark = 0

    def setRating(self, rating):
        self.rating = rating

    def userMark(self, answer):
        if answer == self._right_answer:
            self.user_mark = self.rating

    def printQ(self):
        print(str(self._question), end='\n')

    def userGetAnswer(self):
        self.user_answer = double(input())
        userMark(self.user_answer)

    def writeTestFile(self, file):
        ftest = open('{}.txt'.format(file), "a")
        ftest.write('QstScale\n')
        ftest.write(self._question,end = '\n')
        ftest.write(self.user_answer, end = '\n')
        ftest.close()

class QstTableOne:  # встановлення відповідності
    def __init__(self):
        self._question = ''
        self.num_answers = 0
        self.text_answers = None
        self.text_questions = None
        self.rating = 0
        self._user_answer = None
        self._right_answer = None
        self.user_mark = 0

    def setRating(self, rating):
        self.rating = rating

    def getTextAnswers(self):
        for i in range(self.num_answers):
            print('Answer ', str(i), ':', end=' ')
            self.text_answers += input()
            print(end='\n')

    def getTextQuestions(self):
        for i in range(self.num_questions):
            print('Question ', str(i), ':', end=' ')
            self.text_questions[i] = str(input())
            print(end='\n')

    def setRightAnswer(self):
        self._right_answer = input()

    def userGetAnswer(self):
        for i in range(self.num_questions):
            ans = int(input())
            while (ans > self.num_answers) or (ans<0):
                print('Оберіть номер з перелічених')
                ans = int(input())
            self._user_answer[i] = ans
        self.userMark()

    def userMark(self):
        right_answer = self._right_answer.split()
        user_answer = self._user_answer.split()
        for i in range(right_answer):
            if user_answer[i] == right_answer[i]:
                self.user_mark += self.rating / self.num_answers

    def printQ(self):
        print (self._question, end = '\n\n')
        for i in range(self.num_answers):
            print (str(i+1)+self.text_questions[i],end = '\n')
        print (end = '\n')
        for i in range(self.num_answers):
            print (str(i+1)+self.text_answers[i], end = '\n')

    def add(self):
        print('Input main question')
        self._question = input()
        print('Input number of options/questions\n')
        self.num_answers = int(input())

        self.text_answers = [] * self.num_answers
        self.text_questions = [] * self.num_answers
        self._user_answer = [] * self.num_answers
        self._right_answer = [] * self.num_answers

        print('Input local questions\n')
        self.getTextQuestions()
        print('Input answers\n')
        self.getTextAnswers()

        print('Input indexes of right answer for each local questions\n')
        self.setRightAnswer()
        print('Input question valuation\n')
        self.setRating(float(input()))

    def readTestFile(self, file):
        self._question = file.readline()
        self.num_answers = int(file.readline())
        for i in range(self.num_answers):
            self.text_questions[i] = file.readline()
            self.text_answers[i] = file.readline()
        self._right_answer = file.readline()
        self.rating = float(file.readline())

    def writeTestFile(self, file):
        ftest = open('{}.txt'.format(file), "a")
        ftest.write('QstTableOne\n')
        ftest.write(self._question, end='\n')
        ftest.write(str(self.num_answers), end='\n')
        for i in range(self.num_answers):
            ftest.write(self.text_questions[i] + '\n' + self.text_answers[i],end = '\n')
        ftest.write(self._right_answer, end = '\n')
        ftest.write(str(self.rating)+'\n', end='\n')
        ftest.close()


