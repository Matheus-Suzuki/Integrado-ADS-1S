import sqlite3

class management:
    def __init__ (self, database):
        self.conn = sqlite3.connect(database)
        self.createDB()

# Criação da tabela caso não exista.

    def createDB(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock (
            id INTEGER PRIMARY KEY, 
            product TEXT, 
            amount INTEGER
            ) 
        ''')
        self.conn.commit()

# Adicionar produto.

    def addProduct(self, product, amount):
        cursor = self.conn.cursor()
        cursor.execute(
            '''INSERT INTO stock (product, amount) VALUES (?, ?)''', (product, amount))
        self.conn.commit()

# Remover produto.

    def removeProduct(self, product, amount):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT amount FROM stock WHERE product=?", (product))
        result = cursor.fetchone()

        if result:
            currentstock = result[0]
            if currentstock >= amount:
                cursor.execute("UPDATE stock SET amount=? WHERE product=?",(currentstock - amount, product))
                self.conn.commit()
            else:
                print(f'Valor invalido.\nQuantidade do produto "{product}" insuficiente para essa operação.')  
        else:
            print(f'O produto "{product}" não foi enconntrado.')  
        
# connsultar estoque.

    def connsultProduct(self, product):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT amount FROM stock WHERE product=?", [product])
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0

# Lista de produtos.

    def connsultProducts(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT product FROM stock")
        products = cursor.fetchall()
        return [product[0] for product in products]

#-------------------------------------------------------------------------------------------------------------
        
