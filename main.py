import tkinter as tk
from task import Task
from todo import ToDo
todo = ToDo()

class GUI:
    def __init__(self):
        self.root = tk.Tk()
    def main_menu(self):
        self.root.title("ToDO")
        self.root.geometry("500x500+450+100")
        self.root.minsize(300, 300)
        self.root.maxsize(500, 700)
        self.root.resizable(False, False)
        self.root["bg"] = "Black"
        tittle_label = tk.Label(self.root, text="===ToDO===", fg="White", font=("Times New Roman", 50), bg="Black")
        tittle_label.pack()



        def add_tasks():
            self.add_tasks_window = tk.Toplevel(self.root)
            self.add_tasks_window.title("Tasks")
            self.add_tasks_window.geometry("300x300+450+100")
            self.add_tasks_window.minsize(300, 300)
            self.add_tasks_window.maxsize(300, 300)
            self.add_tasks_window.resizable(False, False)
            self.add_tasks_window["bg"] = "Black"

            def exit_window():
                self.add_tasks_window.destroy()

            top_framet = tk.Frame(self.add_tasks_window, bg="White")
            top_framet.pack(side="top", fill="x", padx=10, pady=10)

            labeltask = tk.Label(top_framet, text="State the task: ", font=("Times New Roman", 16))
            labeltask.pack(side="left", padx=5)

            entry_label = tk.Entry(top_framet, font=("Times New Roman", 16))
            entry_label.pack(side="left", padx=5)

            def save_task():
                title = entry_label.get()
                if title.strip() == "":
                    return
                new_task = Task(None, title, False)
                todo.add_task(new_task)
                self.add_tasks_window.destroy()


            exit_button = tk.Button(self.add_tasks_window, text="Exit", font=("Times New Roman", 20), bg="Dimgrey", fg="White", command=exit_window)
            exit_button.pack(side="bottom", fill="x", padx=2, pady=3)
            save_button = tk.Button(self.add_tasks_window, text="Save", font=("Times New Roman", 20), bg="Dimgrey", fg="White", command=save_task)
            save_button.pack(side="bottom", fill="x", padx=2, pady=3)


        def show_all_tasks():
            self.all_tasks_window = tk.Toplevel(self.root)
            self.all_tasks_window.title("All Tasks")
            self.all_tasks_window.geometry("650x650+450+100")
            self.all_tasks_window.minsize(650, 650)
            self.all_tasks_window.maxsize(650, 650)
            self.all_tasks_window.resizable(False, False)
            self.all_tasks_window["bg"] = "Black"
            un_all_tasks = tk.Listbox(self.all_tasks_window, font=("Times New Roman", 20), bg="Silver")

            def show_tasks():
                un_all_tasks.delete(0, tk.END)
                task_list = todo.get_tasks()
                if not task_list:
                    un_all_lable = tk.Label(self.all_tasks_window, text="The list is empty", font=("Times New Roman", 20), bg="Silver")
                    un_all_lable.pack(side="top", fill="x", padx=10, pady=10)
                else:
                    for task in task_list:
                        if task.completed:
                            un_all_tasks.insert(tk.END, f"{task.title} - Completed")
                        else:
                            un_all_tasks.insert(tk.END, f"{task.title} - Uncompleted")
                un_all_tasks.pack(side="top", fill="x", padx=10, pady=10)

            show_tasks()

            def dell_task():
                tasks_to_del = un_all_tasks.curselection()
                index = tasks_to_del[0]
                task = todo.get_tasks()[index]

                if task:
                    todo.delete_task(task)
                else:
                    un_del_lable = tk.Label(self.all_tasks_window, text="Task not found", font=("Times New Roman", 20),
                                            bg="Dimgrey", fg="White")
                    un_del_lable.pack(side="top", fill="x", padx=10, pady=10)
                show_tasks()

            def complete_task():
                tasks_to_complete = un_all_tasks.curselection()
                index = tasks_to_complete[0]
                task = todo.get_tasks()[index]

                if task:
                    task.complete()
                    todo.update_task(task)
                else:
                    un_complete_lable = tk.Label(self.all_tasks_window, text="Task is Incomplete",font=("Times New Roman", 20),bg="Dimgrey", fg="White")
                    un_complete_lable.pack(side="top", fill="x", padx=10, pady=10)
                show_tasks()

            def incomplete_task():
                tasks_to_decomplete = un_all_tasks.curselection()
                index = tasks_to_decomplete[0]
                task = todo.get_tasks()[index]

                if task:
                    task.decomplete()
                    todo.update_task(task)
                else:
                    un_incomplete_lable = tk.Label(self.all_tasks_window, text="Task not found",font=("Times New Roman", 20),bg="Dimgrey", fg="White")
                    un_incomplete_lable.pack(side="top", fill="x", padx=10, pady=10)
                show_tasks()
            def exit_window():
                self.all_tasks_window.destroy()


            exit_button = tk.Button(self.all_tasks_window, text="Exit", font=("Times New Roman", 20), fg="White", bg="Dimgrey", command=exit_window)
            exit_button.pack(side="bottom", fill="x", padx=2, pady=1)
            dell_button = tk.Button(self.all_tasks_window, text="Delete", font=("Times New Roman", 20), bg="Dimgrey",fg="White", command=dell_task)
            dell_button.pack(side="bottom", fill="x", padx=2, pady=1)
            incomplete_button = tk.Button(self.all_tasks_window, text="Mark as Incomplete", font=("Times New Roman", 20), bg="Dimgrey",fg="White", command=incomplete_task)
            incomplete_button.pack(side="bottom", fill="x", padx=2, pady=1)
            complete_button = tk.Button(self.all_tasks_window, text="Complete", font=("Times New Roman", 20), bg="Dimgrey",fg="White", command=complete_task)
            complete_button.pack(side="bottom", fill="x", padx=2, pady=1)






































        def exit_program():
            self.root.destroy()

        exit_button = tk.Button(self.root, text="Exit", font=("Times New Roman", 20), fg="White", bg="Dimgrey", command=exit_program)
        exit_button.pack(side="bottom", fill="x", padx=2, pady=3)
        add_button = tk.Button(self.root, text="Add task", font=("Times New Roman", 20), fg="White", bg="Dimgrey", command=add_tasks)
        add_button.pack(side="bottom", fill="x", padx=2, pady=3)
        show_button = tk.Button(self.root, text="All tasks", font=("Times New Roman", 20), fg="White", bg="Dimgrey",command=show_all_tasks)
        show_button.pack(side="bottom", fill="x", padx=2, pady=3)



gui = GUI()
gui.main_menu()
gui.root.mainloop()