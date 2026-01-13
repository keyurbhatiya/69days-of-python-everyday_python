# day 25  of 69 days python

# blild bulk file renamer tool

from pathlib import Path

def bulk_rename(
        folder_path: str,
        prefix : str= "file",
        start_number: int = 1,
        extension_filter : str | None = None
):
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found : {folder}")
    
    files = sorted([
        f for f in folder.iterdir()
        if f.is_file() and (extension_filter is None or f.suffix == extension_filter)
    ])

    if not files:
        print("No files found to rename..")
        return
    
    print(f"Renaming {len(files)} files in  : {folder}")


    for index,file in enumerate(files,start=start_number):

        new_name= f"{prefix}_{index}{file.suffix}"
        new_path = folder / new_name

        if new_path.exists():
            print(f"Skipping (already exists) : {new_name}")
            continue
        file.rename(new_path)
        print(f"Renamed : {file.name} -> {new_name}")

print("\n Bluk renaming sucess!.....")

if __name__ == "__main__":
    bulk_rename(
        folder_path = "sample_files",
        prefix = "image",
        start_number=1,
        extension_filter= None
    )

print("End Day 25/69 days python")