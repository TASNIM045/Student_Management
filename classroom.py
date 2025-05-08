class Classroom:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self,student):
        rool_no = f"{self.name}-{len(self.students)+1}"
        student.id = rool_no
        self.students.append(student)

    def add_subject(self,subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for sub in self.subjects:
            sub.eaxm(self.students)
        for stu in self.students:
            stu.final_grade()
