import requests
import re
from datetime import datetime

def fetch_last_commit_time(owner, repo):
    # GitHub API URL for the repository commits
    commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    # Fetch last commit
    commits_response = requests.get(commits_url)
    if commits_response.status_code != 200:
        print(f"Error fetching commits: {commits_response.status_code}")
        return None

    commits_data = commits_response.json()

    # Last commit time in YYYY-MM-DD format
    last_commit_time = commits_data[0]['commit']['committer']['date']
    return last_commit_time.split('T')[0]  # Only return date part

def update_markdown_file(file_path):
    # Read the Markdown file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Prepare to write the updated lines
    updated_lines = []
    pattern = r'\[(.*?)\]\((.*?)\)'
    github_header = "https://github.com/"
    for line in lines:
        # Match the specific table line
        fields = line.split('|')
        if len(fields) != 8:
            updated_lines.append(line)
            continue
        first_field = fields[1].strip()
        match = re.search(pattern, first_field)
        if not match:
            updated_lines.append(line)
            continue
        url = match.group(2)
        if not url.startswith(github_header):
            updated_lines.append(line)
            continue
        remain = url[len(github_header):]
        subs = remain.split('/')
        owner, repo = subs[0], subs[1]
        last_commit_time = fetch_last_commit_time(owner, repo)
        if not last_commit_time:
            update_lines.append(line)
            continue
        # Replace the last field with the last commit time
        fields[6] = f" {last_commit_time} "
        updated_line = '|'.join(fields)
        updated_lines.append(updated_line)

    # Write the updated lines back to the Markdown file
    with open("test.md", 'w') as file:
        file.writelines(updated_lines)

# Example usage
if __name__ == "__main__":
    markdown_file_path = "README.md"  # Replace with your Markdown file path
    update_markdown_file(markdown_file_path)
