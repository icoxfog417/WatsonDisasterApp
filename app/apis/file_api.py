from app.model.notification import Notification


def read(file_path: str, delimiter=",", column_names: [str]=(), use_header=False):
    column_dict = {
        "message": 0,
        "reporter": 1
    }

    def make_define(names):
        if len(names) > 0:
            column_dict.clear()
            for i, n in enumerate(names):
                _n = n.lower()
                column_dict[_n] = i

    def to_notification(items):
        n = Notification(message="", reporter="")
        for c in column_dict:
            if hasattr(n, c):
                setattr(n, c, items[column_dict[c]])
        return n

    make_define(column_names)
    with open(file_path, mode="rt", encoding="utf-8", newline="") as f:
        header = use_header

        if delimiter == ",":
            import csv
            reader = csv.reader(f)
            for row in reader:
                if header:
                    make_define(row)
                    header = False
                else:
                    yield to_notification(row)
        else:
            for ln in f:
                _ln = ln.replace("\r", "").replace("\n", "")
                row = _ln.split(delimiter)
                if header:
                    make_define(row)
                    header = False
                else:
                    yield to_notification(row)
