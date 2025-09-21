import random
import string
import streamlit as st

def gerarSenha(tamanho, usarMaiuscula, usarMinuscula, usarNumeros, usarSimbolos, palavra="") -> str:
    caracters = ""
    if usarMaiuscula: caracters += string.ascii_uppercase # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if usarMinuscula: caracters += string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    if usarNumeros: caracters += string.digits # '0123456789'
    if usarSimbolos: caracters += string.punctuation # r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    if not caracters:
        return "Escolha pelo menos alguma das opções!"
    
    if palavra:
        if len(palavra) >= tamanho: 
            return "A palavra é maior ou igual o tamanho da senha"

        senhaGerada = "".join(random.choice(caracters) for i in range (tamanho-len(palavra)))    

        posicao = random.randint(0, len(senhaGerada))

        senha = senhaGerada[:posicao] + palavra + senhaGerada[posicao:]
        return senha
    else:
        return "".join(random.choice(caracters) for i in range(tamanho))

st.title("Gerador de Senhas")
st.subheader("Opções da senha:")

tam = st.number_input("Tamanho da senha:", min_value=4, max_value=50, value=8)
    
usar_maiusculas = st.checkbox("Letras maiúsculas (A-Z)", value=True) 
usar_minusculas = st.checkbox("Letras minúsculas (a-z)", value=True)
usar_numeros = st.checkbox("Números (0-9)", value=True)
usar_simbolos = st.checkbox("Caracteres especiais (!@#$...)", value=True)
    
ativarPalavra = st.checkbox("Deseja incluir alguma palavra na senha?")

palavra_usuario = st.text_input("Digite a palavra que quer incluir na senha:", disabled=not ativarPalavra)

if st.button("Gerar Senha"):
    senha = gerarSenha(tam, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos, palavra_usuario if ativarPalavra else "")
    st.success(f"Sua senha gerada: `{senha}`")
