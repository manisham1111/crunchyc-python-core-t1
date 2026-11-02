
# Smart Downloads Folder Organizer

A Python automation tool that organizes files into folders based on file extensions.

## Features

- Automatically categorizes files
- Supports images, PDFs, documents, and archives
- Dry-run mode for safe preview
- Duplicate file detection
- Error handling for invalid folders
- Python standard libraries only

## Tech Stack

- Python 3.12
- pathlib
- shutil

## Project Structure

```text
crunchyc-python-core-t1/
├── organizer.py
├── requirements.txt
├── README.md
├── .gitignore
├── test_downloads/
└── test_output/
```

## Setup

```cmd
py -3.12 -m venv .venv
.venv\Scripts\activate
```

## Run

```cmd
python organizer.py
```

Enter source folder and target folder.

Select:
- y: Dry run
- n: Actual file moving

## File Categories

| Extension | Folder |
|---|---|
| JPG, PNG | Images |
| PDF | PDFs |
| DOC, DOCX, TXT | Documents |
| ZIP, RAR | Archives |
| Other | Others |

## Author

Manisha M