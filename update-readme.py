import os

README_PATH = "README.md"
MEETING_DIR = "docs"

files = sorted(os.listdir(MEETING_DIR), reverse=True)
latest_file = next((f for f in files if f.startswith("meeting-")), None)

if latest_file:
    with open(os.path.join(MEETING_DIR, latest_file), "r", encoding="utf-8") as f:
        meeting_content = f.read()

    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start = lines.index("<!-- MEETING_START -->\n")
    end = lines.index("<!-- MEETING_END -->\n")
    new_lines = lines[:start+1] + [meeting_content + "\n"] + lines[end:]

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
