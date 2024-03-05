import json
import hashlib
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import os

def register():
    global username_entry, password_entry, username
    with open('credentials.json') as file:
        credentials = json.load(file)

    username = username_entry.get()
    password = password_entry.get()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in credentials:
        messagebox.showerror('Ошибка', 'Пользователь с таким именем уже существует.')
    else:
        credentials[username] = hashed_password
        with open('credentials.json', 'w') as file:
            json.dump(credentials, file)
        messagebox.showinfo('Успех', 'Регистрация прошла успешно!')

def login():
    global username_entry, password_entry, username
    with open('credentials.json') as file:
        credentials = json.load(file)

    username = username_entry.get()
    password = password_entry.get()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in credentials and hashed_password == credentials[username]:
        messagebox.showinfo('Успех', 'Вход выполнен успешно!')
    else:
        messagebox.showerror('Ошибка', 'Неверное имя пользователя или пароль.')

def create_text_file(username, filename):
    user_folder = os.path.join('texts', username)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    file_path = os.path.join(user_folder, filename)
    with open(file_path, 'w') as file:
        file.write('')

def edit_text_file(username, filename, content):
    user_folder = os.path.join('texts', username)
    file_path = os.path.join(user_folder, filename)
    with open(file_path, 'w') as file:
        file.write(content)

def delete_text_file(username, filename):
    user_folder = os.path.join('texts', username)
    file_path = os.path.join(user_folder, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("Файл не существует")

def open_text_file(username, filename, content_entry):
    user_folder = os.path.join('texts', username)
    file_path = os.path.join(user_folder, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            content_entry.delete(1.0, tk.END)  # Очистить поле содержимого
            content_entry.insert(tk.END, content)
    else:
        messagebox.showerror('Ошибка', 'Файл не существует')

def main():
    global username_entry, password_entry, username
    root = tk.Tk()
    root.title('Система')
    root.geometry('400x500')

    welcome_label = tk.Label(root, text='Добро пожаловать в систему', font=('Arial', 14))
    welcome_label.pack(pady=20)

    label_username = tk.Label(root, text='Имя пользователя:')
    label_username.pack()

    username_entry = tk.Entry(root)
    username_entry.pack()

    label_password = tk.Label(root, text='Пароль:')
    label_password.pack()

    password_entry = tk.Entry(root, show='*')
    password_entry.pack()

    label_filename = tk.Label(root, text='Имя файла:')
    label_filename.pack()

    filename_entry = tk.Entry(root)
    filename_entry.pack()

    label_content = tk.Label(root, text='Содержимое:')
    label_content.pack()

    content_entry = tk.Text(root, height=5, width=30)
    content_entry.pack()

    register_button = tk.Button(root, text='Зарегистрироваться', command=register, bg='green', fg='white')
    register_button.pack(pady=10)

    login_button = tk.Button(root, text='Войти', command=login, bg='blue', fg='white')
    login_button.pack()

    filename_label = tk.Label(root, text='Имя файла:')
    filename_label.pack()

    filename_entry = tk.Entry(root)
    filename_entry.pack()

    content_label = tk.Label(root, text='Содержимое:')
    content_label.pack()

    content_entry = tk.Text(root, height=5, width=30)
    content_entry.pack()

    create_file_button = tk.Button(root, text='Создать файл',
                                   command=lambda: create_text_file(username, filename_entry.get()), bg='orange')
    create_file_button.pack()

    edit_file_button = tk.Button(root, text='Редактировать файл',
                                 command=lambda: edit_text_file(username, filename_entry.get(),
                                                                content_entry.get("1.0", "end-1c")), bg='yellow')
    edit_file_button.pack()

    delete_file_button = tk.Button(root, text='Удалить файл',
                                   command=lambda: delete_text_file(username, filename_entry.get()), bg='red',
                                   fg='white')
    delete_file_button.pack()

    open_file_button = tk.Button(root, text='Открыть файл',
                                 command=lambda: open_text_file(username, filename_entry.get(), content_entry),
                                 bg='purple')
    open_file_button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
