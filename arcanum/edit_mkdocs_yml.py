from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from operator import itemgetter

import yaml
from pathlib import Path

MKDOCS_YML_PATH = Path(".").absolute() / "mkdocs.yml"
DIARY_PATH = Path(".").absolute() / "diary"


@dataclass
class DiaryEntry:
    entry_date: date
    entry_path: Path


class MkDocsNavHandler:
    def __init__(self):
        self.first = "index.md"
        self.entries = []

    @staticmethod
    def get_date(path: Path) -> date:
        year = int(path.parent.parent.name)
        month = int(path.parent.name)
        day = int(path.stem)
        return date(year=year, month=month, day=day)

    def add_paths_from(self, base_path: Path):
        for path in base_path.glob("**/*"):
            if path.is_file() and path.name != "index.md":
                self.add_path(path)

    def add_path(self, path: Path):
        assert str(path.name).endswith(".md")
        entry_date = self.get_date(path)
        self.entries.append(DiaryEntry(entry_date=entry_date, entry_path=path))

    @staticmethod
    def format_day(entry_date: date):
        return f'{entry_date.day} ({entry_date.strftime("%A")})'

    def create_nav(self):
        nav = [{"Home": self.first}]
        entries = defaultdict(lambda: defaultdict(dict))
        for entry in self.entries:
            entries[entry.entry_date.year][entry.entry_date.strftime("%B")][
                self.format_day(entry.entry_date)
            ] = entry.entry_path
        for year, months in sorted(entries.items(), key=itemgetter(0), reverse=True):
            curr_year = {year: []}
            for month, days in sorted(months.items(), key=itemgetter(0), reverse=True):
                curr_month = {month: []}
                for day, filepath in sorted(
                    days.items(), key=itemgetter(0), reverse=True
                ):
                    curr_month[month].append(
                        {day: str(Path(*Path(filepath).parts[-3:]))}
                    )
                curr_year[year].append(curr_month)
            nav.append(curr_year)
        return nav


if __name__ == "__main__":
    import sys

    mkdocs_yml_path = Path(sys.argv[1])
    diary_path = Path(sys.argv[2])
    with open(mkdocs_yml_path, "r") as handle:
        mkdocs_yaml_file = yaml.safe_load(handle)
    handler = MkDocsNavHandler()
    handler.add_paths_from(diary_path)
    nav = handler.create_nav()
    mkdocs_yaml_file["nav"] = nav
    with open(MKDOCS_YML_PATH, "w") as handle:
        yaml.safe_dump(mkdocs_yaml_file, handle)
