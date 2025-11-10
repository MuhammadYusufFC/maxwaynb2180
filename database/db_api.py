import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data


    def create_category_table(self):
        sql = """CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255)
        )"""
        self.execute(sql, commit=True)


    def create_products_table(self):
        sql = """CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            weight INTEGER,
            ingredients VARCHAR(255),
            photo VARCHAR(500),
            price REAL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category(id)

        )"""
        self.execute(sql, commit=True)

    # CATEGORY CRUD OPERATIONS
    def add_category(self, name: str) -> None:
        sql = """INSERT INTO category (name) VALUES (?)"""
        self.execute(sql, parameters=(name,), commit=True)
    
    def update_category(self, id: int, new_name: str) -> None:
        sql = '''UPDATE category SET name = ? WHERE id = ?'''
        self.execute(sql, parameters=(new_name, id))

    def delete_category(self, id: int) -> None:
        sql = """DELETE FROM category WHERE id = ?"""
        self.execute(sql, parameters=(id, ), commit=True)
    
    def select_categories(self):
        sql = """SELECT * FROM category"""
        return self.execute(sql, fetchall=True)
    
    def get_category_by_id(self, id: int) -> str:
        sql = "SELECT name FROM category WHERE id = ?"
        return self.execute(sql, parameters=(int(id), ), fetchone=True)

    # PRODUCT CRUD OPERATIONS
    def add_product(self, name, weight, ingredients, photo, price, category_id):
        sql = '''
        INSERT INTO product 
            (name, weight, ingredients, photo, price, category_id)
        VALUES
            (?, ?, ?, ?, ?, ?)
        '''
        self.execute(sql, (name, weight, ingredients, photo, price, category_id), commit=True)


    def delete_product(self, id):
        sql = """DELETE FROM product FROM id = ?"""
        self.execute(sql, commit=True)
    
    def select_product_by_category(self, category_name: str) -> list:
        sql = """
            SELECT id, name FROM product 
            WHERE category_id = (
                SELECT id FROM category WHERE name = ?
            )
        """
        return self.execute(sql, parameters=(category_name,), fetchall=True)
    
    def select_product_by_name(self, name: str) -> list:
        sql = '''SELECT * FROM product WHERE name = ?'''
        return self.execute(sql, parameters=(name, ), fetchone=True)
    

    



def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
    
