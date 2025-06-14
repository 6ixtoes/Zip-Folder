import os
import shutil
import subprocess

def setup_git_repo(local_repo_path, github_url):
    if not os.path.exists(local_repo_path):
        print("[+] Cloning GitHub repository...")
        subprocess.run(["git", "clone", github_url, local_repo_path], check=True)
    else:
        print("[+] Local repo exists. Using it.")

def push_to_github(repo_path, zip_file_path, commit_message="Add zipped folder"):
    shutil.copy(zip_file_path, repo_path)
    os.chdir(repo_path)

    subprocess.run(["git", "add", "."], check=True)

    # Check if anything is staged
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if result.stdout.strip():
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("[+] Changes committed and pushed to GitHub.")
    else:
        print("[!] No changes to commit. Skipping commit and push.")
