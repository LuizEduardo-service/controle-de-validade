import imp
from numpy import dtype
import streamlit as st
# from funcoes import define_minimo_recebimento, define_alerta_comercial
import random
from datetime import datetime

def produto_liberado():
        st.success('Produto Liberado')
        st.subheader('Resumo do Recebimento')
        st.write('Sku: 123')
        st.write('descrição: Controle Remoto')
        st.write('Data de Recebimento: ', format(dta_rec,'%d/%m/%Y'))
        st.write('Data de Fabricação: ', format(dta_fab,'%d/%m/%Y'))
        st.write('Data de Vencimento: ', format(dta_venc,'%d/%m/%Y'))
        st.write('Alerta Comercial: ', define_alerta_comercial(dta_venc, dta_fab))
        btn_finalizar = st.button('Finalizar', key='finalizar',help='clique aqui')

def define_alerta_comercial(dta_venc, dta_fab, percent = 0.25):
    """ define a data do alerta comercial"""

    data_final = dta_venc - ((dta_venc - dta_fab) * percent)

    return format(data_final,'%d/%m/%Y')


def define_minimo_recebimento(dta_venc, dta_fab, percent = 0.75):
    """Define a data minima para recebimento do produto"""

    data_final = dta_venc - ((dta_venc - dta_fab) * percent)
    return data_final

st.title('Controle de Validade')
usuario = st.number_input('Matricula do usuario:',format='%d',step=1,key='usuario')
sku = st.number_input('Numero Sku',format='%d',step=1,key='sku')
dta_rec = st.date_input('Data de Recebimento',key='dta_rec')
dta_fab = st.date_input('Data de Fabricação',key='dta_fab')
dta_venc = st.date_input('Data de Vencimento',key='dta_venc')

btn_consultar = st.button('Consultar',key='consultar')


if btn_consultar:
    dta_min_rec = define_minimo_recebimento(dta_venc, dta_fab)
    if dta_min_rec >= dta_rec:
        produto_liberado()
    else:
        st.error('Produto fora do prazo de validade')
        st.write('Deseja Receber mesmo assim?')
        opc_sim = st.button('Sim', key='opc_sim')
        opc_nao = st.button('Não', key='opc_nao')

        if opc_sim:
            produto_liberado()
        elif opc_nao:
            st.error('Produto fora do prazo de validade')
        else: 
            pass





