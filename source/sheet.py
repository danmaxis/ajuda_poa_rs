import os
from api.google_sheets import get_spreadsheet_data
from data_processing import calculate_gravity, parse_needs, geocode_addresses, create_map
import pandas as pd

# Get data from csv file
try:
    df = pd.read_csv('data.csv')
    # Parse Precisando and Disponível columns as lists
    df['Precisando'] = df['Precisando'].apply(lambda x: x[1:-1].split(', ') if isinstance(x, str) else [])
    df['Disponível'] = df['Disponível'].apply(lambda x: x[1:-1].split(', ') if isinstance(x, str) else [])
    df['PIX'] = df['PIX'].apply(lambda x: x[1:-1].split(', ') if isinstance(x, str) else [])

    # Empty "LOCAL" column values put "Local não informado"
    df['LOCAL'] = df['LOCAL'].fillna('Local não informado')
    
except FileNotFoundError:
    df = None

if df is None:
    api_key = os.getenv('GOOGLE_API_KEY')
    spreadsheet_id = '1zaYIEfmbtOTrKCqwecS9w0mwgUzIqpB-ujf15lQ_L_8'
    range_name = 'Sheet1'
    # Get data from Google Sheets
    df = get_spreadsheet_data(api_key, spreadsheet_id, range_name)

    df = df.drop(0).reset_index(drop=True)  # Limpar os cabeçalhos duplicados se existirem
    # Remove lines with empty values
    # df = df.dropna()
    df['Índice de Gravidade'] = df.apply(calculate_gravity, axis=1)
    df[['Precisando', 'Disponível', 'PIX']] = df['OBS'].apply(parse_needs)

    # Extract all items in the 'Precisando' and 'Disponível' columns
    needs = df['Precisando'].explode().dropna().unique()
    available = df['Disponível'].explode().dropna().unique()

    # Empty "ENDEREÇO" column values put df['LOCAL'] + "Porto Alegre, RS"
    df['ENDEREÇO'] = df['ENDEREÇO'].fillna(df['LOCAL'] + ', Porto Alegre, RS')
    
    # Empty "LOCAL" column values put "Local não informado"
    df['LOCAL'] = df['LOCAL'].fillna('Local não informado')
    
    # Print df summary
    print(df.info())

    # Geocode addresses
    df = geocode_addresses(df, 'ENDEREÇO')

    #save the dataframe to a csv file
    df.to_csv('data.csv', index=False)

if df is not None:
    # Create map
    create_map(df)


    
