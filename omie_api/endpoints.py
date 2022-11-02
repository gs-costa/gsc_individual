from omie import ApiOmie
import pandas as pd
import logging

log = logging.getLogger(__name__)\

class Endpoint:

    def request_conta_a_receber(api_omie):

        registros = 500
        r = api_omie.request(
          url = 'https://app.omie.com.br/api/v1/geral/categorias/', 
          call = 'ListarCategorias', 
          params = {
            "pagina": 1,
            "registros_por_pagina": registros}).json()
        
        receber = r['conta_receber_cadastro']

        for n in range(1, r['total_de_paginas']):
            r = api_omie.request(
              url = 'https://app.omie.com.br/api/v1/geral/categorias/', 
              call = 'ListarCategorias',
              params = {
                "pagina": n+1,
                "registros_por_pagina": registros}).json()
            receber += r['conta_receber_cadastro']
        return receber

    def request_vendedores(api_omie):

        registros = 500
        r = api_omie.request(
          url = 'https://app.omie.com.br/api/v1/geral/vendedores/',
          call='ListarVendedores',
          params={
            "pagina": 1,
            "registros_por_pagina": registros,
            "apenas_importado_api": "N"}).json()

        vendedores = r['cadastro']
        
        for i in range(1, r['total_de_registros']):
          r = api_omie.request(
          url = 'https://app.omie.com.br/api/v1/geral/vendedores/',
          call='ListarVendedores',
          params={
            "pagina": i+1,
            "registros_por_pagina": registros,
            "apenas_importado_api": "N"}).json()
         
          vendedores += r['cadastro']
        return vendedores

    def request_clientes(api_omie):

        registros = 500
        r = api_omie.request(
          url = 'https://app.omie.com.br/api/v1/geral/clientes/', 
          call = 'ListarClientes',
          params = {
            "pagina": 1,
            "registros_por_pagina": registros,
            "apenas_importado_api": "N"}).json()
        
        clientes = r['clientes_cadastro']
        
        for n in range(1, r['total_de_paginas']):

            r = api_omie.request(
              url = 'https://app.omie.com.br/api/v1/geral/clientes/', 
              call = 'ListarClientes', 
              params = {
                "pagina": n+1,
                "registros_por_pagina": registros,
                "apenas_importado_api": "N"}).json()
            
            clientes += r['clientes_cadastro']
        return clientes

    def request_movimentos(api_omie):

        registros = 500
        r = api_omie.request(
          url = 'https://app.omie.com.br/api/v1/financas/mf/', 
          call = 'ListarMovimentos', 
          params = {
            "npagina": 1,
            "nRegPorPagina": registros}).json()
        log.info(f"Number of pages on Movimentos: {r['nTotPaginas']}")
        
        lista = r['movimentos'] #aproveita a primeira chamada para agregar ao dict

        for n in range(2, r['nTotPaginas'] + 1):

            log.info(f"Request number {n}")
            r = api_omie.request(
              url = 'https://app.omie.com.br/api/v1/financas/mf/', 
              call = 'ListarMovimentos', 
              params = {
                "npagina": n,
                "nRegPorPagina": registros}).json()
            try:
                lista = lista + r['movimentos']
            except:
                continue
        return lista

    def request_categorias(api_omie):

        registros = 500
        r = api_omie.request(
          url = 'https://app.omie.com.br/api/v1/geral/categorias/',
          call = 'ListarCategorias',
          params = {
            "pagina": 1,
            "registros_por_pagina": registros}).json()
        
        categorias = r['categoria_cadastro']

        for n in range(1, r['total_de_paginas']):

            r = api_omie.request(
              url = 'https://app.omie.com.br/api/v1/geral/categorias/',
              call = 'ListarCategorias',
              params = {
                "pagina": n+1,
                "registros_por_pagina": registros}).json()
            categorias += r['categoria_cadastro']

        return categorias