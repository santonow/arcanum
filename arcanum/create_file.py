from pathlib import Path
from datetime import date


if __name__ == "__main__":
    import sys

    diary_path = Path(sys.argv[1])
    today = date.today()
    day = today.strftime("%A")
    month = today.strftime("%B")
    filepath = diary_path / str(today.year) / str(today.month)
    filepath.mkdir(parents=True, exist_ok=True)
    final_fpath = filepath / (str(today.day) + ".md")
    if not final_fpath.exists():
        with open(final_fpath, "w") as handle:
            handle.write(f"# {today.day} ({day})/{month}/{today.year}")
    print(str(final_fpath))
