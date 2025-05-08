class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teachers = {} # {"subject_name" : teacher_object}
        self.classrooms = {} # {"class_no" : class_object}

        def add_classroom(self,classroom):
            self.classrooms[classroom.name] = classroom

        def add_teacher(self,subject,teacher):
            self.teachers[subject] = teacher
        
        def student_addmission(self,student):
            classname = student.classroom.name
            self.classrooms[classname].add_student(student)

        @staticmethod
        def calculate_grade(marks):
            if marks>=80 and marks <=100:
                return 'A+'
            elif marks>=70 and marks<80:
                return 'A'
            elif marks>=60 and marks<70:
                return 'A-'
            elif marks>=50 and marks<60:
                return 'B'
            elif marks>=40 and marks<50:
                return 'C'
            elif marks>=33 and marks<40:
                return 'D'
            else:
                return 'F'
        
        @staticmethod
        def grade_to_value(grade):
            grade_map = {
                'A+' : 5.00,
                'A' : 4.00,
                'A-' : 3.50,
                'B' : 3.00,
                'C' : 2.00,
                'D' : 1.00,
                'F' : 0.00
            }
            return grade_map[grade]
        
        @staticmethod
        def value_to_grade(value):
            if value >= 4.50 and value <= 5.0:
                return 'A+'
            elif value >= 3.50 and value < 4.50:
                return 'A'
            elif value >= 3.00 and value < 3.50:
                return 'A-'
            elif value >= 2.50 and value < 3.00:
                return 'B'
            elif value >= 2.00 and value < 2.50:
                return 'C'
            elif value >= 1.00 and value < 2.00:
                return 'D'
            else:
                return 'F'
            
    def __repr__(self):
        for k in self.classrooms.keys():
            print(k)
        
        print("All Students : ")
        result = ''
        for k,v in self.classrooms.items():
            result += f"---{k.upper()} Classroom Student\n"
            for student in v.students:
                result += f"{student.name}\n"
        print(result)

        subject = ''
        for k,v in self.classrooms.items():
            subject += f"---{k.upper()} Classroom Subjects\n"
            for subject in v.subjects:
                subject += f"{subject.name}\n"
        print(subject)

        print("Student Results : ")
        for k,v in self.classrooms.items():
            for student in v.students:
                for i,j in student.marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.final_grade())
        
        return ""