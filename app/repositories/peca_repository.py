from app.models.peca import Peca

class PecaRepositorio:
    def __init__(self, database):
        self.database = database

    def criarTabela(self):
        cursor = self.database.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pecas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)

        self.database.commit()

    def salvar(self, peca):
        cursor = self.database.cursor()

        cursor.execute("""
            INSERT INTO Pecas (descricao, valor, quantidade)
            VALUES (?, ?, ?)
        """, (
            peca.descricao,
            peca.valor,
            peca.quantidade
        ))

        peca.id = cursor.lastrowid
        self.database.commit()

    def buscarPorId(self, id):
        cursor = self.database.cursor()

        cursor.execute("""
            SELECT * FROM Pecas WHERE id = ?
        """, (id,))

        registro = cursor.fetchone()

        return self.converterParaObjeto(registro) if registro else None

    def listarTodos(self):
        cursor = self.database.cursor()

        cursor.execute("SELECT * FROM Pecas")

        return [self.converterParaObjeto(r) for r in cursor.fetchall()]

    def atualizar(self, peca):
        cursor = self.database.cursor()

        cursor.execute("""
            UPDATE Pecas
            SET descricao = ?, valor = ?, quantidade = ?
            WHERE id = ?
        """, (
            peca.descricao,
            peca.valor,
            peca.quantidade,
            peca.id
        ))

        self.database.commit()

    def deletar(self, id):
        cursor = self.database.cursor()

        cursor.execute("DELETE FROM Pecas WHERE id = ?", (id,))

        self.database.commit()

    def converterParaObjeto(self, registro):
        peca = Peca(
            descricao=registro[1],
            valor=registro[2],
            quantidade=registro[3]
        )
        peca.id = registro[0]
        return peca