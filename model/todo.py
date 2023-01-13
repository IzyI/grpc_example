from piccolo.columns import Boolean, Varchar,Integer
from piccolo.engine.sqlite import SQLiteEngine
from piccolo.table import Table, create_tables

DB = SQLiteEngine("bd.sqlite")


class Todo(Table, db=DB):
    name = Varchar()
    completed = Boolean(default=False)
    day = Integer(default=0)
