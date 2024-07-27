# Acessar o site de login do sistema
    #Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Fazer login
# Importar/Pegar a base de dados
# Cadastrar um produto
# Repetir os passos 4 e 5 para todos os produtos da base de dados até o fim.

# área de importação de bibliotecas
import pyautogui
import time
import pandas as pd

# vamos usar as funções de click, press e write
# pyautogui.click
# pyautogui.write
# pyautogui.press
# pyautogui.hotkey - combinação de teclas
# pyautogui.scroll - rolar a tela

# definir o tempo de espera entre os comandos
pyautogui.PAUSE = 0.5 
# 0.5 segundos

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")



pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# inserir uma pausa de 3 segundos pra carregar a página
time.sleep(3)

# login
pyautogui.click(x=893, y=406)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("email@email.com")

#senha
pyautogui.press("tab")
pyautogui.write("senha")

# clicar no botão de login
pyautogui.click(x=802, y=571)

# inserir uma pausa de 3 segundos pra carregar a página
time.sleep(3)

# importar a base de dados
productTable = pd.read_csv("produtos.csv")

# print(productTable)
# cada produto tem código, marca, tipo, categoria, preco_unitario, custo e obs

# cadastrar um produto
for line in productTable.index:

    # clicar no no primeiro campo digitável
    pyautogui.click(x=653, y=294)

    # copiar o valor da tabela
    codigo = productTable.loc[line, "codigo"]

    # preencher o campo selecionado digitável
    pyautogui.write(str(codigo))

    # pra ir pro próximo campo
    pyautogui.press("tab")
    pyautogui.write(str(productTable.loc[line, "marca"]))

    pyautogui.press("tab")
    pyautogui.write(str(productTable.loc[line, "tipo"]))

    pyautogui.press("tab")
    pyautogui.write(str(productTable.loc[line, "categoria"]))

    pyautogui.press("tab")
    pyautogui.write(str(productTable.loc[line, "preco_unitario"]))

    pyautogui.press("tab")
    pyautogui.write(str(productTable.loc[line, "custo"]))

    pyautogui.press("tab")
    obs = productTable.loc[line, "obs"]

    # como obs é opcional, vamos verificar se tem algo escrito
    if pd.isna(obs) == False:
        pyautogui.write(str(productTable.loc[line, "obs"]))

    # agora vai pro botão de salvar/enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    # rola a tela até o topo da página
    pyautogui.scroll(5000)
    