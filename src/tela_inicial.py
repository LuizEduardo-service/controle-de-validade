import streamlit as st
import random


st.title('Controle de Validade')
usuario = st.number_input('Matricula do usuario:',format='%d',step=1,key='usuario')
sku = st.number_input('Numero Sku',format='%d',step=1,key='sku')
dta_rec = st.date_input('Data de Recebimento',key='dta_rec')
dta_fab = st.date_input('Data de Fabricação',key='dta_fab')
dta_venc = st.date_input('Data de Vencimento',key='dta_venc')

btn_consultar = st.button('Consultar',key='consultar')


if btn_consultar:
    if dta_venc > dta_rec:
        st.success('Produto Liberado')

        st.write('Sku: 123')
        st.write('descrição: Controle Remoto')
        btn_finalizar = st.button('Finalizar', key='finalizar')
    else:
        st.error('Produto fora do prazo de validade')


