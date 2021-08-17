class Student:
    total = 0
    percentage = 0
    divison = ''
    def student_mark(self):
        nep = int(input("Enter nepali marks: "))
        eng = int(input("Enter english marks: "))
        sci = int(input("enter science marks: "))
        self.total += nep + eng + sci
        self.percentage += self.total / 3

    # def total_marks(self):
    #     print(f"total marks: {self.total}")

    def div(self):
        # divison = ''
        if self.percentage > 35 and self.percentage < 45:
            self.divison += 'third'
        elif self.percentage > 45 and self.percentage< 60:
            self.divison += 'second'
        elif self.percentage > 60 and self.percentage< 75:
            self.divison += 'first'
        elif self.percentage > 75 and self.percentage< 100:
            self.divison += 'distinction'
        else:
            self.divison += 'Fail'
        # print(f"Divison: {divison}")

    def result(self):
        self.student_mark()
        self.div()
        print(f"total marks: {self.total}")
        print(f"Percentage: {self.percentage}")
        print(f"divison: {self.divison}")



obj = Student()
obj.result()
