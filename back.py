import os
import shutil
import time
from datetime import date

# Function to copy files of specific types from source to destination
def copy_files(source, destination):
    file_extensions = (".png", ".jpg", ".docx")  # Add more file extensions as needed
    copied_files = []

    for root, dirs, files in os.walk(source):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in file_extensions:
                file_path = os.path.join(root, file)
                try:
                    shutil.copy2(file_path, destination)
                    copied_files.append(file_path)
                    print(f"Copied: {file_path}")
                except Exception as e:
                    print(f"Error copying file: {file_path}")
                    print(f"Error message: {str(e)}")

                if time.time() >= end_time:
                    print("Time limit reached. Backup stopped.")
                    return copied_files

    return copied_files

# Specify the source directory on the PC
source_directory = "C:\\Users"  # Replace with the desired source directory

# Specify the destination directory on the USB drive
destination_directory = "D:\\backup"  # Replace with your desired destination directory on the USB drive

# Calculate the end time after 10 seconds
end_time = time.time() + 10

# Copy files from the source directory on the PC to the destination directory on the USB drive
copied_files = []
for root, dirs, files in os.walk(source_directory, topdown=True):
    copied_files.extend(copy_files(root, destination_directory))

    if time.time() >= end_time:
        print("Time limit reached. Backup stopped.")
        break

# Create a folder on the USB drive with the current date
today = date.today()
backup_folder_name = today.strftime("%Y-%m-%d")
backup_folder = os.path.join(destination_directory, backup_folder_name)
os.makedirs(backup_folder, exist_ok=True)

# Move the copied files to the backup folder
for file_path in copied_files:
    try:
        file_name = os.path.basename(file_path)
        destination_file_path = os.path.join(backup_folder, file_name)
        shutil.move(file_path, destination_file_path)
    except Exception as e:
        print(f"Error moving file: {file_path}")
        print(f"Error message: {str(e)}")

print(f"Backup completed. Files saved in folder: {backup_folder_name}")

# Prompt to indicate when the script has finished
input("Press Enter to exit...")
