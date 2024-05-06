from dicts.urgency_mapping import URGENCY_MAPPING

def calculate_gravity(row):
    col_voluntarios = 'VOLUNTÁRIOS'
    col_donations = 'DOAÇÕES'
    # Put values in same case
    row[col_voluntarios] = row[col_voluntarios].lower()
    row[col_donations] = row[col_donations].lower()

    # Calcular o índice de gravidade somando os níveis de urgência
    volunteer_urgency = URGENCY_MAPPING.get(row[col_voluntarios], 0)
    donation_urgency = URGENCY_MAPPING.get(row[col_donations], 0)
    return volunteer_urgency * donation_urgency