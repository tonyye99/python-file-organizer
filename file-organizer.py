import os, time
import shutil


def organize_files(folder_path, organize_by_ext):
    files = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith(".")
    ]

    for file in files:
        if organize_by_ext:
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


organize_files("/Users/tony/Desktop", False)
