import tkinter as tk
from tkinter import messagebox
import pickle
import os

# Создаем основное окно
root = tk.Tk()
root.title("Мои задачи")

# Путь к файлу, где будут храниться задачи
tasks_file = "tasks.pkl"


def load_tasks():
    """Загрузка задач из файла, если файл существует."""
    if os.path.exists(tasks_file):
        with open(tasks_file, "rb") as file:
            tasks = pickle.load(file)
            for task in tasks:
                task_listBox.insert(tk.END, task)

def save_tasks():
    """Сохранение задач в файл."""
    tasks = list(task_listBox.get(0, tk.END))
    with open(tasks_file, "wb") as file:
        pickle.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()  # Сохраняем задачи после добавления

def add_task_enter(event=None):
    task = task_entry.get().strip()
    if task:
        task_listBox.insert(tk.END, task)  # Исправлено с task_listbox на task_listBox
        task_entry.delete(0, tk.END)  # Очистить поле ввода
        save_tasks()  # Сохраняем задачи после добавления
    else:
        messagebox.showwarning("Предупреждение", "Введите задачу!")

def delete_task():
    try:
        selected_task_index = task_listBox.curselection()[0]
        task_listBox.delete(selected_task_index)
        save_tasks()  # Сохраняем задачи после удаления
    except IndexError:
        pass

def mark_task():
    try:
        selected_task_index = task_listBox.curselection()[0]
        task = task_listBox.get(selected_task_index)
        completed_listBox.insert(tk.END, task)
        task_listBox.delete(selected_task_index)
        save_tasks()  # Сохраняем задачи после отметки
    except IndexError:
        pass

def clear_tasks():
    """Очистка всех задач из списков и файла."""
    task_listBox.delete(0, tk.END)
    completed_listBox.delete(0, tk.END)

    # Удаляем файл с задачами
    if os.path.exists(tasks_file):
        os.remove(tasks_file)

# Создаем текстовое поле для ввода задачи
task_entry = tk.Entry(root, width=52)
task_entry.grid(row=0, column=0, columnspan=2, pady=10)

# Привязываем нажатие клавиши Enter к функции добавления задачи
task_entry.bind("<Return>", add_task_enter)

# Создаем и позиционируем кнопку для добавления задачи
add_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_button.grid(row=1, column=0, pady=5)

# Создаем и позиционируем кнопку для удаления задачи
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.grid(row=1, column=1, pady=5)

# Создаем и позиционируем кнопку, которая будет отмечать задачу выполненной
mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.grid(row=2, column=0, padx=10, pady=10)

# Создаем и позиционируем кнопку для очистки списка
clear_button = tk.Button(root, text="Очистить список", command=clear_tasks)
clear_button.grid(row=2, column=1, padx=10, pady=10)

# Добавляем и позиционируем надпись, чтобы у списка задач был заголовок
text2 = tk.Label(root, text="Список задач:", bg="grey74")
text2.grid(row=4, column=0, padx=5, pady=5)

# Создаем список, в который будут добавляться задачи
task_listBox = tk.Listbox(root, height=10, width=25, bg="alice blue")
task_listBox.grid(row=5, column=0, padx=5, pady=5)

# Добавляем и позиционируем надпись для списка выполненных задач
text3 = tk.Label(root, text="Выполненные задачи:", bg="grey74")
text3.grid(row=4, column=1, padx=10, pady=5)

# Создаем второй список для выполненных задач
completed_listBox = tk.Listbox(root, height=10, width=25, bg="LavenderBlush4")
completed_listBox.grid(row=5, column=1, padx=10, pady=10)

# Загружаем задачи при старте программы
load_tasks()

root.mainloop()
