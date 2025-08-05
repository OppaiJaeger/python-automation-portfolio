"""CLI To-Do Lists"""

import os

LOGFILE = "tasks.txt"

def get_task():
    """ Prompt until a valid string is entered and return it."""
    while True:
        new_task = input("\nEnter a task description : ").strip()
        if new_task:
            return new_task

def view_tasks(task_list):
    """ Prints all tasks in order."""
    if task_list:
        print("\nYou have " + str(len(task_list))+ " tasks: ")
        for index,value in enumerate(task_list):
            print(str(index + 1) + ". " + value)

def confirm_continue():
    """Ask whether to continue; return True to continue."""
    while True:
        answer = input("\nDo want to add another task? or delete a task?(y/n/d): ").strip().lower()
        if answer.startswith("y"):
            return True
        if answer.startswith("n"):
            return False
        if answer.startswith("d"):
            return "d"
        print("Please answer y or n or d.")

def log_task(task):
    """Append a new task with a line number to the file."""
    line_number = 1
    if os.path.exists(LOGFILE):
        with open(LOGFILE, "r", encoding="utf8") as file:
            lines = [line for line in file if line.strip() and not line.startswith("#")]
            line_number = len(lines) + 1

    with open(LOGFILE, "a", encoding="utf8") as file:
        if line_number == 1:
            file.write("# Global Task List\n")
        file.write(f"{line_number}. {task}\n")

def add_new_task(task_list):
    """ Append a new task to the list."""
    new_task = get_task()
    task_list.append(new_task)
    print("\nTask added!")
    log_task(new_task)

def load_tasks():
    """Load tasks from the file if it exists, ignoring header."""
    tasks = []
    if os.path.exists(LOGFILE):
        with open(LOGFILE, "r", encoding="utf8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(". ", 1)
                if len(parts) == 2:
                    tasks.append(parts[1])
    else:
        print("\nYour list is empty!")
    return tasks

def delete_task(task_list):
    """Remove a task by number."""
    if not task_list:
        print("\nYour list is empty!")
        return

    view_tasks(task_list)
    while True:
        try:
            deltasknum = int(input("\nEnter the task number to delete: "))
            if 1 <= deltasknum <= len(task_list):
                removed = task_list.pop(deltasknum - 1)
                print(f"Deleted task: {removed}")
                update_log_file(task_list)
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def update_log_file(task_list):
    """Rewrites the log file with current tasks."""
    with open(LOGFILE, "w", encoding="utf8") as file:
        file.write("# Global Task List\n")
        for idx, task in enumerate(task_list):
            file.write(f"{idx + 1}. {task}\n")

def main():
    """Main function."""
    print("\nWelcome to the CLI To-Do Lists!")
    task_list = load_tasks()
    view_tasks(task_list)
    while True :

        if not task_list :
            add_new_task(task_list)
            view_tasks(task_list)

        answer = confirm_continue()
        if not answer:
            print("\nGoodbye!")
            break
        if answer == "d":
            delete_task(task_list)
            continue

        add_new_task(task_list)
        view_tasks(task_list)



if __name__ == "__main__":
    main()
