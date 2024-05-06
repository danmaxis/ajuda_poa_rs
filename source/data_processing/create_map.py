import folium
from folium.plugins import HeatMap
from folium import Popup
import pandas as pd

def build_popup_text(row):
    precisando = ', '.join(row['Precisando']) if row['Precisando'] else 'Nada'
    disponivel = ', '.join(row['Disponível']) if row['Disponível'] else 'Nada'
    pix = row['PIX'] or 'Não informado'
    return Popup(
        f" \
        <b>{row['LOCAL']}</b><br><br> \
        <b>Endereço:</b> {row['ENDEREÇO']}<br> \
        <b>Índice de Gravidade:</b> {row['Índice de Gravidade']}<br> \
        <b>Necessidades:</b> {precisando}<br> \
        <b>Disponível:</b> {disponivel}<br> \
        <b>PIX:</b> {pix}",
        max_width="90px"
    )


def create_map(df):
    # Criar um mapa centrado nas coordenadas médias
    map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
    folium_map = folium.Map(location=map_center, zoom_start=10)

    #remove rows with empty values for latitude and longitude
    df = df.dropna(subset=['Latitude', 'Longitude'])

    # Preparar dados para o mapa de calor
    heat_data = [[row['Latitude'], row['Longitude'], row['Índice de Gravidade']] for index, row in df.iterrows() if row['Latitude'] and row['Longitude']]

    # Adicionar o mapa de calor
    HeatMap(heat_data, radius=70,min_opacity=0.2).add_to(folium_map)

    # Adicionar marcadores
    for index, row in df.iterrows():
        if row['Latitude'] and row['Longitude']:
            folium.Marker(
                [row['Latitude'],
                row['Longitude']],
                popup=build_popup_text(row), 
                tooltip=row['LOCAL']
            ).add_to(folium_map)

    # Salvar o mapa em um arquivo HTML
    folium_map.save('heatmap.html')