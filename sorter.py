from pathlib import Path
path = Path("test_downloads")

categories = {
    "Images" : [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".webm"],
}



for file in path.iterdir():

    if file.is_file():
        found_category = "Other"


        for category, extensions in categories.items():
            if file.suffix.lower() in extensions:
                found_category = category
                break

        path_category = path / found_category
        path_category.mkdir(exist_ok=True)

        destination = path_category / file.name
        i = 1
        while destination.exists():
            new_name = f"{file.stem} ({i}){file.suffix}"
            destination = path_category / new_name
            i += 1

        file.rename(destination)
        print(f"Moved {destination.name} -> {found_category}")

