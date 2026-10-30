from pathlib import Path
path = Path("test_downloads")

categories = {
    "Images" : [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".webm"],
}

#Testing the script without actually moving files
DRY_RUN = True

def get_category(file):
    for category, extensions in categories.items():
        if file.suffix.lower() in extensions:
            return category
    return "Other"

if DRY_RUN:
    print("DRY RUN!")

for file in path.iterdir():

    if file.is_file():
        
        found_category = get_category(file)

        path_category = path / found_category
        if not DRY_RUN:
            path_category.mkdir(exist_ok=True)

        destination = path_category / file.name
        i = 1
        while destination.exists():
            new_name = f"{file.stem} ({i}){file.suffix}"
            destination = path_category / new_name
            i += 1

        if DRY_RUN:
            print(f"Would have moved {destination.name} -> {found_category}")
        else:
            file.rename(destination)
            print(f"Moved {destination.name} -> {found_category}")

