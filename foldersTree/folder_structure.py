import os

# List of folder names to skip the contents of
skip_folders = ["node_modules", "object"]

def generate_tree_structure(folder_path, indent=""):
    items = os.listdir(folder_path)
    for item in items:
        item_path = os.path.join(folder_path, item)
        if item in skip_folders and os.path.isdir(item_path):
            print(indent + "├── " + item + "/")
            with open("folder_structure.txt", "a") as file:
                file.write(indent + "├── " + item + "/\n")
        elif os.path.isdir(item_path):
            print(indent + "├── " + item + "/")
            with open("folder_structure.txt", "a") as file:
                file.write(indent + "├── " + item + "/\n")
            generate_tree_structure(item_path, indent + "│   ")
        else:
            print(indent + "├── " + item)
            with open("folder_structure.txt", "a") as file:
                file.write(indent + "├── " + item + "\n")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    if os.path.exists(folder_path):
        print(folder_path + "/")
        with open("folder_structure.txt", "w") as file:
            file.write(folder_path + "/\n")
        generate_tree_structure(folder_path)
        print("Folder structure has been written to 'folder_structure.txt'")
    else:
        print("Folder path does not exist.")
