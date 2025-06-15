import os
import subprocess
import shutil

def setup_git_repo(local_repo_path, github_url):
    if os.path.exists(local_repo_path):
        print("[+] Repo folder already exists. Skipping clone.")
        # ✅ Change the origin URL to what the user provided
        os.chdir(local_repo_path)
        subprocess.run(["git", "remote", "set-url", "origin", github_url], check=True)
    else:
        print("[+] Cloning Github repository...")
        subprocess.run(["git", "clone", github_url, local_repo_path], check=True)


def push_to_github(local_repo_path, zip_path, commit_message):
    zip_name = os.path.basename(zip_path)
    dest_path = os.path.join(local_repo_path, zip_name)

    print(f"[+] Copying {zip_name} to repo...")
    shutil.copy2(zip_path, dest_path)

    os.chdir(local_repo_path)
    subprocess.run(["git", "add", zip_name], check=True)

    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if result.stdout.strip() == "":
        print("[!] No changes to commit. Skipping commit and push.")
        return

    print("[+] Committing changes...")
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    print("[+] Pushing to GitHub...")
    subprocess.run(["git", "push"], check=True)
