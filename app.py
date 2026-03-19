import streamlit as st
import gspread
from google.auth import default
import pandas as pd

st.set_page_config(page_title="Imóveis Curitiba", layout="wide")

st.title("🏠 Imóveis em Curitiba")
st.write("Encontre os melhores imóveis para alugar em Curitiba")

# Conectar ao Google Sheets
creds, _ = default()
gc = gspread.authorize(creds)
sh = gc.open_by_key("1HZ11ayBVI8K-cpRBNDgS8Mf6J3pjwDGQgnwWkweHLxw")
worksheet = sh.sheet1

# Pegar dados
dados = worksheet.get_all_records()
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