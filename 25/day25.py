from pathlib import Path

def bulk_rename(folder_path, prefix):
    folder = Path(folder_path)
    files = sorted([f for f in folder.iterdir() if f.is_file()])
    
    for index, file in enumerate(files, start=1):
        new_name = f"{prefix}_{index}{file.suffix}"
        file.rename(folder / new_name)
        print(f"Renamed to: {new_name}")

if __name__ == "__main__":
    bulk_rename("sample_files", "image")