
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="💎 Pérola Negra – Bot Analítico de Vendas", layout="wide")

st.title("💎 Pérola Negra – Bot Analítico de Vendas")

uploaded_file = st.file_uploader("📂 Envie sua planilha de vendas (.xlsx)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.success("✅ Planilha carregada com sucesso!")

    receita_total = df["Receita"].sum()
    transacoes = len(df)
    ticket_medio = receita_total / transacoes if transacoes > 0 else 0
    produto_top = df.groupby("Produto")["Receita"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Receita Total", f"R$ {receita_total:,.2f}")
    col2.metric("🧾 Transações", transacoes)
    col3.metric("🎟️ Ticket Médio", f"R$ {ticket_medio:,.2f}")
    col4.metric("🏆 Produto Top", produto_top)

    st.divider()

    if "Categoria" in df.columns:
        fig_cat = px.pie(df, names="Categoria", values="Receita", title="📊 Receita por Categoria")
        st.plotly_chart(fig_cat, use_container_width=True)

    if "Região" in df.columns:
        fig_reg = px.bar(df, x="Região", y="Receita", title="📈 Receita por Região", color="Região")
        st.plotly_chart(fig_reg, use_container_width=True)
else:
    st.info("📄 Envie uma planilha para começar.")
