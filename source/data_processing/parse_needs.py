import pandas as pd

# Função para extrair informações de OBS
def parse_needs(obs):
    if not obs:
        return pd.Series({'Precisando': '', 'Disponível': '', 'PIX': ''})
    parts = {'Precisando': '', 'Disponível': '', 'PIX': ''}

    if 'PRECISANDO:' in obs:
        parts['Precisando'] = obs.split('PRECISANDO:')[1].split('DISPONÍVEL:')[0].strip().split(',')
    if 'DISPONÍVEL:' in obs:
        disponivel_part = obs.split('DISPONÍVEL:')[1].split('PIX:')[0].strip().split(',')
        parts['Disponível'] = disponivel_part.split('PIX:')[0].strip().split(',') if 'PIX:' in disponivel_part else disponivel_part[0].strip().split(',')
    if 'PIX:' in obs:
        parts['PIX'] = obs.split('PIX:')[-1].strip()

    # Set column values to lowercase
    obs = obs.lower()
    
    return pd.Series(parts)