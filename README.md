# Predição de Risco de Defasagem Educacional

Projeto desenvolvido para o **Datathon — ONG Passos Mágicos**, com o objetivo de identificar alunos com risco de defasagem educacional por meio de análise de dados e Machine Learning.

---

## Objetivo

Desenvolver um modelo preditivo capaz de identificar alunos em risco de defasagem educacional utilizando indicadores acadêmicos, psicossociais e de engajamento.

A solução busca apoiar ações preventivas e auxiliar na tomada de decisão pedagógica.

---

## Base de Dados

Foram utilizadas as bases **PEDE** da ONG Passos Mágicos dos anos:

* 2022
* 2023
* 2024

As bases foram unificadas em uma única estrutura analítica.

### Indicadores utilizados

* **IDA** → Desempenho acadêmico
* **IEG** → Engajamento escolar
* **IAA** → Autoavaliação
* **IPS** → Aspectos psicossociais
* **IPP** → Aspectos psicopedagógicos
* **IPV** → Ponto de virada
* **IAN** → Adequação de nível

---

## Tratamento dos Dados

Etapas realizadas:

✔ Padronização das colunas  
✔ Conversão de dados numéricos  
✔ Tratamento de valores nulos  
✔ Criação da variável alvo  
✔ Separação treino e teste  

---

## Modelo de Machine Learning

Modelo utilizado:

**Gradient Boosting Classifier**

Configuração:

* Treino: 80%
* Teste: 20%
* Random State: 42

### Resultados obtidos

| Métrica        | Resultado |
| -------------- | --------: |
| Acurácia       |     61,9% |
| Precisão média |       62% |
| Recall médio   |       61% |
| F1-score médio |       61% |

---

## Aplicação Desenvolvida

Foi desenvolvida uma aplicação em Streamlit para simulação do risco de defasagem educacional.

🔗 Streamlit:

https://datathon-paapps-magicos-e8jrkkeezug7knrcreizvj.streamlit.app/

---

## 📁 Estrutura do Projeto

```bash
datathon-passos-magicos
│
├── app.py
├── modelo_defasagem.pkl
├── requirements.txt
├── tech_challenge_passos_magicos.ipynb
├── Storytelling — ONG Passos Mágicos.pdf
├── BASE DE DADOS PEDE 2024 - DATATHON.xlsx
├── Video.mp4  
└── README.md
```

---

## Integrantes

* Emmilly Katriny
* Matheus Rodrigues

---

## 🔗 Links

**Aplicação Streamlit:**
https://datathon-paapps-magicos-e8jrkkeezug7knrcreizvj.streamlit.app/

**Vídeo da apresentação:**
https://github.com/EmmillyKatriny/datathon-passos-magicos/blob/main/video.mp4  

---
