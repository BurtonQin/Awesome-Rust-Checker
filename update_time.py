import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests


LAST_UPDATED_PREFIX = "> Contributions welcomed! Last updated: "
HERMES_ENV_PATH = Path("/home/ubuntu/.hermes/.env")


def load_github_token():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token.strip()

    if not HERMES_ENV_PATH.exists():
        return None

    for line in HERMES_ENV_PATH.read_text().splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        key, value = s.split("=", 1)
        if key.strip() == "GITHUB_TOKEN":
            return value.strip().strip('"').strip("'")

    return None


def parse_github_repo(url):
    parsed = urlparse(url)
    if parsed.netloc != "github.com":
        return None

    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return None

    owner, repo = parts[0], parts[1]
    if repo.endswith(".git"):
        repo = repo[:-4]

    return owner, repo


def fetch_last_commit_time(owner, repo, token=None):
    # GitHub API URL for the repository commits
    commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-rust-checker-update-script",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Fetch last commit
    commits_response = requests.get(commits_url, headers=headers, timeout=20)
    if commits_response.status_code != 200:
        print(f"Error fetching commits for {owner}/{repo}: {commits_response.status_code}")
        return None

    commits_data = commits_response.json()
    if not commits_data:
        return None

    # Last commit time in YYYY-MM-DD format
    last_commit_time = commits_data[0]["commit"]["committer"]["date"]
    return last_commit_time.split("T")[0]  # Only return date part


def update_markdown_file(file_path):
    # Read the Markdown file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Prepare to write the updated lines
    updated_lines = []
    pattern = r"\[(.*?)\]\((.*?)\)"
    github_header = "https://github.com/"
    today = datetime.now(timezone.utc).date().isoformat()
    github_token = load_github_token()

    for line in lines:
        if line.startswith(LAST_UPDATED_PREFIX):
            updated_lines.append(f"{LAST_UPDATED_PREFIX}{today}\n")
            continue

        # Match the specific table line
        fields = line.split("|")
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

        repo_info = parse_github_repo(url)
        if not repo_info:
            updated_lines.append(line)
            continue

        owner, repo = repo_info
        last_commit_time = fetch_last_commit_time(owner, repo, github_token)
        if not last_commit_time:
            updated_lines.append(line)
            continue

        # Replace the last field with the last commit time
        fields[6] = f" {last_commit_time} "
        updated_line = "|".join(fields)
        updated_lines.append(updated_line)

    # Write the updated lines back to the Markdown file
    with open(file_path, "w") as file:
        file.writelines(updated_lines)


# Example usage
if __name__ == "__main__":
    markdown_file_path = "README.md"
    update_markdown_file(markdown_file_path)
