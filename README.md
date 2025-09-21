# Gerador de Senhas

![Interface do Gerador de Senhas](print.png)

## Sobre o Projeto

Este é um Gerador de Senhas simples e prático, desenvolvido em Python com a biblioteca Streamlit. Ele foi criado como forma de praticar um pouco da linguagem Python e também como integrar com a interface web. A aplicação permite que você gere senhas seguras e aleatórias.

## Funcionalidades

  * **Tamanho personalizável**: Defina o tamanho da sua senha, de 4 a 50 caracteres.
  * **Controle de caracteres**: Escolha exatamente o que incluir na sua senha:
      * **Letras maiúsculas** (`A-Z`)
      * **Letras minúsculas** (`a-z`)
      * **Números** (`0-9`)
      * **Caracteres especiais** (`!@#$...`)
  * **Inclusão de palavra-chave**: Quer uma senha forte que seja fácil de lembrar? Você pode adicionar uma palavra de sua escolha para ser inserida aleatoriamente na senha gerada.

## Como Usar

Você pode acessar a aplicação diretamente pelo link de deploy:

**[Gerador de Senhas - Streamlit](https://gerador-de-senhas-basico-jwpkjrz2zwetfefgra866t.streamlit.app/)**

Se você preferir rodar o projeto localmente, siga estes passos:

1.  **Clone o repositório** para a sua máquina:
    ```bash
    git clone https://github.com/Luisjackson/gerador-de-senhas-basico.git
    cd gerador-de-senhas-basico
    ```
2.  **Instale as dependências** do projeto:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute a aplicação**:
    ```bash
    streamlit run app.py
    ```

A aplicação será aberta automaticamente no seu navegador, geralmente em `http://localhost:8501`.
