from app.model.notification import Notification


def read(file_path: str, delimiter=",", column_names: [str]=()):
    column_dict = {
        "message": 0,
        "reporter": 1
    }

    if len(column_names) > 0:
        for i, n in enumerate(column_names):
            _n = n.lower()
            column_dict[_n] = i

    def to_notification(items):
        n = Notification(message="", reporter="")
        for c in column_dict:
            if hasattr(n, c):
                setattr(n, c, items[column_dict[c]])
        return n

    with open(file_path, mode="rt", encoding="utf-8", newline="") as f:
        if delimiter == ",":
            import csv
            reader = csv.reader(f)
            for row in reader:
                yield to_notification(row)
        else:
            for ln in f:
                _ln = ln.replace("\r", "").replace("\n", "")
                row = _ln.split(delimiter)
                yield to_notification(row)
