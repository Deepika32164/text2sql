from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('models/gemini-2.0-flash')
    response = model.generate_content(f"{prompt}\n{question}")
    return response.text.strip()

# Function to read SQL data from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except Exception as e:
        rows = [(f"Error executing SQL: {e}",)]
    conn.commit()
    conn.close()
    return rows

# Prompt (use a string, not a list!)
prompt = """
You are an expert in converting English questions to SQL queries!
The SQL database is called STUDENTS and has the following columns - NAME, CLASS, SECTION.

For example:
Example 1 - How many entries of records are present?
The SQL command will be something like: SELECT COUNT(*) FROM STUDENTS;

Example 2 - Tell me all the students studying in Data Science class?
The SQL command will be something like: SELECT * FROM STUDENTS WHERE CLASS='Data Science';

Do not use quotes around the entire query. Do not mention the word 'sql' in the output.
"""

# Streamlit UI
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")
question = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query")
    st.code(response, language="sql")

    data = read_sql_query(response, "students.db")

    st.subheader("The Response is")
    for row in data:
        st.write(row)
# from dotenv import load_dotenv
# load_dotenv()
# import streamlit as st
# import os
# import sqlite3
# import google.generativeai as genai
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# def get_gemini_response(question,prompt):
#     model=genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(f"{prompt}\n{question}") 

#     return response.text
# def read_sql_query(sql,db):
#     conn=sqlite3.connect(db)
#     cur=conn.cursor()
#     cur.execute(sql)
#     rows=cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)
#     return rows
# prompt = ["""
# You are an expert in converting English question to SQL query!
# The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION.

# For example,
# Example 1 - How many entries of records are present?,
# the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;

# Example 2 - Tell me all the students studying in Data Science class?,
# the SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS="Data Science";

# Also, the SQL code should not have " in beginning or end and should not include the word 'sql' in the output.
# """]


# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")
# question=st.text_input("Input: ",key="input")
# submit=st.button("Ask the question")
# if submit:
#     response=get_gemini_response(question,prompt)
#     print(response)
#     data=read_sql_query(response,"students.db")
#     st.subheader("The Response is")
#     for row in data:
#         print(row)
#         st.header()