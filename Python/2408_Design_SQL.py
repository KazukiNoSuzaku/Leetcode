# Premium problem
# Design a SQL-like system supporting insert, delete (by row ID), and select (cell by row/col ID).

class SQL:
    def __init__(self, names: list[str], columns: list[int]):
        self.tables = {name: {} for name in names}  # name -> {row_id: row_data}
        self.next_id = {name: 1 for name in names}

    def insertRow(self, name: str, row: list[str]) -> None:
        rid = self.next_id[name]
        self.tables[name][rid] = row
        self.next_id[name] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        self.tables[name].pop(rowId, None)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId][columnId - 1]
