from pathlib import Path
import os
from directory_management import Directory
# O PROGRAMA ESTÁ ENVIANDO DADOS BRUTOS DE PARÂMENTROS, O QUE É NÃO CONVENCIONAL
def changeDir(arg: tuple[str] = None):
    if arg[0] == None:
        print(PATHDIR)
    elif arg[0] == "..":
        PATHDIR.back()
    else:
        __dir = str(PATHDIR) + "/" + arg[0]
        if os.path.isdir(__dir):
            PATHDIR.add(arg[0])
        else:
            print(f"{__dir} é um diretório inválido.\n")
def showSubDirs():
    print()
    for subd in os.listdir(str(PATHDIR)):
        print("|", subd)
    print()
def revert(index: tuple[int] = None):
    def exec_history(index: int):
        if len(cmd_history[index]) > 1:
            print("->", *cmd_history[index])
            execute(*cmd_history[index]) # É preciso desempacotar porque o histórico armazena tupla quando há parâmetros
        else:
            print(f"-> ", *cmd_history[index])
            execute(*cmd_history[index])
    cmd_history.pop() # Deletei o último porque, para entrar na função, é preciso adicionar "!!" no histórico, então apaguei
    try:
        if index == None:
            exec_history(-1)
        else:
            exec_history(int(index[0]))
    except IndexError:
        print("o histórico solicitado não está armazenado.\n")
def showHistory():
    print("_"*30)
    for i in range(len(cmd_history)):
        print(i,"->", cmd_history[i][0], "(", end="")
        for j in range(1,len(cmd_history[i])):
            print(f"'{cmd_history[i][j]}'", end=", ")
        print(")")
    print("-"*30)
def execute(*functools: str):
    if catch_typing_errors(functools[0], len(functools) - 1):
        if len(functools) == 1:
            paramters[functools[0]][0]()
        else:
            paramters[functools[0]][0](functools[1:])
def catch_typing_errors(command: str, qtparams: int):
    if command not in paramters.keys():
        print(f"'{command}' não é reconhecido como comando interno ou externo,\nprograma operável ou arquivo batch.\n")
        return False
    elif qtparams != paramters[command][1]:
        qt_func_params = paramters[command][1]
        print(f"'{command}' deve haver {qt_func_params} parâmetros.\n")
        return False
    else:
        return True
paramters = {"dir": (showSubDirs, 0),
             "cd": (changeDir, 1),
             "!!": (revert, 0),
             "!": (revert, 1),
             "exit": (exit, 0),
             "showh": (showHistory, 0),
             }
PATHDIR = Directory(Path(__file__).parent)
cmd_history = []
while True:
    entrada = input(f"{PATHDIR}>").strip().split(" ")
    cmd_history.append(tuple(entrada))
    if catch_typing_errors(entrada[0], len(entrada) - 1):
        execute(*entrada)