import streamlit as st
import functions
import time

todos = functions.get_todos()
blank = ''

def add_todo():
    current_time = time.strftime("%I%M%S")
    todo = current_time + st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.save_todos(todos)
    st.session_state["new_todo"] = blank

st.title("My Todo App")
st.subheader("This is my Todo app")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo[6:], key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(" ",placeholder="Add a new todo ...",
              on_change=add_todo, key="new_todo")