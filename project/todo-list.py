from datetime import datetime
import json
# create class

class TodoList:
    # create constructor
    def __init__(self):
        self.tasks = [] # default value for tasks
        self.file_name = "task.json" # default value for file name
        self.load_tasks() # load tasks from file when the instance is created

    # adding task
    def add_task(self, description):
        """Add a new task to the todo list"""
        
        task = {
            "id" : len(self.tasks) + 1, # generate id based on the number of tasks
            "description" : description,
            "completed" : False,
            "created_at" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }   
        self.tasks.append(task)
        self.save_tasks() # save tasks to file after adding a new task
        print(f"Task {task['id']}: {description} added to the todo list.")
        
    # viewing tasks
    def view_tasks(self):
        """Display all tasks"""
        
        if not self.tasks:
            print("No tasks in the todo list.")
            return
        
        print("Todo List:")
        print("-" * 50)
        for task in self.tasks:
            status = "✅" if task['completed'] else " "

            # 1. [✅] build todo list app
            # 2. [ ] learn python
            print(f'{task['id']}. [{status}] {task['description']} (Created at: {task['created_at']})')
        print("-" * 50)
        
    # mark task as completed    
    def mark_completed(self, task_id):
        """Mark a task as completed"""
        
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks() # save tasks to file after marking a task as completed
                print(f"Task {task_id} marked as completed.")
                return
        
        print(f"Task {task_id} not found.")
        
    # delete task    
    def del_task(self, task_id):
        """Delete a task from the todo list"""
        
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks() # save tasks to file after deleting a task
                print(f"Task {task_id} deleted from the todo list.")
                return
        
        print(f"Task {task_id} not found.")
        
    # save tasks to file
    def save_tasks(self):
        """Save tasks to a JSON file"""
        
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)
        print(f"Tasks saved to {self.file_name}.")
        
    # load tasks from file
    def load_tasks(self):
        """Load tasks from a JSON file"""
        
        try:
            with open(self.file_name, 'r') as file:
                self.tasks = json.load(file)
            print(f"Tasks loaded from {self.file_name}.")
        except FileNotFoundError:
            print(f"No existing task file found. Starting with an empty todo list.")

def main():
    todo = TodoList() # create an instance of TodoList
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            todo.add_task(description)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.view_tasks() 
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo.mark_completed(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.del_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '5':
            print("Exiting the Todo List application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
if __name__ == "__main__":
    
    main()
    
    # todo_list = TodoList() # create an instance of TodoList
    
    # add tasks to the todo list and view them
    # todo_list.add_task("Buy groceries") # add task to the todo list
    # todo_list.add_task("Finish homework") # add task to the todo list
    
    # save tasks to file
    # todo_list.save_tasks() # save tasks to a JSON file
    
    # load tasks from file and view them
    # todo_list.load_tasks() # load tasks from a JSON file
    
    # view tasks in the todo list
    # todo_list.view_tasks() # view tasks in the todo list
    
    # # mark tasks as completed and view them
    # todo_list.mark_completed(1) # mark task with id 1 as completed
    # todo_list.mark_completed(2) # mark task with id 2 as completed
    # todo_list.view_tasks() # view tasks in the todo list after marking as completed
    
    # # delete tasks and view them
    # todo_list.del_task(1) # delete task with id 1 from the todo list
    # todo_list.del_task(2) # delete task with id 2 from the todo list
    # todo_list.view_tasks() # view tasks in the todo list after deletion
    
    