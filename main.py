import os
import platform
import shutil
import streamlit as st

ext = {
    "jpg": "image",
    "png": "image",
    "pdf": "document",
    "docx": "document",
    "txt": "text",
    "mp3": "audio",
    "mp4": "video",
    "jpeg": "image",
    "wav": "audio",
    "pptx": "document",
    "xlsx": "document",
    "mkv": "video",
    "csv": "document",
    "svg": "image",
    "zip": "archive",
    "exe": "executable",
    "iso": "disk image",
    "psd": "image",
    "md": "text",
    "rar": "archive"
}

# 1. Detect OS and set appropriate default path hints
current_os = platform.system()

if current_os == "Windows":
    example_path = r"C:\Users\YourName\Downloads"
elif current_os == "Darwin":  
    example_path = "/Users/YourName/Downloads"
else:  
    example_path = "/home/yourname/downloads"

# Build UI
st.title("Personal File Organizer")
st.caption(f"🖥️ Detected System: **{current_os}**")
st.write("Clean up your messy files and folders with ease!")

raw_folder_path = st.text_input(
    "Enter the full path of the folder you want to organize:",
    placeholder=example_path
)

if st.button("Organize my files"):
    # 2. Normalize paths and expand home directory shortcuts (~/Downloads)
    folder_path = os.path.normpath(os.path.expanduser(raw_folder_path.strip()))
    
    if raw_folder_path and os.path.exists(folder_path) and os.path.isdir(folder_path):
        files_moved = 0
        
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Ensure we only move files, skipping existing category subdirectories
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower().lstrip(".")
                category_name = ext.get(file_extension, "others")
                
                # Construct target path using OS-specific separator
                target_folder = os.path.join(folder_path, category_name)
                os.makedirs(target_folder, exist_ok=True)
                
                destination = os.path.join(target_folder, filename)
                shutil.move(file_path, destination)
                files_moved += 1
                
        if files_moved > 0:
            st.success(f"🎉 Successfully organized {files_moved} files into category folders.")
            st.balloons()
        else:
            st.info("No files were moved. The folder might already be organized!")
            
    elif not raw_folder_path:
        st.warning("Please enter a folder path first.")
    else:
        st.error(f"Oops! The path '{folder_path}' was not found on this system.")