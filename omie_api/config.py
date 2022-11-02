cols_movimentos = [
    'detalhes.cStatus', 'detalhes.nCodCliente', 'detalhes.dDtPrevisao', #previsao_recebimento
    'detalhes.dDtPagamento', #ultimo_recebimento
    'detalhes.nValorTitulo', #valor_da_conta
    'resumo.nValPago', #valor_recebido
    'resumo.nValAberto', #valor_a_receber
    'detalhes.cCodCateg', 'detalhes.dDtVenc', 'detalhes.dDtEmissao', 'detalhes.cCPFCNPJCliente',
    'detalhes.nCodTitulo',
    'detalhes.cOrigem'] #n_do_contrato_de_venda

rename_movimentos = {
    'detalhes.cStatus': 'status', 
    'detalhes.nCodCliente': 'cod_cliente',
    'detalhes.dDtPrevisao': 'previsao_recebimento', #previsao_recebimento
    'detalhes.dDtPagamento': 'ultimo_recebimento', #ultimo_recebimento
    'detalhes.nValorTitulo': 'valor_da_conta', #valor_da_conta
    'resumo.nValPago': ' valor_recebido', #valor_recebido
    'resumo.nValAberto': 'valor_a_receber', #valor_a_receber
    'detalhes.cCodCateg': 'cod_categoria', 
    'detalhes.dDtVenc': 'dt_vencimento', 
    'detalhes.dDtEmissao': 'dt_emissao',
    'detalhes.cCPFCNPJCliente': 'CPFCNPJCliente',
    'detalhes.nCodTitulo': 'n_do_contrato_de_venda',
    'detalhes.cOrigem': 'cod_origem'}

drop_movimentos = ['cod_cliente', 'conta_receita']

cols_clientes = [
    'codigo_cliente_omie', 'nome_fantasia', 'razao_social'
]

rename_clientes = {
    'codigo_cliente_omie': 'cod_cliente'
}

cols_categorias = [
    'codigo', 'descricao', 'conta_receita'
]

rename_categorias = {
    'codigo': 'cod_categoria',
    'descricao': 'categoria'
}