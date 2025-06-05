import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime

class DiscordApp:
    def __init__(self, root):  # Исправлено: __init__ вместо init
        self.root = root
        self.root.title("Tkinter Discord")
        self.root.geometry("1000x600")
        
        # Стиль
        self.bg_color = "#36393F"
        self.sidebar_color = "#2F3136"
        self.channel_color = "#40444B"
        self.text_color = "#DCDDDE"
        self.highlight_color = "#7289DA"
        
        self.root.configure(bg=self.bg_color)
        
        # Создание интерфейса
        self.create_widgets()
        
        # Тестовые данные
        self.channels = ["general", "random", "help"]
        self.users = ["User1", "User2", "User3", "User4"]
        self.current_channel = "general"
        self.update_channel_list()
        self.update_user_list()
        
    def create_widgets(self):
        # Левая панель (сервер/каналы)
        self.left_frame = tk.Frame(self.root, bg=self.sidebar_color, width=200)
        self.left_frame.pack(side="left", fill="y")
        self.left_frame.pack_propagate(False)
        
        # Заголовок сервера
        server_label = tk.Label(
            self.left_frame, 
            text="Tkinter Server", 
            bg=self.sidebar_color, 
            fg=self.text_color,
            font=("Arial", 12, "bold"),
            padx=10,
            pady=15,
            anchor="w"
        )
        server_label.pack(fill="x")
        
        # Разделитель
        ttk.Separator(self.left_frame, orient="horizontal").pack(fill="x")
        
        # Каналы
        channel_label = tk.Label(
            self.left_frame, 
            text="TEXT CHANNELS", 
            bg=self.sidebar_color, 
            fg=self.text_color,
            font=("Arial", 10, "bold"),
            padx=10,
            pady=10,
            anchor="w"
        )
        channel_label.pack(fill="x")
        
        self.channel_listbox = tk.Listbox(
            self.left_frame,
            bg=self.sidebar_color,
            fg=self.text_color,
            selectbackground=self.channel_color,
            borderwidth=0,
            highlightthickness=0,
            font=("Arial", 11),
            activestyle="none"
        )
        self.channel_listbox.pack(fill="both", expand=True, padx=5)
        self.channel_listbox.bind("<<ListboxSelect>>", self.on_channel_select)
        
        # Правая панель (чат + пользователи)
        self.right_frame = tk.Frame(self.root, bg=self.bg_color)
        self.right_frame.pack(side="left", fill="both", expand=True)
        
        # Верхняя часть (чат)
        self.chat_frame = tk.Frame(self.right_frame, bg=self.bg_color)
        self.chat_frame.pack(side="left", fill="both", expand=True)
        
        # Заголовок чата
        self.chat_header = tk.Label(
            self.chat_frame, 
            text="#general", 
            bg=self.bg_color, 
            fg=self.text_color,
            font=("Arial", 14, "bold"),
            padx=10,
            pady=10,
            anchor="w"
        )
        self.chat_header.pack(fill="x")
        
        # Разделитель
        ttk.Separator(self.chat_frame, orient="horizontal").pack(fill="x")
        
        # Область сообщений
        self.message_area = scrolledtext.ScrolledText(
            self.chat_frame,
            bg=self.bg_color,
            fg=self.text_color,
            insertbackground=self.text_color,
            font=("Arial", 11),
            wrap="word",
            padx=10,
            pady=10,
            state="disabled"
        )
        self.message_area.pack(fill="both", expand=True)
        
        # Поле ввода сообщения
        self.message_entry = tk.Text(
            self.chat_frame,
            bg=self.channel_color,
            fg=self.text_color,
            insertbackground=self.text_color,
            font=("Arial", 11),
            height=3,
            padx=10,
            pady=10
        )
        self.message_entry.pack(fill="x", padx=10, pady=10)
        self.message_entry.bind("<Return>", self.send_message)
        
        # Панель пользователей
        self.user_frame = tk.Frame(self.right_frame, bg=self.sidebar_color, width=200)
        self.user_frame.pack(side="right", fill="y")
        self.user_frame.pack_propagate(False)
        
        # Заголовок пользователей
        user_label = tk.Label(
            self.user_frame, 
            text="ONLINE — 4", 
            bg=self.sidebar_color, 
            fg=self.text_color,
            font=("Arial", 10, "bold"),
            padx=10,
            pady=10,
            anchor="w"
        )
        user_label.pack(fill="x")
        
        # Разделитель
        ttk.Separator(self.user_frame, orient="horizontal").pack(fill="x")
        
        # Список пользователей
        self.user_listbox = tk.Listbox(
            self.user_frame,
            bg=self.sidebar_color,
            fg=self.text_color,
            borderwidth=0,
            highlightthickness=0,
            font=("Arial", 11),
            activestyle="none"
        )
        self.user_listbox.pack(fill="both", expand=True, padx=5)
        
    def update_channel_list(self):
        self.channel_listbox.delete(0, tk.END)
        for channel in self.channels:
            self.channel_listbox.insert(tk.END, f"# {channel}")
            
    def update_user_list(self):
        self.user_listbox.delete(0, tk.END)
        for user in self.users:
            self.user_listbox.insert(tk.END, user)
            
    def on_channel_select(self, event):
        selection = self.channel_listbox.curselection()
        if selection:
            index = selection[0]
            self.current_channel = self.channels[index]
            self.chat_header.config(text=f"#{self.current_channel}")
            self.clear_messages()
            self.add_message("System", f"Welcome to #{self.current_channel}!")
            
    def clear_messages(self):
        self.message_area.config(state="normal")
        self.message_area.delete(1.0, tk.END)
        self.message_area.config(state="disabled")
        
    def add_message(self, user, message):
        self.message_area.config(state="normal")
        
        # Время сообщения
        now = datetime.now()
        time_str = now.strftime("%H:%M")
        
        # Форматирование сообщения
        self.message_area.insert(tk.END, f"[{time_str}] {user}: ", "user")
        self.message_area.insert(tk.END, f"{message}\n\n", "message")
        
        self.message_area.config(state="disabled")
        self.message_area.see(tk.END)
        
        # Добавляем теги для стилей
        self.message_area.tag_config("user", foreground=self.highlight_color)
        self.message_area.tag_config("message", foreground=self.text_color)
        
    def send_message(self, event):
        message = self.message_entry.get("1.0", tk.END).strip()
        if message:
            self.add_message("You", message)
            self.message_entry.delete("1.0", tk.END)
            
            # Имитация ответа
            if "привет" in message.lower():
                self.add_message("Bot", "Привет! Как дела?")
            elif "пока" in message.lower():
                self.add_message("Bot", "До свидания! Хорошего дня!")
            else:
                self.add_message("Bot", "Я получил ваше сообщение!")
        
        # Предотвращаем перенос строки по Enter
        return "break"

if __name__ == "__main__":  # Исправлено: __name__ вместо name
    root = tk.Tk()
    app = DiscordApp(root)
    root.mainloop()