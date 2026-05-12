# ==============================
# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# ==============================

import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ==============================
# 2. CONFIGURAÇÃO DA PÁGINA
# ==============================

st.set_page_config(
    page_title="Simulador de Risco de Defasagem",
    page_icon="🏫",
    layout="wide"
)

st.markdown(
    '<meta name="google" content="notranslate">',
    unsafe_allow_html=True
)


# ==============================
# 3. TÍTULO
# ==============================

st.title(
    "Simulador de Risco de Defasagem"
)

st.markdown(
    """
    Aplicação desenvolvida para auxiliar na identificação
    de possíveis alunos em risco de defasagem educacional
    com base nos indicadores da ONG Passos Mágicos.
    """
)


# ==============================
# 4. CARREGAMENTO DO MODELO
# ==============================

modelo = joblib.load(
    'modelo_defasagem.pkl'
)


# ==============================
# 5. SIDEBAR
# ==============================

st.sidebar.header(
    "Indicadores do Aluno"
)

st.sidebar.markdown(
    """
    Os indicadores abaixo representam
    fatores acadêmicos, emocionais
    e comportamentais utilizados
    pelo modelo preditivo.
    """
)

st.sidebar.divider()

st.sidebar.subheader(
    "Indicadores Utilizados"
)

st.sidebar.markdown(
    """
    **IEG** → Engajamento escolar

    **IDA** → Desempenho acadêmico

    **IAA** → Autoavaliação

    **IPS** → Aspectos psicossociais

    **IPP** → Aspectos psicopedagógicos

    **IPV** → Ponto de virada
    """
)


# ==============================
# 6. ABAS
# ==============================

aba_simulador, aba_analise = st.tabs(
    [
        "Simulador Interativo",
        "📊 Análise Profunda dos Dados"
    ]
)


# ==============================
# 7. ABA SIMULADOR
# ==============================

with aba_simulador:

    with st.form("simulador_form"):

        st.subheader(
            "Simular Risco do Aluno"
        )

        nome = st.text_input(
            "Nome do Aluno",
            placeholder="Ex: Aluno Teste"
        )

        escola = st.radio(
            "Tipo de Instituição",
            [
                "Pública",
                "Particular"
            ],
            horizontal=True
        )

        c1, c2 = st.columns(2)

        with c1:

            ieg = st.number_input(
                "Nota IEG (Engajamento)",
                min_value=0.0,
                max_value=10.0,
                value=5.0
            )

            ida = st.number_input(
                "Nota IDA (Desempenho)",
                min_value=0.0,
                max_value=10.0,
                value=5.0
            )

            ipp = st.number_input(
                "Nota IPP (Psicopedagógico)",
                min_value=0.0,
                max_value=10.0,
                value=5.0
            )

        with c2:

            iaa = st.number_input(
                "Nota IAA (Autoavaliação)",
                min_value=0.0,
                max_value=10.0,
                value=5.0
            )

            ips = st.number_input(
                "Nota IPS (Psicossocial)",
                min_value=0.0,
                max_value=10.0,
                value=5.0
            )

            ipv = st.number_input(
                "Nota IPV (Ponto de Virada)",
                min_value=0.0,
                max_value=10.0,
                value=5.0
            )


        # ==============================
        # 8. ORGANIZAÇÃO DOS DADOS
        # ==============================

        entrada = pd.DataFrame(
            [[
                ida,
                ieg,
                iaa,
                ips,
                ipp,
                ipv
            ]],

            columns=[
                'IDA',
                'IEG',
                'IAA',
                'IPS',
                'IPP',
                'IPV'
            ]
        )


        # ==============================
        # 9. BOTÃO DE PREVISÃO
        # ==============================

        analisar = st.form_submit_button(
            "Analisar Risco",
            use_container_width=True
        )


        # ==============================
        # 10. PREVISÃO
        # ==============================

        if analisar:

            prob = modelo.predict_proba(
                entrada
            )[:,1][0]

            prob = round(
                prob * 100,
                1
            )

            st.markdown("---")

            st.subheader(
                "Resultado da Análise"
            )

            if prob >= 70:

                st.error(
                    f"⚠️ **{nome or 'O aluno'}** possui **{prob}%** de risco de defasagem."
                )

            elif prob >= 40:

                st.warning(
                    f"⚠️ **{nome or 'O aluno'}** possui **{prob}%** de risco de defasagem."
                )

            else:

                st.success(
                    f"✅ **{nome or 'O aluno'}** possui **{prob}%** de risco de defasagem."
                )

            st.info(
                """
                O resultado apresentado representa
                uma probabilidade estimada pelo modelo
                preditivo com base nos indicadores
                informados.
                """
            )


# ==============================
# 11. ABA DE ANÁLISE
# ==============================

with aba_analise:

    st.subheader(
        "O que realmente influencia a Defasagem?"
    )

    st.markdown(
        """
        A análise abaixo mostra os fatores
        que mais influenciam o risco de
        defasagem educacional identificado
        pelo modelo preditivo.
        """
    )

    dados_importancia = pd.DataFrame({

        'Indicador': [
            'IPV',
            'IEG',
            'IPS',
            'IDA',
            'IPP',
            'IAA'
        ],

        'Importância': [
            0.25,
            0.23,
            0.16,
            0.14,
            0.11,
            0.11
        ]
    })

    st.bar_chart(
        dados_importancia.set_index(
            'Indicador'
        )
    )

    st.info(
        """
        Os indicadores relacionados ao ponto
        de virada (IPV), engajamento (IEG)
        e fatores psicossociais (IPS)
        apresentaram maior influência
        na identificação de alunos em
        risco de defasagem.
        """
    )


# ==============================
# 12. INSIGHT FINAL
# ==============================

st.divider()

st.info(
    """
    O modelo foi desenvolvido utilizando
    indicadores educacionais da ONG
    Passos Mágicos com o objetivo de
    apoiar análises preventivas e
    intervenções antecipadas em alunos
    com possível risco de defasagem.
    """
)