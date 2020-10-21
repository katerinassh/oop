class Test(): # клас менеджер-тест, взаємодія і з адміністратором, і зі звичайним користувачем
    def __init__(self, title, description, qamount, level):
        self.title = title
        self.decription = description
        self.qamount = 0
        self.level = 0

    def create_newtest(self):# метод створює новий тест

    def add(self, type):# метод додає нове питання у тест

    def remove(self, number):# метод видаляє певне питання з тесту

    def edit(self, number):# метод редагує питання

    def display(self):# метод виводить тест для проходження

    def save_result(self):# метод збергігає результат проходження тесту

    def save_test(self):# метод зберігає усі зміни адміністратором
