import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Imóveis Curitiba", layout="wide")

st.title("🏠 Imóveis em Curitiba")
st.write("Os imóveis mais recentes para alugar em Curitiba")

# Dados direto no código
dados = {
    "Título": [
        "Apartamento 2Q - Centro",
        "Casa 3Q - Batel",
        "Studio - Água Verde",
        "Terreno - Portão"
    ],
    "Preço": ["R$ 1.500", "R$ 2.500", "R$ 800", "R$ 5.000"],
    "Bairro": ["Centro", "Batel", "Água Verde", "Portão"],
    "Descrição": ["Bem localizado", "Com garagem", "Mobiliado", "500m²"],
    "Link": [
        "https://www.olx.com.br/imoveis/apartamento-2-quartos-centro-curitiba",
        "https://www.zapimoveis.com.br/aluguel/apartamento-3-quartos-batel-curitiba-pr",
        "https://www.imoveiswebcuritiba.com.br/studio-agua-verde",
        "https://www.vilarealcuritiba.com.br/terreno-portao"
    ],
    "Site": ["OLX", "Zap", "Imóveis Web", "Vivareal"],
    "Data Coletado": ["19/03/2026", "19/03/2026", "19/03/2026", "19/03/2026"]
}

df = pd.DataFrame(dados)

# Converter data para datetime para ordenar corretamente
df['Data Coletado'] = pd.to_datetime(df['Data Coletado'], format='%d/%m/%Y')

# Filtro por bairro (opcional)
col1, col2 = st.columns(2)

with col1:
    bairro_filter = st.selectbox("Filtrar por bairro:", ["Todos"] + sorted(df["Bairro"].unique().tolist()))

with col2:
    st.write("")  # Espaço vazio

# Filtrar dados
if bairro_filter != "Todos":
    df_filtrado = df[df["Bairro"] == bairro_filter]
else:
    df_filtrado = df.copy()

# ORDENAR POR DATA (MAIS RECENTES PRIMEIRO)
df_filtrado = df_filtrado.sort_values('Data Coletado', ascending=False)

# Mostrar imóveis
st.subheader(f"📊 Total: {len(df_filtrado)} imóveis encontrados")

for idx, row in df_filtrado.iterrows():
    with st.container():
        st.markdown(f"### {row['Título']}")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.write(f"💰 **{row['Preço']}**")
        with col2:
            st.write(f"📍 {row['Bairro']}")
        with col3:
            st.write(f"🏢 {row['Site']}")
        with col4:
            st.write(f"📅 {row['Data Coletado'].strftime('%d/%m/%Y')}")
        
        st.write(f"_{row['Descrição']}_")
        st.markdown(f"[🔗 Ver anúncio]({row['Link']})")
        st.divider()
