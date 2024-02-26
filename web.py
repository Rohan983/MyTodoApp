import streamlit as st
import functions

todos = functions.readfile()


def add_todo():
    td = st.session_state['new_todo']
    todos.append(td + '\n')
    functions.writefile(todos)


st.title('My ToDo App')
st.subheader('This is my ToDo App')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writefile(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder='Add new ToDo',
              on_change=add_todo, key='new_todo')
