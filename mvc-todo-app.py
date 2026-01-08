
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Task manager")
        self.geometry("500x380")
        self.columnconfigure(0, weight=1)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.data_manager = DataManager()
        self.app_controlling = AppController()

        # root menu
        self.application_menu = tk.Menu(self)
        self.configure(menu=self.application_menu)

        self.file_menu = tk.Menu(self.application_menu)
        self.file_menu.add_command(label="Save file", command=self.app_controlling.save_file)
        self.file_menu.add_command(label="Open file", command=self.app_controlling.load_file)

        self.application_menu.add_cascade(label="File", menu=self.file_menu)

        # frame creation
        self.user_input_frame = UserInputFrame(self,
                                               controller=self.app_controlling)
        self.user_input_frame.grid(row=0, column=0, pady=20)
        self.app_controlling.user_input_frame = self.user_input_frame

        self.task_frame = TaskFrame(self,
                                    controller=self.app_controlling)
        self.task_frame.grid(row=1, column=0, pady=10)
        self.app_controlling.task_frame = self.task_frame

        self.user_input_frame.task_treeview = self.task_frame.task_treeview


class UserInputFrame(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.task_treeview = None
        self.task = tk.StringVar()

        self.controller = controller

        task_label = ttk.Label(self,
                               text="Task:")
        task_label.grid(row=0, column=0)

        self.task_entry = ttk.Entry(self,
                                    width=60,
                                    textvariable=self.task)
        self.task_entry.grid(row=0, column=1)

        add_task_button = ttk.Button(self,
                                     text="Add Task",
                                     command=self.controller.add_task)
        add_task_button.grid(row=1, column=0, columnspan=2, sticky=tk.EW, pady=2)


class TaskFrame(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.controller = controller

        # treeview creation
        self.task_treeview = ttk.Treeview(self,
                                          selectmode=tk.BROWSE)
        self.task_treeview.grid(row=0, column=0, sticky=tk.EW)

        self.task_treeview.heading("#0", text="Your tasks")
        self.task_treeview.column("#0", width=350)

        task_treeview_scroll = ttk.Scrollbar(self,
                                             orient=tk.VERTICAL,
                                             command=self.task_treeview.yview)
        task_treeview_scroll.grid(row=0, column=1, sticky=tk.NS)
        self.task_treeview.configure(yscrollcommand=task_treeview_scroll.set)

        delete_task_button = ttk.Button(self,
                                        text="Delete selected task",
                                        command=self.controller.remove_task)
        delete_task_button.grid(row=1, column=0, columnspan=2, sticky=tk.EW)


class AppController:
    def __init__(self):
        self.task_frame = None
        self.user_input_frame = None

    def add_task(self):
        if self.user_input_frame.task.get() != "":
            self.task_frame.task_treeview.insert(parent="", index=tk.END, text=self.user_input_frame.task.get())
            self.user_input_frame.task_entry.delete(0, tk.END)
        else:
            print("Please enter task.")

    def remove_task(self):
        selected_item = self.task_frame.task_treeview.selection()
        if selected_item != ():
            self.task_frame.task_treeview.delete(selected_item)
        else:
            print("Please select task.")

    def save_file(self):
        file_name = filedialog.asksaveasfilename(defaultextension=(".txt"),
                                                 initialdir=DataManager.DIRECTORY,
                                                 title="Save file")
        if not file_name:
            return

        # get tasks from treeview
        tasks = [self.task_frame.task_treeview.item(item, "text") for item in
                 self.task_frame.task_treeview.get_children()]

        DataManager.save(file_name, tasks)

    def load_file(self):
        file_name = filedialog.askopenfilename(initialdir=DataManager.DIRECTORY,
                                               title="Open file")

        if not file_name:
            return

        tasks = DataManager.load(file_name)
        for task in tasks:
            self.task_frame.task_treeview.insert("", tk.END, text=task)


class DataManager:
    DIRECTORY = r"Insert your path"

    @staticmethod
    def save(file, tasks):
        with open(file, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")

    @staticmethod
    def load(file):
        tasks = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                task = line.strip()
                if task:
                    tasks.append(task)
        return tasks


root = MainWindow()
root.mainloop()
