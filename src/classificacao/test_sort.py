import unittest
from collections import namedtuple

class TestClassificacao(unittest.TestCase):


    def load_payload(self):
        return {
            "name": "Payload",
            "parametros": [{
                "chave": "numero_contrato",
                "valor": "1234"
                 },
                {
                    "chave": "sigla_sistemica",
                    "valor": "b2"
                },
                {
                    "chave": "codigo_pessoa",
                    "valor": "777"
                },
                {
                    "chave": "data_liquidacao",
                    "valor": "23/01/2023"
                }
            ]
        }


    def obtemDado(self, payload):
        resultado = {}
        for dado in payload["parametros"]:
             resultado[dado["chave"]] = dado["valor"]

        return resultado


    def test_sort(self):
        # ordem codigo_pessoa, sigla_sitemica, numero_contrato, data_liquidacao
        payload = self.load_payload()

        Classificacao = namedtuple("Classificacao", "codigo_pessoa, data_liquidacao, sigla_sistemica, numero_contrato")

        dado = self.obtemDado(payload)

        valor = Classificacao(**dado)._asdict()

        self.assertTrue(len(valor.keys()), 5)
        print(valor)


