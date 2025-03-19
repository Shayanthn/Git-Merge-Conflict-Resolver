# Git Merge Conflict Resolver

## Overview

Git Merge Conflict Resolver is a command-line tool designed to detect, display, and assist users in resolving merge conflicts in Git repositories. It simplifies the process of handling merge conflicts by providing automated and manual resolution options.

## Description

Merge conflicts can be frustrating and time-consuming, especially when collaborating on large projects. This tool automates the detection of merge conflicts and provides multiple resolution strategies, helping developers streamline their workflow and focus on coding instead of manually fixing conflicts. Whether you're a beginner or an experienced developer, this tool will make resolving conflicts in Git easier and more efficient.

## Features

- **Detect merge conflicts** automatically.
- **Display conflict details** to help understand the issue.
- **Provide resolution options** including:
  - Keep your changes (`keep-mine`).
  - Accept changes from the other branch (`keep-theirs`).
  - Manual resolution guidance.
- **Cross-platform compatibility** (Windows, Mac, Linux).

## Installation

1. Ensure you have Python installed (`>=3.6`).
2. Clone the repository:
   ```bash
   git clone https://github.com/Shayanthn/Git-Merge-Conflict-Resolver.git
   ```
3. Navigate to the project directory:
   ```bash
   cd Git-Merge-Conflict-Resolver
   ```
4. Make the script executable (optional for Linux/macOS):
   ```bash
   chmod +x merge_conflict_resolver.py
   ```

## Usage

Run the script inside a Git repository with potential merge conflicts:
```bash
python merge_conflict_resolver.py
```

It will:
1. Identify files with merge conflicts.
2. Show conflicting sections in the files.
3. Provide resolution options for the user to choose from.

## Example
If conflicts are found, the script will prompt you with options:
```bash
🔍 Checking for Git merge conflicts...
⚠️ Conflicts found in file example.txt:

<<<<<<< HEAD
Your changes here...
=======
Their changes here...
>>>>>> branch-name

📌 Conflict resolution options:
1. Keep your changes (keep-mine)
2. Accept changes from the other branch (keep-theirs)
3. Edit manually
✅ Choose an option (1/2/3):
```

## Contribution

We welcome contributions! Feel free to submit issues and pull requests to improve this tool.

## License

This project is licensed under the MIT License.

## Tags

- `git`
- `merge-conflicts`
- `conflict-resolution`
- `developer-tools`
- `automation`
- `python`

