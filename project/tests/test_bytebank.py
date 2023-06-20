from codigo.bytebank import Funcionario


class TestClass:
    def test_receber_data_de_nascimento_e_retornar_idade(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23  # realizado no ano de 2023. Por favor mudar a idade de esperado para o ano atual

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_receber_e_retornar_sobrenome(self):
        entrada = ' Lucas Carvalho'  # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()  # When

        assert resultado == esperado  # Then
