class QstTrueFalse: # клас для виду запитань із двома варіантами відповіді так/ні
    def true_false(self):
        return bool

class QstEnterText: # клас для виду запитань із введенням текстової відповідді
    def small_answer(self): # метод для введення відповідді з обмеженням у 50 символів
        return

    def big_answer(self): # метод для введення відповідді з обмеженням у 1000 символів
        return


class OneAnswer():# запитання з вибором однієї правильної відповіді
    def __init__(self, question, numoptions):
        self.question = question
        self.numoptions = numoptions


class SomeAnswer():# запитання з вибором декількох правильних відповідей
    def __init__(self, question, numoptions, numright):
        self.question = question
        self.numoptions = numoptions
        self.numright = numright