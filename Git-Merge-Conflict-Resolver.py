import os
import subprocess
import re

def get_conflicted_files():
    """Check Git status and extract conflicted files."""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        conflicted_files = []
        
        for line in result.stdout.split('\n'):
            if line.startswith('UU') or 'both modified' in line:
                file_name = line.split()[-1]
                conflicted_files.append(file_name)
        
        return conflicted_files
    except Exception as e:
        print(f"❌ Error checking Git status: {e}")
        return []

def show_conflict_details(file_name):
    """Display conflict details for a specific file."""
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        
        conflict_pattern = re.compile(r'(<<<<<<<.*?=======.*?>>>>>>>.*?)', re.DOTALL)
        conflicts = conflict_pattern.findall(content)
        
        if conflicts:
            print(f"\n⚠️ Conflicts found in file {file_name}:")
            for conflict in conflicts:
                print(f"\n{conflict}\n")
        else:
            print(f"✅ No conflicts found in {file_name}!")
    except Exception as e:
        print(f"❌ Error reading file {file_name}: {e}")

def resolve_conflict(file_name, strategy="manual"):
    """Resolve conflict based on the chosen strategy."""
    if strategy == "keep-mine":
        try:
            subprocess.run(['git', 'checkout', '--ours', file_name], check=True)
            print(f"✅ Your changes for {file_name} have been kept.")
        except Exception as e:
            print(f"❌ Error executing 'keep-mine': {e}")
    elif strategy == "keep-theirs":
        try:
            subprocess.run(['git', 'checkout', '--theirs', file_name], check=True)
            print(f"✅ Changes from the other branch for {file_name} have been accepted.")
        except Exception as e:
            print(f"❌ Error executing 'keep-theirs': {e}")
    else:
        print("🔧 Please resolve the conflict manually and then run 'git add'.")

def main():
    print("🔍 Checking for Git merge conflicts...")
    conflicted_files = get_conflicted_files()
    
    if not conflicted_files:
        print("✅ No conflicts found!")
        return
    
    for file in conflicted_files:
        show_conflict_details(file)
        
        print("\n📌 Conflict resolution options:")
        print("1. Keep your changes (keep-mine)")
        print("2. Accept changes from the other branch (keep-theirs)")
        print("3. Edit manually")
        
        choice = input("✅ Choose an option (1/2/3): ")
        if choice == "1":
            resolve_conflict(file, "keep-mine")
        elif choice == "2":
            resolve_conflict(file, "keep-theirs")
        else:
            print(f"⚡ Please edit {file} manually and then run 'git add'.")

if __name__ == "__main__":
    main()

## https://github.com/Shayanthn
## shayanthn78@gmail.com
""" 🚀 About the Developer
Python Expert | Advanced English Instructor | Creative Thinker

Passionate Python developer with expertise in web development, AI, automation, and data science. Skilled in problem-solving, clean code, and scalable solutions. Also an advanced English instructor with strong communication and technical documentation abilities.

💡 Innovator & Idea Generator | Always seeking to create efficient, cutting-edge projects.
📌 Proficient in Django, Flask, FastAPI, TensorFlow, Pandas, Selenium, and more.
🚀 Open to collaboration on GitHub and tech-driven projects.
 """