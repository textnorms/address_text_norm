'''
    Dicionário para simular erros de OCR, dde modo que letras
    semelhantes podem ser trocadas por números similares ou letras
    que possuem formato parecido podem ser trocadas entre-si.
'''
lookalike_chars = {
    'o':'0',
    '0':'o',
    'c':'ç',
    'ç':'c',
    'l':'i',
    'i':'l',
    'n':'m',
    'm':'n',
    'u':'v',
    'v':'u',
    '9':'g',
    'g':'9'
}

'''
    Dict with most commom  pt_BR abbreviations 
'''
'''
    Commom Brazilian Portuguese abbreviations used
    in addresses dict
'''
abbreviations_dict = {
    'Rua':'R.',
    'Avenida':'Av.',
    'Travessa':'Tv.',
    'Praça':'Pç.',
    'Jardim':'Jd.',
    'Cidade':'Cid.',
    'Torre':'T.',
    'Apartamento':'Apto.',
    'São':'S.',
    'Santo':'Sto.',
    'Santa':'Sta.',
    'Vila':'Vl.',
    'Rodovia':'Rod.',
    'Parque':'Prq.',
    'Sul':'S.',
    'Condomínio':'Cond.',
}