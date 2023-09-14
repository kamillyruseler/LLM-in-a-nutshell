# 🥜 LLM-in-a-nutshell 🥜
Implementação de uma integração de GPT, usando Streamlit, LangChain, LLM e padrões de projeto em Python

## Motivação
No cenário brasileiro atual, a maior parte da população não possui quaisquer investimentos. Mas, num geral, quem investe, investe em produtos de Renda Fixa (principalmente na poupança). A ideia dessa aplicação é servir como um instrutor para aplicações em Renda Fixa, para além da poupança. Com ela, os brasileiros conseguirão ter fácil acesso à informação e a possibilidade de tirar suas dúvidas com Machine Learning!
Fonte: https://www.infomoney.com.br/minhas-financas/poupanca-ainda-e-a-principal-aplicacao-dos-brasileiros-veja-grafico/

### Material do Ebook
Alimentamos essa aplicação com as 170 páginas do "Guia Definitivo para Investir em Renda Fixa: O Simples que Funciona", de 2021, escrito pela  Mariana Delgado. Disponível aqui: https://elivros.love/livro/baixar-livro-guia-definitivo-para-investir-em-renda-fixa-mariana-delgado-em-epub-pdf-mobi-ou-ler-online. 

## Deploy na Streamlit
Acesse o link: https://llm-in-a-nutshell.streamlit.app/
![image](https://github.com/kamillyruseler/LLM-in-a-nutshell/assets/107367118/2887a49f-1717-4bc2-96f5-aee1529c8e00)

## Rodando localmente
Para rodar localmente, faça o git clone do repositório e insira o comando "make all" para baixar os requisitos, fazer o linting (com isort, flake8 e black), rodar os tester unitários e abrir o Streamlit no seu localhost. 

### Segurança
Importante: no main.py, coloque a sua chave da OpenAI para rodar localmente.
No Streamlit, usei o Secrets Management para armazenar a chave. Você pode ver um tutorial aqui: https://blog.streamlit.io/8-tips-for-securely-using-api-keys/
