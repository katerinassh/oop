class QstName:
    def __init__(self):
        self._question = None
        self.rating = 0
        self.user_answer = None

    def userGetAnswer(self):
        self.user_answer = input()[:1000]

    def printQ(self):
        print(str(self._question))

    def add(self):
        self._question = "What is your name?"

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")


class QstTrueFalse:  # клас для виду запитань із двома варіантами відповіді правда/брехня
    def __init__(self):
        self._question = None
        self._right_answer = None
        self._answerOptions = ["True", "False"]
        self.user_answer = None
        self.user_mark = 0
        self.rating = 0

    def setRating(self, rating):
        self.rating = rating

    def userGetAnswer(self):
        self.user_answer = input("Enter your answer:\n")
        self.userMark()

    def userMark(self):
        if self.user_answer == self._right_answer:
            self.user_mark = self.rating

    def printQ(self):
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        print(str(self._question) + '\n' + options)

    def add(self):
        print('Input question')
        self._question = input()
        print('Input the right answer (True or False)')
        self._right_answer = input()
        print('Input question valuation')
        self.rating = input()

    def writeTestFile(self, the_file):
        the_file.write('QstTrueFalse\n')
        the_file.write(str(self._question) + "\n")
        the_file.write(str(self._right_answer) + "\n" + str(self.rating) + "\n\n")

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        self._right_answer = file.readline().strip("\n")
        self.rating = float(file.readline().strip("\n"))


class QstEnterText:  # клас для виду запитань із введенням текстової відповідді
    def __init__(self):
        self._question = None
        self._right_answer = None
        self.rating = 0
        self.user_answer = None
        self.user_mark = 0

    def setRating(self, rating):
        self.rating = rating

    def userGetAnswer(self):
        self.user_answer = input()[:1000]
        self.userMark()

    def userMark(self):
        right_answer = str(self._right_answer).lower().split()
        user_answer = str(self.user_answer).lower()

        if all(keyword in user_answer for keyword in right_answer):
            self.user_mark = self.rating

    def printQ(self):
        print(str(self._question))

    def add(self):
        print('Input question')
        self._question = input()
        print('Input the right answer')
        self._right_answer = input()
        print('Input question valuation')
        self.rating = input()

    def writeTestFile(self, the_file):
        the_file.write('QstEnterText\n')
        the_file.write(str(self._question) + "\n" + str(self._right_answer) + "\n" + str(self.rating) + "\n\n")

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        self._right_answer = file.readline().strip("\n")
        self.rating = float(file.readline().strip("\n"))


class QstOneAnswer:  # запитання з вибором однієї правильної відповіді
    def __init__(self):
        self._question = ''
        self._answerOptions = []
        self._rightAnswerIndex = None
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
        print('Input number of options')
        numOptions = int(input())
        self._answerOptions = [] * numOptions
        for i in range(numOptions):
            print('Input option ' + str(i + 1) + ' : ')
            option = input()
            self.enterOption(option)
        print('Input index of right answer')
        self._rightAnswerIndex = int(input())
        print('Input question valuation')
        self.setRating(input())

    def userGetAnswer(self):
        self.user_answer = input()
        self.userMark(self.user_answer)

    def userMark(self, choice):
        mark = 0
        if choice == self._answerOptions[self._rightAnswerIndex - 1]:
            mark = self.rating
        self.user_mark = mark

    def writeTestFile(self, file):
        file.write('QstOneAnswer\n')
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        file.write(self._question)
        file.write(str(len(self._answerOptions)) + '\n')
        file.write(options + str(self._rightAnswerIndex) + '\n')
        file.write(str(self.rating) + '\n\n')

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        numOptions = int(file.readline().strip("\n"))
        for i in range(numOptions):
            self._answerOptions[i] = file.readline().strip("\n")
        self._rightAnswerIndex = int(file.readline().strip("\n"))
        self.rating = float(file.readline().strip("\n"))

    def printQ(self):
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        print(str(self._question) + '\n' + options)


class QstSomeAnswer(QstOneAnswer):  # запитання з вибором декількох правильних відповідей, наслідує клас з одним правильним
    def __init__(self):
        super().__init__()
        self._rightAnswerIndexArr = []

    def add(self):
        print('Input question')
        self._question = input()
        print('Input number of options')
        numOptions = int(input())
        self._answerOptions = [] * numOptions
        for i in range(numOptions):
            print('Input option ' + str(i + 1) + ' : ')
            option = input()
            self.enterOption(option)
        print('Input number of right options')
        numRight = int(input())
        for i in range(numRight):
            print('Input index of right answer ' + str(i + 1) + ' : ')
            right = input()
            self._rightAnswerIndexArr.append(int(right))
        print('Input question valuation')
        self.setRating(input())


    def userMark(self, choice):
        mark = 0
        markForPoint = int(self.rating) / len(self._rightAnswerIndexArr)
        for i in range(len(choice.split(', '))):
            for j in range(len(self._rightAnswerIndexArr)):
                if (choice.split(', '))[i] == self._answerOptions[int(self._rightAnswerIndexArr[j]) - 1]:
                    mark += markForPoint
                    break
        self.user_mark = mark

    def writeTestFile(self, file):
        file.write('QstSomeAnswer\n')
        options = ''
        rights = ''
        for i in self._answerOptions:
            options += i + '\n'
        for i in self._rightAnswerIndexArr:
            rights += str(i) + ' '
        file.write(str(self._question) + '\n' + str(len(self._answerOptions)) + '\n' + options +
                   rights + '\n' + str(self.rating) + '\n\n')

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        numOptions = int(file.readline().strip("\n"))
        for i in range(numOptions):
            self._answerOptions[i] = file.readline().strip("\n")
        numRight = int(file.readline().strip("\n"))
        for i in range(numRight):
            self._rightAnswerIndexArr = int(file.readline().strip("\n"))
        self.rating = float(file.readline().strip("\n"))


