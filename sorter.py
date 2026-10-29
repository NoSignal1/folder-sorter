from pathlib import Path
path = Path("test_downloads")

for file in path.iterdir():
    if file.is_file():
        print(f"{file.name} -> {file.suffix}")