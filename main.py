# Import necessary libraries
from pathlib import Path
import streamlit as st
from PIL import Image

# --- CONFIGURAÇÕES DE CAMINHO ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- CONFIGURAÇÕES GERAIS ---
TITULO_DA_PAGINA = "Portfólio | Renato Firmino"
ICON_DA_PAGINA = ":wave:"
NOME = "Renato Firmino"
DESCRICAO = """
Analista de Dados, auxiliando na análise de informações para apoiar decisões baseadas em dados.
"""
EMAIL = "renato.apf@hotmail.com"
REDES_SOCIAIS = {
    "LinkedIn": "https://www.linkedin.com/in/renato-firmino",
    "GitHub": "https://github.com/xRenatoW",
}
PROJETOS = {
    "🏆 Dashboard Financeiro - Python usando as bibliotecas pandas, yfinance e streamlit": {
        "Aplicação": "https://dashboardyf.streamlit.app/",
        "Repositório Git": "https://github.com/xRenatoW/streamlit"
    },
    "🏆 Bot de Análise de Escanteios - Analisa jogos em tempo real e envia por Telegram jogos com as estatísticas determinadas": {
        "Aplicação": "https://github.com/xRenatoW/Cantos_bot",
        "Repositório Git": "https://github.com/seu_nome/seu_repositorio_bot"
    },
    "🏆 Dashboard Fifa 23 - Python usando as bibliotecas Pandas e Streamlit": {
        "Aplicação": "https://dashboardfifa.streamlit.app",
        "Repositório Git": "https://github.com/xRenatoW/dashfifa"
    }
}


CERTIFICACOES = [
    "📜 Formado em Analise e Desenvolvimento de Sistemas (Uninove)",
    "📜 Certificação em Python para Análise de Dados (HashTag Treinamentos)",
    "📜 Certificado em Power Bi Impressionador (HashTag Treinamentos)",
    "📜 Certificado em Segurança da Informação (Fundação Bradesco)",
    "📜 Certificação em Formação em C# (Fundação Bradesco)",
    "📜 Certificado em Semana Python na Pratica (EmpowerData)",
    "📜 E muitas outras certificações relevantes para análise de dados.",
]

# Set Streamlit page configuration
st.set_page_config(page_title=TITULO_DA_PAGINA, page_icon=ICON_DA_PAGINA)

# --- CARREGAR CSS, PDF E FOTO DE PERFIL ---
with open(css_file, encoding='utf-8') as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- SEÇÃO DE HERÓI ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label=" 📄 Baixar Currículo",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- LINKS PARA REDES SOCIAIS ---
st.write('\n')
cols = st.columns(len(REDES_SOCIAIS))
for index, (plataforma, link) in enumerate(REDES_SOCIAIS.items()):
    cols[index].markdown(f"[{plataforma}]({link})")

# --- SOBRE MIM ---
st.write('\n')
st.subheader("Sobre Mim")
st.write(
    """
- 🌟 Apaixonado por dados e análise
- 🚀 Transição de Analista de Suporte Técnico para Ciência de Dados
- 📈 Experiência em criação de visualizações impactantes
- 🎓 Formado em Analise e Desenvolvimento de Sistemas
"""
)

# --- EXPERIÊNCIA E QUALIFICAÇÕES ---
st.write('\n')
st.subheader("Experiência e Qualificações")
st.write(
    """
- ✔️ Conclusão de projetos pessoais de análise de dados ao longo de 1 ano
- ✔️ Estudante dedicado de Ciência de Dados e Visualização
- ✔️ Criação de visualizações de dados personalizadas utilizando bibliotecas como Matplotlib e Seaborn.
- ✔️ Transição bem-sucedida de uma carreira anterior como Analista de Suporte Técnico para o campo de análise de dados.
- ✔️ Realização de análises estatísticas básicas em projetos próprios para extrair insights valiosos.
    """
)

# --- COMPETÊNCIAS ---
st.write('\n')
st.subheader("Habilidades Técnicas")
st.write(
    """
- 👩‍💻 Programação: Python (Scikit-learn, Pandas), SQL, 
- 📊 Visualização de Dados: PowerBi, MS Excel, Plotly
- 📚 Modelagem: Regressão Logística, Regressão Linear, Árvores de Decisão
- 🗄️ Bancos de Dados: Postgres, MongoDB, MySQL
"""
)
# --- Projetos e Conquistas ---
st.subheader("Projetos")
for projeto, links in PROJETOS.items():
    st.write(f"{projeto}")
    st.write(f"- [Aplicação]({links['Aplicação']})")
    st.write(f"- [Repositório Git]({links['Repositório Git']})")

# --- CERTIFICAÇÕES ---
st.write('\n')
st.subheader("Certificações")
for certificado in CERTIFICACOES:
    st.write(certificado)
