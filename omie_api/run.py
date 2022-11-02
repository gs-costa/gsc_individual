from endpoints import Endpoint, ApiOmie
import pandas as pd
import sched
import logging
from transformations import drop_useless, select_columns, rename_columns
from config import cols_movimentos,rename_movimentos, drop_movimentos, \
    cols_clientes, rename_clientes, cols_categorias, rename_categorias

scheduler = sched.scheduler()
 #app key e app secret de exemplo da omie, substitua pelos seus
omie_app_key = '38333295000'
omie_app_secret = 'fed2163e2e8dccb53ff914ce9e2f1258'

def run():
    logging.basicConfig(
        level = logging.INFO,
        format = '%(asctime)s %(name)s %(levelname)s %(message)s'
    )
    log = logging.getLogger(__name__)

    api_omie = ApiOmie(omie_app_key, omie_app_secret)

    log.info("Start request Categorias")
    lista_categorias = Endpoint.request_categorias(api_omie)

    log.info("Start request ListarMovimentos")
    lista_movimentos = Endpoint.request_movimentos((api_omie))

    log.info("Start request Clientes")
    lista_clientes = Endpoint.request_clientes(api_omie)

    df_categorias = pd.DataFrame(lista_categorias)
    df_clientes = pd.DataFrame(lista_clientes)
    df_movimentos = pd.json_normalize(lista_movimentos, max_level = 3)

    log.info("Transforming dfs")
    df_movimentos = select_columns(df_movimentos, cols_movimentos)
    df_movimentos = rename_columns(df_movimentos, rename_movimentos)
    df_clientes = select_columns(df_clientes, cols_clientes)
    df_clientes = rename_columns(df_clientes, rename_clientes)
    df_categorias = select_columns(df_categorias, cols_categorias)
    df_categorias = rename_columns(df_categorias, rename_categorias)

    log.info("Merging movimentos, clientes and categorias")
    df1 = pd.merge(
        df_movimentos, 
        df_categorias,
        on = 'cod_categoria')
    df2 = pd.merge(
        df1, 
        df_clientes, 
        on = 'cod_cliente')

    log.info("Filtering only revenue data")
    df2 = df2.query('conta_receita == "S"')

    log.info("Drop useless columns")
    df2 = drop_useless(df2, drop_movimentos)

    log.info("Save dataframe to xlsx file")
    path = r"Área de Trabalho\teste.xlsx" #path onde salvará seu arquivo xlsx
    
    writer = pd.ExcelWriter(path , engine='xlsxwriter')
    df2.to_excel(writer)
    writer.save()

if __name__ == '__main__':
    run()