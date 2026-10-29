from pathlib import Path
path = Path("test_downloads")

for file in path.iterdir():
    print(file.name)