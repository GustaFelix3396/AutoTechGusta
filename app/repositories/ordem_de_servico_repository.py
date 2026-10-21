from app.models.ordem_de_servico import OrdemDeServico

class OrdemDeServicoRepositorio:
    def __init__(self, database):
        self.database = database

    def criarTabela(self):
        cursor = self.database.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS OrdensDeServico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER NOT NULL,
                cliente_id INTEGER NOT NULL,
                veiculo_id INTEGER NOT NULL,
                mecanico_id INTEGER NOT NULL
            )
        """)

        self.database.commit()

    def salvar(self, ordem):
        cursor = self.database.cursor()

        cursor.execute("""
            INSERT INTO OrdensDeServico
            (numero, cliente_id, veiculo_id, mecanico_id)
            VALUES (?, ?, ?, ?)
        """, (
            ordem.numero,
            ordem.cliente.id,
            ordem.veiculo.id,
            ordem.mecanico.id
        ))

        ordem.id = cursor.lastrowid
        self.database.commit()

    def buscarPorId(self, id):
        cursor = self.database.cursor()

        cursor.execute("""
            SELECT * FROM OrdensDeServico WHERE id = ?
        """, (id,))

        registro = cursor.fetchone()

        return self.converterParaObjeto(registro) if registro else None

    def listarTodos(self):
        cursor = self.database.cursor()

        cursor.execute("SELECT * FROM OrdensDeServico")

        return [
            self.converterParaObjeto(r)
            for r in cursor.fetchall()
        ]

    def atualizar(self, ordem):
        cursor = self.database.cursor()

        cursor.execute("""
            UPDATE OrdensDeServico
            SET numero = ?, cliente_id = ?, veiculo_id = ?,
                mecanico_id = ?
            WHERE id = ?
        """, (
            ordem.numero,
            ordem.cliente.id,
            ordem.veiculo.id,
            ordem.mecanico.id,
            ordem.id
        ))

        self.database.commit()

    def deletar(self, id):
        cursor = self.database.cursor()

        cursor.execute("""
            DELETE FROM OrdensDeServico WHERE id = ?
        """, (id,))

        self.database.commit()

    def converterParaObjeto(self, registro):
        return OrdemDeServico(
            numero=registro[1],
            cliente=registro[2],
            veiculo=registro[3],
            mecanico=registro[4]
        )