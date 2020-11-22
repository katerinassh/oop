class QstTrueFalse: # клас для виду запитань із двома варіантами відповіді так/ні
    def __init__(self, question, answer):
        self.answer = answer
        self.question = question

class QstEnterText: # клас для виду запитань із введенням текстової відповідді
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class QstEnterTextShort(QstEnterText):
    def __init__(self, answer):
        self.answer = answer

class QstOneAnswer:# запитання з вибором однієї правильної відповіді
    def __init__(self, question, numOptions, rightAnswerIndex):
        self._question = question
        self._answerOptions = [] * numOptions
        self._rightAnswer = rightAnswerIndex
        self.rating = 0

    def enterOption(self, option):
        self._answerOptions.push(option)

    def setRating(self, rating):
        self.rating = rating

    def userMarkPerQ(self, choice):
        mark = 0
        if choice == self._rightAnswer:
            mark = self.rating
        return mark

    def __str__(self):
        for i in range (self._answerOptions):
            options = str(self._answerOptions.push[i]) + '\n'
        return str(self._question) + '\n' + options


class QstSomeAnswer:# запитання з вибором декількох правильних відповідей
    def __init__(self, question, rightIndexes):
        self._question = question
        self._answerOptions = len([] * rightIndexes)
        self._rightIndexes = rightIndexes

    def enterOption(self, option):
        self._answerOptions.push(option)

    def setRating(self, rating):
        self.rating = rating

    def userMarkPerQ(self, choice):
        mark = 0
        for i in range(len(choice)):
            for j in range(len(self._rightAnswer)):
                if choice[i] == self._rightAnswer[j]:
                    mark += self.rating / len(choice)
                    break
        return mark

    def __str__(self):
        for i in range (self._answerOptions):
            options = str(self._answerOptions.push[i]) + '\n'
        return str(self._question) + '\n' + options


class QstTableSome(QstSomeAnswer): # питання з кількома варіантами відповіді в таблиці
    def __init__(self, size):
        self.size = size

class QstScale: # запитання з відповіддю на шкалі
    def __init__(self, start, end, step):
        self.step = step
        self.start = start
        self.end = end

class QstTableOne(QstOneAnswer): # встановлення відповідності
    def __init__(self, size):
        self.size = size

