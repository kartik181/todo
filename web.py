import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My TO-DO App")
st.subheader("This is my todo app")
st.write("This app is built using Streamlit")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=f"{todo.strip()}_{index}")
    if checkbox:
        todos.pop(index) 
        functions.write_todos(todos)
        del st.session_state[f"{todo.strip()}_{index}"]
        
        st.rerun()
        
st.text_input(
    label="New Todo",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo"
)
