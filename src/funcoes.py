from datetime import datetime

def define_alerta_comercial(dta_venc, dta_fab, percent = 0.25):
    """ define a data do alerta comercial"""

    data_final = dta_venc - ((dta_venc - dta_fab) * percent)

    return format(data_final,'%d/%m/%Y')


def define_minimo_recebimento(dta_venc, dta_fab, percent = 0.75):
    """Define a data minima para recebimento do produto"""

    data_final = dta_venc - ((dta_venc - dta_fab) * percent)
    return format(data_final,'%d/%m/%Y')
