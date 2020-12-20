import os
import test
import feedback


class Manager:
    def __init__(self):
        self.current_test = None
        self.feedback = None

    def create_new_test(self):  # метод створює новий тест
        print('Input name of test and description in different rows')
        name_of_test = input()
        description = input()
        self.current_test = test.Test(name_of_test, description)
        self.current_test.workTestFile()
        self.current_test.createAnswerFile()
        self.feedback = feedback.Feedback(name_of_test, self.current_test.qamount)

    def display(self):  # метод виводить тест для проходження
        self.current_test.passingTest()

    def open(self):
        print('Input name of test')
        name_of_test = input()
        file = open('{}.txt'.format(name_of_test), 'r')
        title = file.readline().strip('\n')
        description = file.readline().strip('\n')
        _ = file.readline()
        self.current_test = test.Test(title, description)
        self.current_test.readFromFile(file)
        self.feedback = feedback.Feedback(name_of_test, self.current_test.qamount)

    @staticmethod
    def delete():
        print('Input name of test what should be removed')
        name = input()
        os.remove('{}.txt'.format(name))
        os.remove('{}_answers.txt'.format(name))
        print("File Removed!")

    def ConsoleView(self):
        print('Welcome to program. Created by SulfurTech, Katerina Shakiryanova, Valeria Didych.')
        print('''
\tCommands:
help - to show this info
del - to delete Test and Answers files by input name
open - to open file by input name
new - to create new Test file
exit - to close program
\t(Test need to be opened before)
pass - to pass current Test 
add - to add qst to current Test
edit - to rewrite qst with number
remove - to delete qst in Test
save - to save changes
sort by mark - to create new mark-sorted file with answers
sort by name - to create new name-sorted file with answers
statistic by mark - to create new file with statistic''')
        print('\nInput command',end = '\n')
        while True:
            command = input()
            if command == "new":
                self.create_new_test()
            elif command == "help":
                print('''
\tCommands:
help - to show this info
del - to delete Test and Answers files by input name
open - to open file by input name
new - to create new Test file
exit - to close program
\t(Test need to be opened before)
pass - to pass current Test 
add - to add qst to current Test
edit - to rewrite qst with number
remove - to delete qst in Test
save - to save changes
sort by mark - to create new mark-sorted file with answers
sort by name - to create new name-sorted file with answers
statistic by mark - to create new file with statistic''')
                continue
            elif command == "del":
                self.delete()
                continue
            elif command == "open":
                self.open()
            elif command == "pass":
                self.display()
            elif command == "exit":
                break
            elif command == "add":
                print('Input type of Qst')
                type = input()
                self.current_test.add(type)
            elif command == "edit":
                print('Input number of Qst to edit')
                num = int(input())
                self.current_test.rewrite(num)
            elif command == "remove":
                print('Input number of Qst to delete')
                num = int(input())
                self.current_test.remove(num)
            elif command == "save":
                self.current_test.workTestFile()
            elif command == "sort by name":
                self.feedback.sort_by_name()
            elif command == "sort by mark":
                self.feedback.sort_by_mark()
            elif command == "statistic by mark":
                self.feedback.statistic_by_mark(self.current_test.total_mark)
            elif command == "filter":
                print('Input mark')
                limit = float(input())
                print('Input "less" or "more"')
                Or = input()
                self.feedback.filter_by_mark(limit, Or)
            else:
                print('Invalid command')
                continue
            print("Done!")


