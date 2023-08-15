import os
import shutil


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def organize_files(download_folder):
    course_names = {
        "מבני נתונים": ["מבני נתונים"],
        "פתרון בעיות": ["פתרון בעיות"],
        "לינארית 1": ["ליניארית1", "לינ1", "לינארית1", "לינארית 1", "לינ 1", "ליניארית 1"],
        "אינפי 1": ["אינפי1", "אינפי 1"],
        "בדידה 1": ["בדידה 1"],
        "בדידה 2": ["בדידה 2"],
        "מערכות הפעלה": ["מערכות הפעלה"],
    }

    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        dest_path = r"c:\Users\ASUS\OneDrive\שולחן העבודה\מדעי המחשב"

        if os.path.isfile(file_path):
            # Variable to keep track of whether a match was found for the file
            found_match = False

            for course_name, keywords in course_names.items():
                for keyword in keywords:
                    if keyword in filename:
                        create_folder_if_not_exists(
                            os.path.join(dest_path, course_name))
                        try:
                            shutil.move(file_path, os.path.join(
                                dest_path, course_name, filename))
                            print(f"Moved {filename} to {course_name} folder.")
                            found_match = True  # Set the flag to indicate a match was found
                            break  # Found a match, no need to check other keywords for this course name
                        except PermissionError:
                            print(
                                f"Error: Could not move {filename}. It is being used by another process.")
                        break  # Found a match, no need to check other course names

            if not found_match:
                # If no match was found, print a message indicating it
                print(
                    f"No course match found for {filename}. It will not be moved.")


if __name__ == "__main__":
    # Replace this with the actual path to your download library folder
    download_library_path = r"C:\Users\ASUS\Downloads"
    organize_files(download_library_path)
