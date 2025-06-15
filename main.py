import os
from zipper import zip_folder
from gitutils import setup_git_repo, push_to_github

def main():
    folder_to_zip = input("Enter full path to folder: ").strip()
    zip_name = input("Enter desired ZIP file name (no extension): ").strip()
    github_url = input("Enter GitHub HTTPS URL: ").strip()

    local_repo_path = os.path.join(os.getcwd(), "my_github_repo")

    zip_path = zip_folder(folder_to_zip, zip_name)
    setup_git_repo(local_repo_path, github_url)
    push_to_github(local_repo_path, zip_path, f"Add zip: {zip_name}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERROR] {e}")

