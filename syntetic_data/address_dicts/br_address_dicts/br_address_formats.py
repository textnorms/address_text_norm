'''
    This file implements the format of
'''

def format1(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        Returning a non cannonical order:
        numero,logradouro,complemento,bairro,cidade,uf,cep
    '''

    target = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}, {cep}'
    sample = f'{numero}, {logradouro}, {bairro}, {cidade}, {uf}, {cep}'

    return sample, target


address_formats = {
    '1':format1
}