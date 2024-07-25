import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=77, height=30, bd=0, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, font=('Comic Sans MS', 12))
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_task_btn = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(side=tk.LEFT, padx=10)

        self.update_task_btn = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_task_btn.pack(side=tk.LEFT, padx=10)

        self.delete_task_btn = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_btn.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
            self.tasks.append(task)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            updated_task = self.entry.get()
            if updated_task != "":
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, updated_task)
                self.tasks[selected_task_index] = updated_task
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
