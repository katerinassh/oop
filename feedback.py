class Feedback:  # клас-звіт, що надає статистичні дані
    def __init__(self, file, qst_amount):
        self.file = file
        self.qst_amount = qst_amount

        data_file = open(self.file, "r")
        self.data = data_file.readlines()
        data_file.close()

        self.block = (self.qst_amount * 3) + 5

    def merge(self, the_input, first, middle, last):
        left = the_input[first:middle + 1]
        right = the_input[middle + 1:last + 1]
        l = r = 0

        for i in range(first, last + 1):
            if l >= len(left):
                the_input[i] = right[r]
                r += 1
            elif r >= len(right):
                the_input[i] = left[l]
                l += 1
            elif float(left[l]) <= float(right[r]):
                the_input[i] = left[l]
                l += 1
            elif float(left[l]) > float(right[r]):
                the_input[i] = right[r]
                r += 1

    def recursion(self, the_input, first, last):
        if first < last:
            middle = first + (last - first) // 2
            self.recursion(the_input, first, middle)
            self.recursion(the_input, middle + 1, last)
            self.merge(the_input, first, middle, last)

    def merge_sort(self, the_input):
        self.recursion(the_input, 0, len(the_input) - 1)

    def sort_by_name(self):  # створює новий файл, де респонденти відсортовані по іменам
        # *self.file = "answs.txt"
        new_file = open("name-sorted.txt", "w")

        arr_names = []
        for i in range(2, len(self.data), self.block):
            name = str(self.data[i]).strip("\n")
            mark = str(self.data[i + (self.qst_amount * 3) + 2]).strip("\n")
            arr_names.append(name + ", " + mark)
            if (len(self.data) - i) < (2 * self.block):
                break

        self.merge_sort(arr_names)
        for j in range(len(arr_names)):
            new_file.write(arr_names[j] + "\n")

        new_file.close()

    def sort_by_mark(self):  # створює новий файл, де респонденти відсортовані по балам
        # *self.file = "answs.txt"
        new_file = open("mark-sorted.txt", "w")

        arr_marks = []
        for i in range(2, len(self.data), self.block):
            name = str(self.data[i]).strip("\n")
            mark = str(self.data[i + (self.qst_amount * 3) + 2]).strip("\n")
            arr_marks.append(mark + ", " + name)
            if (len(self.data) - i) < (2 * self.block):
                break

        self.merge_sort(arr_marks)
        for j in range(len(arr_marks)):
            new_file.write(arr_marks[j] + "\n")

        new_file.close()

    def filter_by_mark(self, limit, less_or_more):  # показує лише результати респондентів в заданих межах балів
        name_newfile = less_or_more + str(limit) + ".txt"
        new_file = open(name_newfile, 'w')

        arr_marks = []
        for i in range(2, len(self.data), self.block):
            name = str(self.data[i]).strip("\n")
            mark = str(self.data[i + (self.qst_amount * 3) + 2]).strip("\n")

            if less_or_more == 'less':
                if mark <= limit:
                    arr_marks.append(mark + ", " + name)
            elif less_or_more == 'more':
                if mark >= limit:
                    arr_marks.append(mark + ", " + name)
            else:
                print("Run the command again and check the spelling.")
                break

        for j in range(len(arr_marks)):
            new_file.write(arr_marks[j] + "\n")

        new_file.close()

    def statistic_by_mark(self, max_mark):  # надає статистику по результатам проходження тесту
        new_file = open("statistic.txt", 'w')

        arr_marks = []
        for i in range(2, len(self.data), self.block):
            mark = int(str(self.data[i + (self.qst_amount * 3) + 2]).strip("\n"))
            arr_marks.append(mark)

        amount_maxmark = arr_marks.count(max_mark)
        average = len(arr_marks) / sum(arr_marks)   # середній бал
        av_procent = (average * 100) / max_mark     # середня успішність у відсотках

        new_file.write("Average mark: " + str(average) + " from " + str(max_mark) + "\n")
        new_file.write("Average success rate in percent: " + str(av_procent) + "%" + "\n")
        new_file.write("Number of excellent tests: " + str(amount_maxmark) + " from " + str(len(arr_marks)))

        new_file.close()
