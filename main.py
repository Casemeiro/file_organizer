import os
import platform
import shutil
import streamlit as st

ext = {
    "jpg": "image", "png": "image", "pdf": "document", "docx": "document",
    "txt": "text", "mp3": "audio", "mp4": "video", "jpeg": "image",
    "wav": "audio", "pptx": "document", "xlsx": "document", "mkv": "video",
    "csv": "document", "svg": "image", "zip": "archive", "exe": "executable",
    "iso": "disk image", "psd": "image", "md": "text", "rar": "archive"
}

# 1. Dynamically detect the actual system username and path
user_home = os.path.expanduser("~")
default_downloads = os.path.join(user_home, "Downloads")
current_os = platform.system()

st.title("Personal File Organizer")
st.caption(f"🖥️ System: **{current_os}** | 👤 Detected User Home: `{user_home}`")

# 2. Pre-fill or suggest the exact absolute path
raw_folder_path = st.text_input(
    "Enter the full path of the folder you want to organize:",
    value=default_downloads  # Sets the user's real Downloads folder as default
)

if st.button("Organize my files"):
    folder_path = os.path.normpath(raw_folder_path.strip())
    
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files_moved = 0
        
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower().lstrip(".")
                category_name = ext.get(file_extension, "others")
                
                target_folder = os.path.join(folder_path, category_name)
                os.makedirs(target_folder, exist_ok=True)
                
                destination = os.path.join(target_folder, filename)
                shutil.move(file_path, destination)
                files_moved += 1
                
        if files_moved > 0:
            st.success(f"🎉 Successfully organized {files_moved} files!")
            st.balloons()
        else:
            st.info("No files were moved. The folder might already be organized!")
            
    else:
        st.error(f"Oops! The path '{folder_path}' was not found on this system.")