class QstTable(QstSomeAnswer):  # запитання з кількома варіантами відповіді в таблиці, наслідує клас з декількома варіантами відповідей
    def __init__(self):
        self._subquestions = []
        self.options = []
        self._answerOptions = []
        self.sizeHeight = len(self._subquestions)
        self.table = [] * self.sizeHeight
        self.user_answer = None
        self.rating = 0

    def add(self):
        print('Input main question')
        self._question = input()
        print('Input subquestions')
        s = input()
        self._subquestions = s.split(', ')
        self.sizeHeight = len(self._subquestions)
        print('Input number of options')
        numOptions = int(input())
        for i in range(numOptions):
            print('Input option ' + (str(i + 1)))
            option = input()
            self.enterOption(option)
        for i in range(numOptions):
            subRightIndexes = []
            print('Input indexes of right answers option ' + str(i + 1))
            indexes = input().split(', ')
            for j in range(len(indexes)):
                subRightIndexes.append(indexes[i])
            self._rightAnswerIndexArr.append(subRightIndexes)
        print('Input question valuation\n')
        self.rating = float(input())
        self.formTable(self.rating)

    def formTable(self, rating):
        for i in range(self.sizeHeight):
            qRow = QstSomeAnswer(self._subquestions[i], len(self.options), self._rightAnswerIndex[i])
            self.table.append(qRow)
            self.table[i].setRating(rating / self.sizeHeight)

    def userMark(self, choice):
        mark = 0
        for i in range(self.sizeHeight):
            if len(choice[i]) > len(self._rightAnswerIndexArr[i]):
                break
            else:
                mark += self.table[i].userMark(choice[i])
        self.user_mark = mark

    def userGetAnswer(self, file):
        self.user_answer = input()
        self.userMark(self.user_answer)

    def writeTestFile(self, file):
        file.write('QstTable\n')
        file.write(self._question + '\n')
        file.write(str(self.sizeHeight) + '\n')
        for i in range(self.sizeHeight):
            file.write(self._subquestions[i] + '\n')
        file.write(str(len(self.options)) + '\n')
        for i in range(len(self.options)):
            file.write(self.options[i] + '\n')
        for i in range(self.sizeHeight):
            file.write(self._rightAnswerIndexArr[i] + '\n')
        file.write(str(self.rating) + '\n\n')

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        self.sizeHeight = int(file.readline().strip("\n"))
        for i in range(self.sizeHeight):
            self._subquestions[i] = file.readline().strip("\n")
        length = int(file.readline().strip("\n"))
        for i in range(length):
            self.options[i] = file.readline().strip("\n")
        for i in range(self.sizeHeight):
            self._rightAnswerIndexArr[i] = file.readline().strip("\n")
        self.rating = int(file.readline().strip("\n"))

    def printQ(self):
        print(self._question)
        row = ''
        for i in range(self.sizeHeight):
            row += str(self._subquestions[i]) + ': '
            for j in range(len(self.options)):
                row += str(self.options[j]) + ' '
            print(row)
            row = ''


class QstScale:  # запитання з відповіддю числом (передбачало шкалу з повзунком)
    def __init__(self):
        self._question = ''
        self._right_answer = ''
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
        self.user_answer = float(input())
        self.userMark(self.user_answer)

    def writeTestFile(self, ftest):
        ftest.write('QstScale', end='\n')
        ftest.write(self._question, end='\n')
        ftest.write(self._right_answer, end='\n')
        ftest.write(str(self.rating) + '\n', end='\n')

    def add(self):
        print('Input question\n')
        self._question = input()
        print('Input the right answer\n')
        self._right_answer = float(input())
        print('Input question valuation\n')
        self.setRating(float(input()))
        
    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        self._right_answer = float(file.readline().strip("\n"))
        self.rating = float(file.readline().strip("\n"))


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
        print(self._question, end = '\n\n')
        for i in range(self.num_answers):
            print(str(i+1)+self.text_questions[i], end='\n')
        print(end='\n')
        for i in range(self.num_answers):
            print(str(i+1)+self.text_answers[i], end='\n')

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
        self._question = file.readline().strip("\n")
        self.num_answers = int(file.readline().strip("\n"))
        for i in range(self.num_answers):
            self.text_questions[i] = file.readline().strip("\n")
            self.text_answers[i] = file.readline().strip("\n")
        self._right_answer = file.readline().strip("\n")
        self.rating = float(file.readline().strip("\n"))

    def writeTestFile(self, ftest):
        ftest.write('QstTableOne\n')
        ftest.write(self._question, end='\n')
        ftest.write(str(self.num_answers), end='\n')
        for i in range(self.num_answers):
            ftest.write(self.text_questions[i] + '\n' + self.text_answers[i], end='\n')
        ftest.write(self._right_answer, end='\n')
        ftest.write(str(self.rating)+'\n', end='\n')
