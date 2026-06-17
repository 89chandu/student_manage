import streamlit as st
import pandas as pd

from student import Student
from student_manager import StudentManager


st.title("🎓 🎓 Student Management System")

manager = StudentManager()

menu = st.sidebar.selectbox(
    "Select Option",
    [
       "Add Student", 
       "View Student", 
       "Search Student", 
       "Update Student", 
       "Delete Student"
    ]
)

# Add Student

if menu == "Add Student":


    st.header("Add Student")

    student_id = st.text_input("Student ID")
    name = st.text_input("Name")
    age = st.number_input("Age")
    course = st.text_input("Course")

    # st.button("Remove")
    # st.audio_input("audio")
    # st.color_picker("pick colur")
    # st.file_uploader("file upload")
    
   

    if st.button("Add"):

        student = Student(
            student_id,
            name,
            age,
            course
        )

        manager.add_student(student)

        st.success("Student Added Successfully") 
# View Student

elif menu == "View Student":
    st.header("Student List") 

    students = manager.get_student()

    data = []

    for s in students:
        data.append({

            "ID":s.student_id,
            "Name":s.name,
            "Age":s.age,
            "Course":s.course
        })

        if data:
            st.dataframe(pd.DataFrame(data))
        else:
            st.warning("No Students Found")  

# Search Student    

elif menu == "Search Student":
    st.header("Search Student")  

    student_id = st.text_input("Enter Student ID:")

    if st.button("Search"):

        student = manager.search_student(student_id)

        if student:

            st.success("Student Found")

            st.write("ID:",student.student_id)
            st.write("Name:",student.name)
            st.write("Age:",student.age)
            st.write("Course:",student.course)

        else:
            st.error("Student Not Found")    

#Update Student

elif menu ==  "Update Student":

    st.header("Update Student")

    student_id = st.text_input("Student ID :")

    student = manager.search_student(student_id)

    if student:

        name = st.text_input(
            "Name",
            student.name
        )

        age = st.number_input(
            "Age",
            student.age
        )

        course = st.text_input(
            "Course",
            student.course
        )

        if st.button("Update"):

            manager.update_student (
                student_id,
                name,
                age,
                course

            )

            st.success("Student Updated")



#Delete Student

elif menu == "Delete Student":

    st.header("Delete Student")

    student_id = st.text_input("Student ID")

    if st.button("Delete"):
        manager.delete_students(student_id)
        st.success("Student Deleted")
    else:
        st.error("not")    








