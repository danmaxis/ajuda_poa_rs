import requests
import pandas as pd

def get_spreadsheet_data(api_key, spreadsheet_id, range_name):
    url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}?key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data.get('values', []), columns=data['values'][0])
        df = df.drop(0).reset_index(drop=True)
        return df
    else:
        print('Falha na requisição:', response.status_code, response.text)
        return None