#Importação da Biblioteca

import pyautogui as auto #Para apelidar a biblioteca para um nome mais curto utilizar 'as'.
import time

#Tempo que cada comando demora para executar
auto.PAUSE = 1

#Instruções para abrir o VsCode

auto.press('win') #O comando 'win' é abreviação do menu iniciar na biblioteca pyautogui

#Abrir o VsCode

auto.write('vscode')
auto.press('enter')

#Espera 10 segundos para abrir o vscode e continuar com os comandos

time.sleep(10)

#Criando o repositório local

auto.hotkey('ctrl', 'shift', "'")

auto.write('git init')
auto.press('enter')

auto.write('git add .')
auto.press('enter')

auto.write('git commit -m "Versão Atualizada por automação"')
auto.press('enter')

auto.write('git branch -M main')
auto.press('enter')

auto.write('git remote add origin https://github.com/guilhermealvesd/automacao_repositorio.git')
auto.press('enter')

auto.write('git push -u origin main')
auto.press('enter')