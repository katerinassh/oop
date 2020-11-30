class QstTrueFalse:  # клас для виду запитань із двома варіантами відповіді правда/брехня
    def __init__(self, question, right_answer):
        self._question = question
        self._right_answer = right_answer
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


class QstEnterText:  # клас для виду запитань із введенням текстової відповідді
    def __init__(self, question, right_answer):
        self._question = question
        self._right_answer = right_answer
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


class QstEnterTextShort(QstEnterText):  # клас для виду запитань із введенням короткої текстової відповідді
    def __init__(self, question, right_answer):
        super().__init__(question, right_answer)
        self.rating = 0
        self.user_answer = None

    def setRating(self, rating):
        self.rating = rating

    def userGetAnswer(self):
        self.user_answer = input()[:100]

    def userMarkAnswer(self):
        mark = 0
        if self.user_answer == self._right_answer:
            mark = self.rating
        return mark

    def printQ(self):
        print(str(self._question))


class QstOneAnswer:  # запитання з вибором однієї правильної відповіді
    def __init__(self, question, numOptions, rightAnswerIndex):
        self._question = question
        self._answerOptions = [] * numOptions
        self._rightAnswer = rightAnswerIndex
        self.rating = 0

    def enterOption(self, option):
        self._answerOptions.append(option)

    def setRating(self, rating):
        self.rating = rating

    def userMarkOneAnswer(self, choice):
        mark = 0
        if choice == self._rightAnswer:
            mark = self.rating
        return mark

    def printQ(self):
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        print(str(self._question) + '\n' + options)


class QstSomeAnswer(QstOneAnswer):  # запитання з вибором декількох правильних відповідей, наслідує клас з одним правильним
    def __init__(self, question, numOptions, rightAnswerIndex):
        super().__init__(question, numOptions, rightAnswerIndex)

    def userMarkSomeAnswer(self, choice):
        mark = 0
        markForPoint = self.rating / len(self._rightAnswer)
        for i in range(len(choice)):
            for j in range(len(self._rightAnswer)):
                if choice[i] == self._rightAnswer[j]:
                    mark += markForPoint
                    break
        return mark


class QstTable(QstSomeAnswer):  # запитання з кількома варіантами відповіді в таблиці, наслідує клас з декількома варіантами відповідей
    def __init__(self, mainQuestion, questions, options, rightAnswerIndex):
        super().__init__(mainQuestion, len(options), rightAnswerIndex)
        self.questions = questions
        self.options = options
        self.sizeHeight = len(questions)
        self.table = [] * self.sizeHeight

    def formTable(self, rating):
        for i in range(self.sizeHeight):
            qRow = QstSomeAnswer(self.questions[i], len(self.options), self._rightAnswer[i])
            self.table.append(qRow)
            self.table[i].setRating(rating / self.sizeHeight)

    def userMarkTable(self, choice):
        mark = 0
        for i in range(self.sizeHeight):
            if len(choice[i]) > len(self._rightAnswer[i]):
                break
            else:
                mark += self.table[i].userMarkPerSomeQ(choice[i])
        return mark

    def printTable(self):
        print(self._question)
        row = ''
        for i in range(self.sizeHeight):
            row += str(self.questions[i]) + ': '
            for j in range(len(self.options)):
                row += str(self.options[j]) + ' '
            print(row)
            row = ''


#firstQuestion = QstTable('Who am I for...?', ['Kate', 'Jane'], ['friend', 'nobody', 'stranger'], [[1,3],[1]]) #testing
#firstQuestion.formTable(1)
#firstQuestion.printTable()

#print(firstQuestion.userMarkTable([[1,3],[1,2]]))


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
        mark = 0;
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