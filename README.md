# arcanum

`arcanum` as a lightweight package for writing a personal journal.

## Installation

Clone the repo and run `poetry install`. Requires `Python 3.11` (most likely works on older versions, didn't test it).

## Usage

### Writing

Run `bash write.sh`. You'll see it opens up `vim`, where you can write anything you want. 
The file will be saved in `diary/<current year>/<current month>/<current day>.md`.

If you want it to open something else (e.g. `nano`, `emacs` etc), edit `write.sh` script.

### Displaying the diary

Simply run `mkdocs build` and then `mkdocs serve`. 
All the entries you wrote will appear in the sidebar, formatted for example as:
```
- 2023
 - April
   - 20 (Thursday)
```

## Rationale

I just wanted something dead simple to write some personal stuff and display it nicely.
