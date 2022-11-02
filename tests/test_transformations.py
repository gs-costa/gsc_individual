import unittest
from scripts_gustavo.omie_api.transformations import change_status
import pandas as pd

data = [
    ['ATRASADO', '30/10/2022'],
    ['VENCIDO', '30/10/2022'],
    ['ATRASADO', '29/10/2022']]
df = pd.DataFrame(data, columns= ['status','dt_vencimento'])

class TestTransformations(unittest.TestCase):
    def test_change_status(self):
        # ATRASADO, 30/10/2022 -> Vence hoje (D+1) (boleto gerado)
        # VENCIDO, 30/10/2022 -> VENCIDO
        # ATRASADO, 29/10/2022 -> ATRASADO
        novodf = change_status(df)
        self.assertEqual(novodf.loc[0]['status'], 'Vence hoje (D+1) (boleto gerado)')

if __name__ == '__name__':
    unittest.main()