from pathlib import Path
import csv

CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[2]
DATA_FILE = PROJECT_ROOT /"data"/"events.csv"

def read_events():
    with DATA_FILE.open(mode="r", newline="",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

if __name__ == '__main__':
    events = read_events()
    for event in events:
        print(event)