import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog, messagebox, PhotoImage
from threading import Thread
from pyAesCrypt import encryptFile, decryptFile
from os import remove, path

icon_path = path.join(path.dirname(__file__), "icon.png")

def submit():
    try:
        buffer_size_dict = {"4 KB": 4, "16 KB": 16, "64 KB": 64, "256 KB": 256, "1 MB": 1024}
        buffer_size = buffer_size_dict[buffer_size_combobox.get()] * 1024
        input_file = file_path_entry.get()
        input_file_parts = input_file.split(".")
        password = password_entry.get()

        if input_file == "":
            raise Exception("Input path cannot be empty")
        if password == "":
            raise Exception("Password cannot be empty")
        widgets_state("disabled")
        if input_file_parts[-1] == "aes":
            output_file_parts = input_file.split(".")
            output_file_parts.pop()
            output_file = ".".join(output_file_parts)
            logs.config(state="normal")
            logs.insert(tk.END, "Decrypting File, Please Wait...\n")
            logs.config(state="disabled")
            decryptFile(input_file, output_file, password, buffer_size)
            widgets_state("normal")
            file_path_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            remove(f"{input_file}")
            logs.config(state="normal")
            logs.insert(tk.END, f"Decrypted File: {output_file}\n")
            logs.config(state="disabled")

        elif input_file_parts[-1] != "aes":
            output_file = f"{input_file}.aes"
            logs.config(state="normal")
            logs.insert(tk.END, "Encrypting File, Please Wait...\n")
            logs.config(state="disabled")
            encryptFile(input_file, output_file, password, buffer_size)
            widgets_state("normal")
            file_path_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            remove(f"{input_file}")
            logs.config(state="normal")
            logs.insert(tk.END, f"Encrypted File: {output_file}\n")
            logs.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))
    
    finally:
        widgets_state("normal")

def submit_thread():
    thread_01 = Thread(target=submit, daemon=True)
    thread_01.start()

def select_file():
    file_path = filedialog.askopenfilename(title="Select file", initialdir="~")
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

    file_path_parts = file_path.split(".")
    logs.config(state="normal")
    if file_path_parts[-1] == "aes":
        logs.insert(tk.END, f"Encrypted File Detected\n")
    elif file_path_parts[-1] != "aes":
        logs.insert(tk.END, f"Unencrypted File Detected\n")
    logs.config(state="disabled")

def select_file_thread():
    thread_02 = Thread(target=select_file, daemon=True)
    thread_02.start()

def widgets_state(value):
    file_path_entry.config(state=value)
    file_path_button.config(state=value)
    password_entry.config(state=value)
    password_button.config(state=value)
    buffer_size_combobox.config(state=value)

root = ttk.Window(themename="superhero")
root.title("Cypher")
root.geometry("750x500")
root.minsize(750, 500)
root.iconphoto(False, PhotoImage(file=icon_path))

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="x")
main_frame.columnconfigure(1, weight=1)

ttk.Label(main_frame, text="File Path: ").grid(row=0, column=0, padx=5, pady=5, sticky="w")
file_path_entry = ttk.Entry(main_frame)
file_path_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

file_path_button = ttk.Button(main_frame, text="Select File", command=select_file_thread, bootstyle="secondary")
file_path_button.grid(row=0, column=2, padx=5, pady=5, sticky="we")

ttk.Label(main_frame, text="Buffer Size: ").grid(row=1, column=0, padx=5, pady=5, sticky="w")
buffer_size_combobox = ttk.Combobox(main_frame, values=["4 KB", "16 KB", "64 KB", "256 KB", "1 MB"], state="readonly", bootstyle="secondary")
buffer_size_combobox.current(2)
buffer_size_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="we", columnspan=2)

ttk.Label(main_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
password_entry = ttk.Entry(main_frame, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

password_button = ttk.Button(main_frame, text="Submit", command=submit_thread, bootstyle="primary")
password_button.grid(row=2, column=2, padx=5, pady=5, sticky="we")

logs_frame = ttk.LabelFrame(root, text=" Logs ")
logs_frame.pack(fill="both", expand=True, padx=15, pady=10)
logs_frame.columnconfigure(0, weight=1)
logs_frame.rowconfigure(0, weight=1)

logs = tk.Text(logs_frame, font=("Consolas", 10), state="disabled", borderwidth=0)
logs.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

root.mainloop()
