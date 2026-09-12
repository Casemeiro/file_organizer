import os
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
#1. Build the user interface
st.title("Personal File Organizer")
st.write("Clean up ur messy files and folders with ease!")
# creating a text box for the user to input the path of the folder they want to organize
folder_path= st.text_input("Enter the  full path of the folder you want to organize:")
# Creating a button to trigger the organization process
if st.button("Organize my files"):
    # checks whether the files actually exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        
        files_moved = 0
        
        # 3. Loop through everything in the folder using os.listdir
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Make sure we are only moving files, not folders that are already there
            if os.path.isfile(file_path):
                
                # Get the extension (e.g., '.jpg') and remove the dot so it matches your dictionary
                file_extension = os.path.splitext(filename)[1].lower().replace(".", "")
                
                # Look up the category in your 'ext' dictionary. 
                # If it's a weird file type not in the list, default to "others"
                category_name = ext.get(file_extension, "others")
                
                # 4. Create the new folder path (e.g., /documents/image)
                target_folder = os.path.join(folder_path, category_name)
                
                # If the 'image' folder doesn't exist yet, make it!
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                # 5. Move the file
                destination = os.path.join(target_folder, filename)
                shutil.move(file_path, destination)
                files_moved += 1
                
        # 6. Give the user some feedback on the screen
        if files_moved > 0:
            st.success(f"🎉 Your files have been successfully organized {files_moved} files.")
            st.balloons() # Streamlit's fun celebration animation!
        else:
            st.info("No files were moved. The folder might already be organized!")
            
    elif folder_path == "":
        st.warning("Please enter a folder path first.")
    else:
        st.error("Oops! I can't find that folder. Double-check the path and try again.")
