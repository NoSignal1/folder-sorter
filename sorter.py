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

        print(f"Moving {file.name} -> {found_category}")
        path_category = path / found_category
        path_category.mkdir(exist_ok=True)
        file.rename(path_category / file.name)

