import os
import shutil

def organize_workspace(target_directory):
    # Create a new folder for documents if it doesn't exist
    doc_folder = os.path.join(target_directory, "Documents")
    if not os.path.exists(doc_folder):
        os.makedirs(doc_folder)
        print(f"Created folder: {doc_folder}")

    # Create a new folder for images if it doesn't exist
    image_folder = os.path.join(target_directory, "Images")
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
        print(f"Created folder: {image_folder}")

    # Look at every file in the target directory
    for filename in os.listdir(target_directory):
        print(f"Hmm, let me look at this file: {filename}")
        file_path = os.path.join(target_directory, filename)

      # Skip if it is a folder, we only want to move files
        if os.path.isdir(file_path):
            continue

        # If it's a text or pdf file, move it to Documents
        if filename.lower().endswith('.txt') or filename.lower().endswith('.pdf'):
            destination = os.path.join(doc_folder, filename)
            shutil.move(file_path, destination)
            print(f"Moved: {filename} -> Documents folder")
            
        # If it's a jpg or png, move it to Images
        elif filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
            destination = os.path.join(image_folder, filename)
            shutil.move(file_path, destination)
            print(f"Moved: {filename} -> Images folder")

# --- This is where the script actually starts running ---
current_folder = os.getcwd()
print(f"Scanning folder: {current_folder}")
organize_workspace(current_folder)
print("Organization complete!")