# scanner.py
import os
from datetime import datetime, timedelta

def list_files(folder_path):
    """
    Return a list of all files in the folder (ignore subfolders for simplicity).
    """
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def get_file_info(file_path):
    """
    Return a dictionary with file info: name, size in KB, type, last modified date.
    """
    stat = os.stat(file_path)
    file_info = {
        "name": os.path.basename(file_path),
        "size_kb": round(stat.st_size / 1024, 2),
        "type": os.path.splitext(file_path)[1],
        "last_modified": datetime.fromtimestamp(stat.st_mtime)
    }
    return file_info

def flag_old_files(folder_path, days_threshold=30):
    """
    Return a list of files not modified in the last 'days_threshold' days.
    """
    old_files = []
    now = datetime.now()
    for f in list_files(folder_path):
        file_path = os.path.join(folder_path, f)
        last_mod = get_file_info(file_path)["last_modified"]
        if now - last_mod > timedelta(days=days_threshold):
            old_files.append(f)
    return old_files

# Optional: test module directly
if __name__ == "__main__":
    folder = "."
    print("Files in folder:", list_files(folder))
    print("Old files (>30 days):", flag_old_files(folder))