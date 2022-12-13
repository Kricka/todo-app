from functions import get_todos,write_todos
import time


now=time.strftime("%b %d,%Y , %H:%M:%S")
print('We will display time!')
print("Hi, today is: ",now)
while True:
    user_action=input("Type add,show, edit, complete or exit")
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo=user_action[4:]

        todos=get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos=get_todos()

        for index, item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number=int(user_action[5:])
            number=number-1


            todos=get_todos()

            new_todo = input("Enter new todo: ")
            todos[number]=new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Yor command is not valid!')
            continue



    elif user_action.startswith('complete'):
        try:
            com_num=int(user_action[9:])
            com_num=com_num-1
            todos=get_todos()

            todo_to_remove=todos[com_num].strip('\n')
            todos.remove(todos[com_num])

            write_todos(todos)

            message=f"Todo {todo_to_remove} was removed from the list."

            print(message)
        except IndexError:
            print('Imputed index is not valid!')
        except ValueError:
            print('Your command is not valid!')

            continue



    elif user_action.startswith('exit'):
        break
print("Bye!")
