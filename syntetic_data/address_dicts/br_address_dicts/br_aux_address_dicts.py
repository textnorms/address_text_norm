'''
    This file implements dicts to help implementation of
    auxiliary dicts.    
'''
from collections import OrderedDict
from random import randint

'''
    Brazilian states abbreviations and complete names
'''
br_states_dict = {
    'TO':'Tocantins',
    'SE':'Sergipe',
    'SP':'São Paulo',
    'SC':'Santa Catarina',
    'RR':'Roraima',
    'RO':'Rondônia',
    'RS':'Rio Grande do Sul',
    'RN':'Rio Grande do Norte',
    'RJ':'Rio de Janeiro',
    'PI':'Piauí',
    'PE':'Pernambuco',
    'PR':'Paraná',
    'PB':'Paraíba',
    'PA':'Pará',
    'MG':'Minas Gerais',
    'MS':'Mato Grosso do Sul',
    'MT':'Mato Grosso',
    'MA':'Maranhão',
    'GO':'Goiás',
    'ES':'Espírito Santo',
    'DF':'Distrito Federal',
    'CE':'Ceará',
    'BA':'Bahia',
    'AM':'Amazonas',
    'AP':'Amapá',
    'AL':'Alagoas',
    'AC':'Acre'
}

'''
    Generates a complemento information with reasonable
    informations
'''
complemento_list = [
    f'Torre {randint(1,10)} - Apartamento {randint(1,200)}',
    f'Torre {randint(1,10)}',
    f'Apartamento {randint(1,200)}',
    f'Sala {randint(1,200)}',
    f'Torre {randint(1,10)} - Sala {randint(1,200)}',
    f'Box {randint(1,100)}',
    f'Loja {randint(1,100)}',
    f'Bloco {randint(1,20)} - Sala {randint(1,200)}',
    f'Hangar {randint(1,20)}'
]