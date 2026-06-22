Python Workspace Organizer

A lightweight, automated Python script that acts as a "Digital Janitor" for your computer. It instantly declutters messy directories (like your Downloads folder) by automatically sorting files into designated folders based on their file type.
 Features
Automated Sorting: Instantly scans a directory and moves files to their proper homes.
Document Handling: Automatically creates a Documents folder and moves .txt and .pdf files.
Image Handling: Automatically creates an Images folder and moves .jpg and .png files.
Bulletproof Logic: Fully case-insensitive (successfully handles .JPG, .pdf, .PnG, etc.) using the .lower() method.
Safe Execution: Automatically ignores existing folders so it only moves loose files.

How to Use It
Make sure you have Python installed on your computer.
Download or clone organizer.py to your computer.
Place organizer.py inside the messy folder you want to clean up (for example, your Downloads folder).
Open your terminal or command prompt in that folder.
Run the script using the following command:
python organizer.py

Watch as your files are instantly sorted into newly created Documents and Images folders

🛠️ Built With
Python 3
os module (for file path management)
shutil module (for moving files)

🌱 What I Learned
Building this project helped me develop practical skills in:
Reverse-engineering existing code architectures.
Managing file system operations (os and shutil).
Debugging Python syntax and indentation rules.

Handling real-world edge cases like case-sensitive file extensions.

Version control using Git and GitHub.
