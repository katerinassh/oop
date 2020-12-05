class Sort:
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
            elif left[l] <= right[r]:
                the_input[i] = left[l]
                l += 1
            elif left[l] > right[r]:
                the_input[i] = right[r]
                r += 1

    def recursion(self, the_input, first, last):
        if first < last:
            middle = first + (last - first) // 2
            Sort.recursion(the_input, first, middle)
            Sort.recursion(the_input, middle + 1, last)
            Sort.merge(the_input, first, middle, last)

    def merge_sort(self, the_input):
        Sort.recursion(the_input, 0, len(the_input) - 1)


class Feedback:  # клас-звіт, що надає статистичні дані
    def __init__(self, test_title, qst_amount):
        self.test_title = test_title
        self.qst_amount = qst_amount

    def sort_by_name(self, file, qst_amount):  # створює новий файл, де респонденти відсортовані по іменам
        # *file = "answs.txt"
        new_file = open("name-sorted.txt", "w")
        data_file = open(file, "r")

        data = data_file.readlines()
        data_file.close()

        arr_names = []
        block = (qst_amount * 3) + 5
        for i in range(2, len(data), block):
            name = str(data[i]).strip("\n")
            mark = str(data[i + (qst_amount * 3) + 2]).strip("\n")
            arr_names.append(name + ", " + mark)
            if (len(data) - i) < (2 * block):
                break

        s = Sort()
        s.merge_sort(arr_names)
        for j in range(len(arr_names)):
            new_file.write(arr_names[j] + "\n")

        new_file.close()

    def sort_by_mark(self, file, qst_amount):  # створює новий файл, де респонденти відсортовані по балам
        # *file = "answs.txt"
        new_file = open("mark-sorted.txt", "w")
        data_file = open(file, "r")

        data = data_file.readlines()
        data_file.close()

        arr_marks = []
        block = (qst_amount * 3) + 5
        for i in range(2, len(data), block):
            name = str(data[i]).strip("\n")
            mark = str(data[i + (qst_amount * 3) + 2]).strip("\n")
            arr_marks.append(mark + ", " + name)
            if (len(data) - i) < (2 * block):
                break

        s = Sort()
        s.merge_sort(arr_marks)
        for j in range(len(arr_marks)):
            new_file.write(arr_marks[j] + "\n")

        new_file.close()

    def filter_by_mark(self, ):
        return

    def find(self):
        return

    def statistic_by_mark(self):
        return
