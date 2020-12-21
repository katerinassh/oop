import os
import test
import feedback


class Manager:
    def __init__(self):
        self.current_test = None
        self.feedback = None
        self.access = False

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
        _ = file.readline()
        self.current_test = test.Test(title, description)
        self.current_test.readFromFile(file)

    def upd_feedback(self):
        self.feedback = feedback.Feedback(self.current_test.title, self.current_test.qamount)

    @staticmethod
    def delete():
        print('Input name of test what should be removed')
        name = input()
        os.remove('{}.txt'.format(name))
        os.remove('{}_answers.txt'.format(name))
        print("File Removed!")

    def console_view(self):
        print('Welcome to program. Created by Sierov Ivan, Katerina Shakiryanova, Valeria Didych.')
        print('''
\tCommands:
help - to show this info
del - to delete Test and Answers files by input name
open - to open file by input name
new - to create new Test file
exit - to close program
\t(Test need to be opened or saved before)
pass - to pass current Test 
add - to add qst to current Test
edit - to rewrite qst with number
remove - to delete qst in Test
save - to save changes
sort by mark - to create new mark-sorted file with answers
sort by name - to create new name-sorted file with answers
statistic by mark - to create new file with statistic''')
        print('\nInput command', end='\n')
        while True:
            command = input()
            if command == "help":
                print('''
            \tCommands:
            help - to show this info
            del - to delete Test and Answers files by input name
            open - to open file by input name
            new - to create new Test file
            exit - to close program
            \t(Test need to be opened or created before)
            pass - to pass current Test 
            add - to add qst to current Test
            edit - to rewrite qst with number
            remove - to delete qst in Test
            save - to save changes
            sort by mark - to create new mark-sorted file with answers
            sort by name - to create new name-sorted file with answers
            statistic by mark - to create new file with statistic''')
                continue
            elif command == "new":
                self.access = False
                self.create_new_test()
                self.upd_feedback()
            elif command == "del":
                self.delete()
                continue
            elif command == "open":
                self.access = True
                self.open()
                self.upd_feedback()
            elif command == "pass":
                if self.access:
                    self.display()
                else:
                    print('You need to save or open Test')
            elif command == "exit":
                break
            elif command == "add":
                self.access = False
                print('Input type of Qst')
                type = input()
                self.current_test.add(type)
            elif command == "edit":
                self.access = False
                print('Input number of Qst to edit')
                num = int(input())
                self.current_test.rewrite(num)
            elif command == "remove":
                self.access = False
                print('Input number of Qst to delete')
                num = int(input())
                self.current_test.remove(num)
            elif command == "save":
                self.access = True
                self.current_test.workTestFile()
                self.upd_feedback()
            elif command == "sort by name":
                if self.access:
                    self.feedback.sort_by_name()
                else:
                    print('You need to save or open Test')
            elif command == "sort by mark":
                if self.access:
                    self.feedback.sort_by_mark()
                else:
                    print('You need to save or open Test')
            elif command == "statistic by mark":
                if self.access:
                    self.feedback.statistic_by_mark(self.current_test.total_mark)
                else:
                    print('You need to save or open Test')
            elif command == "filter":
                if self.access:
                    print('Input mark')
                    limit = float(input())
                    print('Input "less" or "more"')
                    Or = input()
                    self.feedback.filter_by_mark(limit, Or)
                else:
                    print('You need to save or open Test')
            else:
                print('Invalid command')
                continue
            print("Done!")


