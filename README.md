# Files sorter

## What it does?
- Sorts files in given directory
- Sorted files are stored in sub-directories ex. 'Images'

## Adding/Changing directories
Dictionary `categories` responsible for categories, where you can directly add or change desired directories.
Unmatched files go to `Other` by default.

## DRY RUN
Bool `DRY_RUN` is responsible for switching to 'Whatif' script run.

DRY RUN TURNED ON BY DEFAULT.

Change to 'False' for script to actually work.

ex. `Would have moved texts (6).txt -> Documents`

## How to run
Requires Python 3

1. Open `sorter.py` and set `path` to the folder you want to sort.
2. Run: `python sorter.py`
3. Check the dry-run output, then set `DRY_RUN = False` and run again.

## Known limitations
- Script does not work in recursive, meaning only sorts top level of the folder.
- In Dry Run multiple duplicates of the same file all show the same predicted name.
