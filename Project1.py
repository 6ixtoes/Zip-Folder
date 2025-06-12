import os
import shutil
import subprocess
import zipfile
from datetime import datetime

def zip_folder(folder_path, zip_name):
    parent_dir = os.path.dirname(folder_path)
    zip_path = os.path.join(parent_dir, f"{zip_name}.zip")

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, start=folder_path)
                zipf.write(full_path, arcname)
    print(f"[+] Folder zipped to {zip_path}")
    return zip_path

def setup_git_repo(local_repo_path, github_url):
    if not os.path.exists(local_repo_path):
        print("[+] Cloning Github repository...")
        subprocess.run(["git", "clone", github_url, local_repo_path], check=True)
    else:
        print("[+] Local repo exists Using it.")
def push_to_github(repo_path, zip_file_path, commit_message="Auto-commit zip file"):
    shutil.copy(zip_file_path, repo_path)
    os.chdir(repo_path)


    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)
    
    print("[+] Pushed to Github successfully.")
    








