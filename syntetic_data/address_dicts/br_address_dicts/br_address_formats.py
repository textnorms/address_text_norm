'''
    This file implements the format of
'''

from .br_aux_address_dicts import br_states_dict
from .br_aux_address_functions import complemento_generation

def format1(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        Returning a non cannonical order:
        numero,logradouro,complemento,bairro,cidade,uf,cep
    '''

    target = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}, {cep}'
    sample = f'{numero}, {logradouro}, {bairro}, {cidade}, {uf}, {cep}'

    return sample, target

def format2(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the cannonical format
    '''
    
    target = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}, {cep}'
    sample = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}, {cep}'

    return sample, target

def format3(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the following format:
        Altura do 123 na Rua das Matas no Residencial Norte Sul de Aparecida de Goiania
    '''
    
    target = f'{logradouro}, {numero}, {bairro}, {cidade}'
    sample = f'Altura do {numero} na {logradouro} no {bairro} de {cidade}'

    return sample, target

def format4(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Rua das Matas, 123, Residencial Norte Sul, Aparecida de Goiania, Goiás, 74946630
    '''

    sample = f'{logradouro}, {numero}, {bairro}, {cidade}, {br_states_dict[uf]}, {cep}'
    target = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}, {cep}'

    return sample, target

def format5(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Rua das Matas, 123, Residencial Norte Sul, Aparecida de Goiania, Goiás    
    '''

    sample = f'{logradouro}, {numero}, {bairro}, {cidade}, {br_states_dict[uf]}'
    target = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}'

    return sample, target

def format6(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Número 123 da Rua das Matas no Residencial Norte Sul de Aparecida de Goiania    
    '''

    sample = f'Número {numero} da {logradouro} no {bairro} de {cidade}'
    target = f'{logradouro}, {numero}, {bairro}, {cidade}'

    return sample, target


def format7(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        GO, Aparecida de Goiania, Residencial Norte Sul, Rua das Matas, 123    
    '''

    target = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}'
    sample = f'{uf}, {cidade}, {bairro}, {numero}, {logradouro}'

    return sample, target


def format8(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Goiás, Aparecida de Goiania, Residencial Norte Sul, Rua das Matas, 123    
    '''

    target = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}'
    sample = f'{br_states_dict[uf]}, {cidade}, {bairro}, {numero}, {logradouro}'

    return sample, target

def format9(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Logradouro: Rua das Matas, Número: 123, Bairro: Residencial Norte Sul, Cidade: Aparecida de Goiania, Estado: GO, CEP: 74946630    
    '''

    target = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}'
    sample = f'Logradouro: {logradouro}, Número: {numero}, Bairro: {bairro}, Cidade: {cidade}, Estado: {uf}'

    return sample, target

def format10(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        Rua das Matas, Sem número, Residencial Norte Sul, Aparecida de Goiania, GO, 74946630
    '''

    target = f'{logradouro}, S/N, {bairro}, {cidade}, {uf}'
    sample = f'{logradouro}, Sem número, {bairro}, {cidade}, {uf}'
    
    return sample,target

def format11(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        Rua das Matas, Residencial Norte Sul, Aparecida de Goiania, GO, 74946630
    '''

    target = f'{logradouro}, S/N, {bairro}, {cidade}, {uf}'
    sample = f'{logradouro}, {bairro}, {cidade}, {uf}'
    
    return sample,target


def format12(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        Returning a non cannonical order:
        numero,logradouro,complemento,bairro,cidade,uf,cep with complement
    '''

    complemento_text = complemento_generation()

    target = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}, {uf}, {cep}'
    sample = f'{numero}, {logradouro}, {complemento_text}, {bairro}, {cidade}, {uf}, {cep}'

    return sample, target

def format13(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the cannonical format with complement
    '''
    complemento_text = complemento_generation()
    
    target = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}, {uf}, {cep}'
    sample = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}, {uf}, {cep}'

    return sample, target


def format14(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the following format:
        Altura do 123 na Rua das Matas no Residencial Norte Sul de Aparecida de Goiania with complemento
    '''
    complemento_text = complemento_generation()
    
    target = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}'
    sample = f'{complemento_text} na altura do {numero} na {logradouro} no {bairro} de {cidade}'

    return sample, target

def format15(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Rua das Matas, 123, Residencial Norte Sul, Aparecida de Goiania, Goiás, 74946630 with complemento
    '''
    complemento_text = complemento_generation()

    sample = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}, {br_states_dict[uf]}, {cep}'
    target = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}, {uf}, {cep}'

    return sample, target

def format16(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Rua das Matas, 123, Residencial Norte Sul, Aparecida de Goiania, Goiás with complemento
    '''
    complemento_text = complemento_generation()

    sample = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}, {br_states_dict[uf]}'
    target = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}, {uf}'

    return sample, target

def format17(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Número 123 da Rua das Matas no Residencial Norte Sul de Aparecida de Goiania with complemento
    '''
    complemento_text = complemento_generation()

    sample = f'{complemento_text} número {numero} da {logradouro} no {bairro} de {cidade}'
    target = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}'

    return sample, target


def format18(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        GO, Aparecida de Goiania, Residencial Norte Sul, Rua das Matas, 123, complemento
    '''
    complemento_text = complemento_generation()

    target = f'{logradouro}, {numero}, {complemento_text} ,{bairro}, {cidade}, {uf}'
    sample = f'{uf}, {cidade}, {bairro}, {logradouro}, {numero}, {complemento_text}'

    return sample, target


def format19(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Goiás, Aparecida de Goiania, Residencial Norte Sul, Rua das Matas, 123 with complemento    
    '''
    complemento_text = complemento_generation()

    target = f'{logradouro}, {numero}, {bairro}, {cidade}, {uf}'
    sample = f'{br_states_dict[uf]}, {cidade}, {bairro}, {logradouro}, {numero}, {complemento_text}'

    return sample, target

def format20(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        This format implements the canonical format with extensive state name:
        Logradouro: Rua das Matas, Número: 123, Bairro: Residencial Norte Sul,
        Cidade: Aparecida de Goiania, Estado: GO, CEP: 74946630 with complemento
    '''
    complemento_text = complemento_generation()

    target = f'{logradouro}, {numero}, {complemento_text}, {bairro}, {cidade}, {uf}'
    sample = f'Logradouro: {logradouro}, Número: {numero}, Complemento:{complemento_text}, Bairro: {bairro}, Cidade: {cidade}, Estado: {uf}'

    return sample, target

def format21(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        Rua das Matas, Sem número, Residencial Norte Sul, Aparecida de Goiania, GO, 74946630 with complemento
    '''
    complemento_text = complemento_generation()

    target = f'{logradouro}, S/N, {complemento_text},{bairro}, {cidade}, {uf}'
    sample = f'{logradouro}, Sem número, {complemento_text}, {bairro}, {cidade}, {uf}'
    
    return sample,target

def format22(logradouro,numero,complemento,bairro,cidade,uf,cep):
    '''
        Rua das Matas, Residencial Norte Sul, Aparecida de Goiania, GO, 74946630 with complemento
    '''
    complemento_text = complemento_generation()

    target = f'{logradouro}, S/N, {complemento_text},{bairro}, {cidade}, {uf}'
    sample = f'{logradouro}, {complemento_text},{bairro}, {cidade}, {uf}'
    
    return sample,target

address_formats = {
    '1':format1,
    '2':format2,
    '3':format3,
    '4':format4,
    '5':format5,
    '6':format6,
    '7':format7,
    '8':format8,
    '9':format9,
    '10':format10,
    '11':format11,
    '12':format12,
    '13':format13,
    '14':format14,
    '15':format15,
    '16':format16,
    '17':format17,
    '18':format18,
    '19':format19,
    '20':format20,
    '21':format21,
    '22':format22
}