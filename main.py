from school import School
from person import Student,Teacher
from subject import Subject
from classroom import Classroom


school = School("ABC","Dhaka")

eight = Classroom("eight")
nine = Classroom("nine")
ten = Classroom("ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student('Rahim',eight)
karim = Student('karim',nine)
abul = Student('abul',ten)
bokul = Student('bokul',ten)

school.student_addmission(rahim)
school.student_addmission(karim)
school.student_addmission(abul)
school.student_addmission(bokul)


babul = Teacher("babul Khan")
arif = Teacher("arif Khan")
shovon = Teacher("shovon Khan")

bangla = Subject("Bangla",babul)
phycics = Subject("phycics",arif)
english = Subject("english",babul)
chemistry = Subject("chemistry",shovon)


eight.add_subject(bangla)
eight.add_student(phycics)
eight.add_subject(chemistry)
nine.add_subject(bangla)
nine.add_subject(english)
ten.add_subject(chemistry)
ten.add_subject(bangla)

eight.take_semester_final()

print(school)
