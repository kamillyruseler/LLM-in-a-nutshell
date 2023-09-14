import os

import streamlit as st
from langchain.agents.agent_toolkits import (
    VectorStoreInfo,
    VectorStoreToolkit,
    create_vectorstore_agent,
)
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI(temperature=0.1, verbose=True)
embeddings = OpenAIEmbeddings()

loader = PyPDFLoader("guia_renda_fixa.pdf")
pages = loader.load_and_split()
store = Chroma.from_documents(pages, embeddings, collection_name="guia_renda_fixa.pdf")

vectorstore_info = VectorStoreInfo(
    name="guia_renda_fixa",
    description="o guia definitivo para investir em renda fixa",
    vectorstore=store,
)
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

agent_executor = create_vectorstore_agent(llm=llm, toolkit=toolkit, verbose=True)


# Roda a função do LLM com base no input do usuário
def prompt_executor(prompt):
    response = agent_executor.run(prompt)
    return response


def main():
    # Front-end
    st.title("Investindo em renda fixa com a LLM 📈💡")
    prompt = st.text_input("Faça sua pergunta aqui")
    col1, col2, col3, col4 = st.columns(4)

    if col1.button("O que é renda fixa?"):
        prompt = "O que é renda fixa?"
    if col2.button("Quando não investir em renda fixa?"):
        prompt = "Quando não investir em renda fixa?"
    if col3.button("Qual a rentabilidade da CDB?"):
        prompt = "Qual a rentabilidade da CDB?"
    if col4.button("Endividados também podem investir?"):
        prompt = "Endividados também podem investir?"

    # Conectando o input com a função do prompt
    resposta = None
    if prompt:
        resposta = prompt_executor(prompt)

    resposta_placeholder = st.empty()

    # Exibir a resposta com o estilo desejado
    if resposta:
        with resposta_placeholder:
            st.markdown(
                f'<div style="background-color: #1e426d; padding: 10px; border-radius: 5px;"><span style="color: white;">{resposta}</span></div>',
                unsafe_allow_html=True,
            )

        with st.expander("O que achamos no ebook:"):
            search = store.similarity_search_with_score(prompt)
            st.write(search[0][0].page_content)


if __name__ == "__main__":
    main()
