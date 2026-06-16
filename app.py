import streamlit as st
import pandas as pd

from student import Student
from student_manager import StudentManager


st.title("🎓 Student Management System")

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







