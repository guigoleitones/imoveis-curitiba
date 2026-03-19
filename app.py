import streamlit as st
import pandas as pd

st.set_page_config(page_title="Imóveis Curitiba", layout="wide")

st.title("🏠 Imóveis em Curitiba")
st.write("Encontre os melhores imóveis para alugar em Curitiba")

# Dados direto no código
dados = {
    "Título": [
        "Apartamento 2Q - Centro",
        "Casa 3Q - Batel",
        "Studio - Água Verde",
        "Terreno - Portão"
    ],
    "Preço": ["R$ 1.500", "R$ 2.500", "R$ 800", "R$ 5.000"],
    "Localização": ["Centro", "Batel", "Água Verde", "Portão"],
    "Descrição": ["Bem localizado", "Com garagem", "Mobiliado", "500m²"],
    "Link": [
        "https://www.olx.com.br/imoveis/apartamento-2-quartos-centro-curitiba",
        "https://www.zapimoveis.com.br/aluguel/apartamento-3-quartos-batel-curitiba-pr",
        "https://www.imoveiswebcuritiba.com.br/studio-agua-verde",
        "https://www.vilarealcuritiba.com.br/terreno-portao"
    ],
    "Site": ["OLX", "Zap", "Imóveis Web", "Vila Real"],
    "Data": ["19/03/2026", "19/03/2026", "19/03/2026", "19/03/2026"]
}

df = pd.DataFrame(dados)

# Filtros
col1, col2 = st.columns(2)

with col1:
    site_filter = st.selectbox("Filtrar por site:", ["Todos"] + list(df["Site"].unique()))

with col2:
    localizacao_filter = st.selectbox("Filtrar por localização:", ["Todos"] + list(df["Localização"].unique()))

# Filtrar dados
if site_filter != "Todos":
    df = df[df["Site"] == site_filter]

if localizacao_filter != "Todos":
    df = df[df["Localização"] == localizacao_filter]

# Mostrar imóveis
st.subheader(f"📊 Total: {len(df)} imóveis encontrados")

for idx, row in df.iterrows():
    with st.container():
        st.markdown(f"### {row['Título']}")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.write(f"💰 **{row['Preço']}**")
        with col2:
            st.write(f"📍 {row['Localização']}")
        with col3:
            st.write(f"🏢 {row['Site']}")
        with col4:
            st.write(f"📅 {row['Data']}")
        
        st.write(f"_{row['Descrição']}_")
        st.markdown(f"[🔗 Ver anúncio]({row['Link']})")
        st.divider()
