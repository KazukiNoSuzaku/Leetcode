# Author: Kaustav Ghosh
# Problem: Design SQL
# Approach: Hold each table as a dictionary from row id to its cells, plus the next id to hand out, which keeps growing so removals never free an id for reuse. Inserts check the table name and the column count, and lookups on a missing table, row or column report "<null>"; since ids only ever grow, the dictionary already holds the rows in id order for exports

class SQL(object):

    def __init__(self, names, columns):
        """
        :type names: List[str]
        :type columns: List[int]
        """
        self.columns = dict(zip(names, columns))
        self.tables = {name: {} for name in names}
        self.next_id = {name: 1 for name in names}

    def ins(self, name, row):
        """
        :type name: str
        :type row: List[str]
        :rtype: bool
        """
        if name not in self.columns or len(row) != self.columns[name]:
            return False
        self.tables[name][self.next_id[name]] = row
        self.next_id[name] += 1
        return True

    def rmv(self, name, rowId):
        """
        :type name: str
        :type rowId: int
        :rtype: None
        """
        if name in self.tables:
            self.tables[name].pop(rowId, None)

    def sel(self, name, rowId, columnId):
        """
        :type name: str
        :type rowId: int
        :type columnId: int
        :rtype: str
        """
        row = self.tables.get(name, {}).get(rowId)
        if row is None or not 1 <= columnId <= len(row):
            return "<null>"
        return row[columnId - 1]

    def exp(self, name):
        """
        :type name: str
        :rtype: List[str]
        """
        return [",".join([str(row_id)] + row)
                for row_id, row in self.tables.get(name, {}).items()]
