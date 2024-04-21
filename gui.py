import os, time
import shutil

os.environ["LC_ALL"] = "C"

from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

window = ttk.Window(themename="darkly")
window.geometry("600x200")
window.title("File Organizer")

frame = ttk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor="c")

directoryValue = ttk.StringVar()


def askDirectory():
    result = filedialog.askdirectory()
    directoryValue.set(result)
    selectedDirectory.delete(0, END)
    selectedDirectory.insert(0, directoryValue.get())


folderLabel = ttk.Label(frame, text="Choose folder: ")
folderLabel.grid(column=0, row=0, padx=10, pady=10, sticky="e")

selectedDirectory = ttk.Entry(frame)
selectedDirectory.grid(column=1, row=0, padx=5)

folderSelectButton = ttk.Button(
    frame, text="Select", bootstyle="INFO", command=askDirectory
)
folderSelectButton.grid(column=2, row=0, pady=10, sticky="e")

cleanTypeLabel = ttk.Label(frame, text="Choose Type to organize: ")
cleanTypeLabel.grid(column=0, row=1, padx=10, pady=10, sticky="e")

cleanType = ttk.IntVar()
cleanType.set(1)
R1 = ttk.Radiobutton(frame, text="By Extension", variable=cleanType, value=1)
R1.grid(column=1, row=1, pady=10, sticky="w")

R2 = ttk.Radiobutton(frame, text="By Date", variable=cleanType, value=2)
R2.grid(column=1, row=1, pady=10, sticky="e")


def organize_files(folder_path, organize_by_ext):
    files = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith(".")
    ]

    for file in files:
        if organize_by_ext == 1:
            file_ext = os.path.splitext(file)[1][1:]
            folder_name = file_ext.upper()
        else:
            gmtime = time.gmtime(os.path.getmtime(os.path.join(folder_path, file)))
            folder_name = time.strftime("%Y-%m-%d", gmtime)

        new_folder_path = os.path.join(folder_path, folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        shutil.move(
            os.path.join(folder_path, file),
            os.path.join(new_folder_path, file),
        )

    print("Completed")
    messageLabel = ttk.Label(
        frame, text="Success! The directory has been organized.", bootstyle="success"
    )
    messageLabel.grid(column=0, row=2, columnspan=2)


mybutton = ttk.Button(
    frame,
    text="Run",
    bootstyle="INFO",
    command=lambda: organize_files(directoryValue.get(), cleanType.get()),
)
mybutton.grid(column=2, row=2, pady=20, sticky="e")

window.mainloop()
