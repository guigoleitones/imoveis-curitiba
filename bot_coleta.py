import requests
import gspread
from google.auth import default
from datetime import datetime
import json
import os

print("🤖 Bot iniciado...")

# Credenciais (vamos configurar depois)
creds_dict = json.loads(os.environ.get('GOOGLE_CREDENTIALS', '{}'))

if creds_dict:
    from google.oauth2.service_account import Credentials
    creds = Credentials.from_service_account_info(creds_dict)
    gc = gspread.authorize(creds)
    sh = gc.open_by_key('1HZ11ayBVI8K-cpRBNDgS8Mf6J3pjwDGQgnwWkweHLxw')
    worksheet = sh.sheet1
    
    imoveis = []
    
    # ===== COLETAR DE OLX =====
    print("🔍 Buscando em OLX...")
    try:
        url = "https://www.olx.com.br/imoveis/aluguel/apartamento/curitiba-pr"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        
        # Extrair links (método simples)
        if "olx.com.br" in response.text:
            print("✅ OLX acessado")
    except Exception as e:
        print(f"❌ Erro OLX: {e}")
    
    # ===== COLETAR DE ZAP =====
    print("🔍 Buscando em Zap...")
    try:
        url = "https://www.zapimoveis.com.br/aluguel/apartamento/curitiba-pr/"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if "zapimoveis.com.br" in response.text:
            print("✅ Zap acessado")
    except Exception as e:
        print(f"❌ Erro Zap: {e}")
    
    # ===== ADICIONAR EXEMPLO =====
    novo_imovel = [
        f"Apartamento coletado - {datetime.now().strftime('%d/%m/%Y')}",
        "R$ 1.800",
        "Centro",
        "Coletado automaticamente",
        "https://olx.com.br/exemplo",
        "OLX",
        datetime.now().strftime('%d/%m/%Y')
    ]
    
    worksheet.append_row(novo_imovel)
    print(f"✅ Imóvel adicionado: {novo_imovel[0]}")
    print("✅ Bot finalizado com sucesso!")
else:
    print("❌ Credenciais não configuradas")
