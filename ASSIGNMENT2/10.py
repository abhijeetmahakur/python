# The student information is stored using a combination of different Python data structures:
# • List – contains marks of students in different subjects.
# • Tuple – stores a student’s information such as (ID, Name).
# • Set – keeps track of unique skills a student has (e.g., ”Python”, ”Java”, ”C”,
# ”C#”, ”C++”).
# • Dictionary – represents a full student profile with keys like ”info”, ”marks”,
# and ”skills”.
# You are given a list of such student profiles (each represented as a dictionary). Write
# a Python function that processes this data and performs the following tasks:
# • Calculate and display the average marks of each student.
# • Count the total occurrences of each skill across all students (e.g., how many
# students know Python, Java, etc.).
# • Identify and display the top-performing student based on average marks.
# Input: A list of student profiles represented as dictionaries, each containing ”info”,
# ”marks”, and ”skills”.
# Output: Display the average marks of each student, the overall skill frequency, and
# the name of the top-performing student.

students = [
    {"info": (1, "Amit"), "marks": [85, 90, 78], "skills": {"Python", "Java"}},
    {"info": (2, "Neha"), "marks": [92, 88, 95], "skills": {"C++", "Python"}},
    {"info": (3, "Ravi"), "marks": [70, 75, 80], "skills": {"Java", "C#"}},
    {"info": (4, "Sanya"), "marks": [88, 92, 85], "skills": {"Python", "C++"}},
           ]
def process_student(student_list):
    skill_count={}
    top_student=None
    top_avg=-1
    for student in student_list:
        name=student['info'][1]
        marks=student['marks']
        avg=sum(marks)/len(marks)
        print(f'{name}:{avg}')

        if avg>top_avg:
            top_avg=avg
            top_student=name
        for ch in student['skills']:
            skill_count[ch]=skill_count.get(ch,0)+1
    for skill,count in skill_count.items():
        print(f'{skill}:{count}')
    print('Top performing student is',top_student,' with marks :',top_avg)



print(process_student(students))