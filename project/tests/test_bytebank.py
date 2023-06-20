from codigo.bytebank import Funcionario
import pytest
from pytest import mark


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

    def test_decrescimo_salario(self):
        entrada_salario = 100000  # Given
        entrada_nome = 'Camila Windsor'
        esperado = 90000

        funcionario_teste = Funcionario(
            entrada_nome, '11/02/1997', entrada_salario)
        funcionario_teste.decrescimo_salario()  # When
        resultado = funcionario_teste.salario

        assert resultado == esperado  # Then

    # Teste para a verificação de salario do funcionario e retornar seu bônus de acordo com seu salario

    @mark.calcular_bonus
    def test_receber_salario_e_retornar_bonus(self):
        entrada = 1000  # Given
        esperado = 100

        funcionario_teste = Funcionario('Ana', '12/03/1997', entrada)
        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == esperado  # Then

    # teste para ver se o salario do funcionario é grande de mais para receber o bônus e se for true retornar erro

    @mark.calcular_bonus
    def test_verificacao_de_salario_para_receber_bonus_e_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 10000000  # Given

            funcionario_teste = Funcionario('Ana', '12/03/1997', entrada)
            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado  # Then
