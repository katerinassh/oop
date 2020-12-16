import os
import test


class Manager:
    def __init__(self):
        self.current_test = None

    def create_new_test(self):  # метод створює новий тест
        print('Input name of test and description in different rows')
        name_of_test = input()
        description = input()
        self.current_test = test.Test(name_of_test, description)
        self.current_test.workTestFile()
        self.current_test.createAnswerFile()

    def display(self):  # метод виводить тест для проходження
        self.current_test.passingTest()

    def open(self):
        print('Input name of test')
        name_of_test = input()
        file = open('{}.txt'.format(name_of_test), 'r')
        title = file.readline().strip('\n')
        description = file.readline().strip('\n')
        temp = file.readline()
        self.current_test = test.Test(title, description)
        self.current_test.readFromFile(file)

    @staticmethod
    def delete():
        print('Input name of test what should be removed')
        name = input()
        os.remove('{}.txt'.format(name))
        os.remove('{}_answers.txt'.format(name))
        print("File Removed!")


man = Manager()
man.create_new_test()
man.current_test.add('QstName')
man.current_test.add('QstEnterText')
man.current_test.add('QstTableOne')
man.current_test.add('QstScale')
man.current_test.workTestFile()
#man.delete()
#man.open()

