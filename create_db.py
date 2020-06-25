from model import Base, LondonBikes
from db_conection import engine

if __name__ == "__main__":
    flag = True
    if engine.dialect.has_table(engine, LondonBikes.__tablename__):
        flag = input(
            "Table already exists. Do you want to delete the existing table? (y/N) "
        ).lower()
        if flag == 'y':
            flag = True
        else:
            flag = False
    if flag:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)