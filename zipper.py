import os
import zipfile

def zip_folder(folder_path, zip_name):
    parent_dir = os.path.dirname(folder_path)
    zip_path = os.path.join(parent_dir, f"{zip_name}.zip")

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, start=folder_path)
                zipf.write(full_path, arcname)

    print(f"[+] Folder zipped to: {zip_path}")
    return zip_path


if __name__ == "__main__":
    folder = input("Enter folder to zip: ").strip()
    name = input("Enter name for the zip file: ").strip()
    zip_folder(folder, name)