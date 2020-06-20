'''
    This file implements the format of
'''

from .br_aux_address_dicts import br_states_dict

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
    '11':format11
}