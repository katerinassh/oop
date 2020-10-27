class QstTrueFalse: # клас для виду запитань із двома варіантами відповіді так/ні
    def __init__(self, question, answer):
        self.answer = answer
        self.question = question

class QstEnterText: # клас для виду запитань із введенням текстової відповідді
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class QstEnterTextShort(QstEnterText):

class QstOneAnswer:# запитання з вибором однієї правильної відповіді
    def __init__(self, question, numoptions):
        self.question = question
        self.numoptions = numoptions


class QstSomeAnswer:# запитання з вибором декількох правильних відповідей
    def __init__(self, question, numoptions, numright):
        self.question = question
        self.numoptions = numoptions
        self.numright = numright

class QstScale: # запитання з відповіддю на шкалі
    def __init__(self, start, end, step):
        self.step = step
        self.start = start
        self.end = end

class QstTableOne(QstOneAnswer): # таблиця відповідностей
    def __init__(self, size):
        self.size = size

class QstTableSome(QstSomeAnswer): # таблиця з кількома відповідями на питання
    def __init__(self, size):
        self.size = size