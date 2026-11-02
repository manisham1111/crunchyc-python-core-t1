
from pathlib import Path
import shutil


def get_category(file_path):
    """Identify the category of a file."""
    extension = file_path.suffix.lower()

    if extension in [".jpg", ".jpeg", ".png"]:
        return "Images"
    elif extension == ".pdf":
        return "PDFs"
    elif extension in [".doc", ".docx", ".txt"]:
        return "Documents"
    elif extension in [".zip", ".rar"]:
        return "Archives"
    else:
        return "Others"


def get_destination(file_path, target_folder):
    """Generate the destination path for a file."""
    category = get_category(file_path)
    return target_folder / category / file_path.name


def organize_files(source_folder, target_folder, dry_run=True):
    """Organize files safely with dry-run support."""
    if not source_folder.exists():
        print("Error: Source folder does not exist.")
        return

    if not source_folder.is_dir():
        print("Error: Source path is not a folder.")
        return

    if source_folder.resolve() == target_folder.resolve():
        print("Error: Source and target cannot be the same.")
        return

    moved = 0
    skipped = 0

    for file_path in source_folder.iterdir():
        if not file_path.is_file():
            continue

        destination = get_destination(file_path, target_folder)

        if destination.exists():
            print(f"Skipped: {file_path.name}")
            skipped += 1
            continue

        if dry_run:
            print(f"[DRY RUN] {file_path.name} -> {destination.parent.name}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name}")
            moved += 1

    print("\n--- Summary ---")
    print(f"Moved: {moved}")
    print(f"Skipped: {skipped}")

    if dry_run:
        print("Dry-run completed. No files were moved.")


def main():
    """Start the file organizer."""
    source = input("Source folder: ").strip().strip('"')
    target = input("Target folder: ").strip().strip('"')

    mode = input("Dry run? (y/n): ").strip().lower()
    dry_run = mode != "n"

    organize_files(Path(source), Path(target), dry_run)


if __name__ == "__main__":
    main()
