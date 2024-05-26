import openpyxl
import pyperclip
import pyautogui
from time import sleep
##https://cadastro-produtos-devaprender.netlify.app/conclusao.html

#Entrar na planilha 
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']
#Copiar as informações e colar em seus respectivos campos
for linha in sheet_produtos.iter_rows(min_row=2):

    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(1104,330, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.click(1111,422, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.click(1107,549, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(1117,638, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(1137,727, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(1103,812, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    
    #próximo
    pyautogui.click(1119,865,duration=1)
    sleep(3)
#--------------------------------------
    preco = linha[6].value
    pyperclip.copy(preco)
    pyautogui.click(1154,372, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    

    qtde_estoque = linha[7].value
    pyperclip.copy(qtde_estoque)
    pyautogui.click(1146,456, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    
    data_validade = linha[8].value
    pyperclip.copy(data_validade)
    pyautogui.click(1153,538, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.click(1126,629, duration=1)
    pyautogui.hotkey('ctrl', 'v')
#--------------------------------------
    tamanho = linha[10].value
    pyautogui.click(1114,714,duration=1)
    if tamanho == 'Pequeno':
        pyautogui.click(1147,49,duration=1)
    elif tamanho == 'Médio':
        pyautogui.click(1118,771,duration=1)
    else:
        pyautogui.click(1122,782,duration=1)

    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.click(1112,804, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #próximo
    pyautogui.click(1141,867,duration=1)
#--------------------------------------
    fabricante = linha[12].value
    pyperclip.copy(fabricante)
    pyautogui.click(1104,388, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pais_de_origem = linha[13].value
    pyperclip.copy(pais_de_origem)
    pyautogui.click(1112,474, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    observacoes = linha[14].value
    pyperclip.copy(observacoes)
    pyautogui.click(1108,564, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    codigo_barras = linha[15].value
    pyperclip.copy(codigo_barras)
    pyautogui.click(1102,697, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    localizacao = linha[16].value
    pyperclip.copy(localizacao)
    pyautogui.click(1104,785, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #próximo
    pyautogui.click(1118,837,duration=1)

    #confirmar confirmação inclusão
    pyautogui.click(1608,189,duration=1)

    #confirmar confirmação inclusão 2
    pyautogui.click(1612,187,duration=1)

    #novo cadastro
    pyautogui.click(1448,603,duration=1)

#Repetir o processo 
#Cadastrar todos os elementos


