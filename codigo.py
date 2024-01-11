'''
projeto de automaão de tarefas para quaisquer sistemas, sendo preciso apenas poucas alteraçôes para casos específicos
'''
import pyautogui
import time
import pandas as pd

# acessar o site
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('google chrome')
pyautogui.press('enter')
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')


time.sleep(5)

#fazer login
pyautogui.click(x=623, y=469) #a posição pode ser diferente dependendo do monitor
pyautogui.write('email@gmail.com')
pyautogui.press('tab')
pyautogui.write('minhasenha')
pyautogui.press('tab')
pyautogui.press('enter')

tabela = pd.read_csv('produtos.csv') #utilização da tabela que esta sendo lida pela biblioteca do pandas
for linha in tabela.index:
    pyautogui.click(x=598, y=323) #clica no primeiro campo da tabela
    pyautogui.write(str(tabela.loc[linha, "codigo"])) #localiza o codigo na base de dados e escreve no sistema
    pyautogui.press("tab") #vai para o próximo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]): #essa condicional é para verficar se no campo 'obs' é preciso escrever algo.
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000) #rola a tela para cima para repetir o processo.  Logitech    Mouse   1   25.95