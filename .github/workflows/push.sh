set -e
echo "Bot starts committing README.md"

# Set up bot committer
git config --local user.email "BurtonQin+github-actions[bot]@users.noreply.github.com"
git config --local user.name "GitHub Actions [Bot]"

test_md=$(pwd)/test.md

# git clone Awesome-Rust-Checker
cd
git clone https://x-access-token:$(GITHUB_TOKEN)@github.com/os-checker/Awesome-Rust-Checker
cd Awesome-Rust-Checker

# Replace README
cp $test_md README.md

echo "Add & Commit README.md"
git add README.md
git commit -m "[bot] Update last commit time in README.md"
git push
echo "Succeed in pushing 🎇"
