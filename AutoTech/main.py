from app.models.cliente import Cliente
from app.models.veiculo import Veiculo
from app.models.mecanico import Mecanico
from app.models.serviço import Servico
from app.models.peça import Peça



def main():
    cliente = Cliente("João da Silva", "34 99999-9999")
    veiculo = Veiculo("ABC-1234", "Toyota Corolla", 2020)
    mecanico = Mecanico("Vitor Ferrari", "34 1234-5678", "Mecanico Geral")
    servico = Servico("Troca da Câmara de Ar", 80)
    peça = Peça("Câmara de Ar Aro 22", 129.00, 23)

    print("=== OficinaTech ===")
    print(f"Cliente: {cliente.nome}")
    print(f"Telefone: {cliente.telefone}")
    print(f"Veículo: {veiculo.modelo}")
    print(f"Placa: {veiculo.placa}")
    print(f"Ano: {veiculo.ano}")

    print(f"\n=== Mecânico ===")
    print(f"Mecânico: {mecanico.nome}")
    print(f"Telefone: {mecanico.telefone}")
    print(f"Especialidade: {mecanico.especialidade}")

    print(f"\n=== Serviço ===")
    print(f"Serviço: {servico.descricao}")
    print(f"Valor do Serviço: {servico.valor}")

    print(f"\n=== Peça ===")
    print(f"Peça: {peça.descricao}")
    print(f"Valor da Peça: {peça.valor}")
    print(f"Quantidade em Estoque: {peça.quantidade}")


if __name__ == "__main__":
    main()
