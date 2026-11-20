from pathlib import Path

# 1. Get the current working directory
current_dir = Path.cwd()
print("Current directory:", current_dir)

# 2. Build a path using the '/' operator
file_path = current_dir / "data" / "notes.txt"

# 3. Create folders if they don't exist
file_path.parent.mkdir(parents=True, exist_ok=True)

# 4. Write and read text directly
file_path.write_text("Hello, pathlib!")
print("File contents:", file_path.read_text())

# 5. Check properties and extract parts
print("Exists?", file_path.exists())
print("File name:", file_path.name)       # notes.txt
print("Extension:", file_path.suffix)     # .txt
