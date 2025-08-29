from pathlib import Path
import os
from directory_management import Directory

# RECURSO DE HISTÓRICO**
    # O PROGRAMA NÃO ESTÁ ARMAZENANDO, NO HISTÓRICO, LINHAS COM MAIS DE 2 PARAMETROS
#A VERIFICAÇÃO DE ERRO DE DIRETORIO NAO ESTA NA FUNCAO CATCH, ASSIM FAZENDO COM QUE FIQUE EM RECURSAO INFINITA,
#JA QUE A EXECUTE PRECISA DE TODOS OS ERRORS PARA QUE O PROGRAMA EXECUTE CORRETAMENTE
def changeDir(arg = None):
    # print("--", changeDir.__name__)
    if arg == None:
        print(PATHDIR)
    elif arg == "..":
        PATHDIR.back()
    else:
        # print(arg)
        __dir = str(PATHDIR) + "/" + arg
        if os.path.isdir(__dir):
            PATHDIR.add(arg)
        else:
            print(f"{__dir} é um diretório inválido.\n")
def showSubDirs():
    for subd in os.listdir(str(PATHDIR)):
        print(subd)
def history(index = None):
    def exec_hist(index: int):
        if isinstance(cmd_history[index], tuple):
            print("->", *cmd_history[index])
            execute(*cmd_history[index]) # É preciso desempacotar porque o histórico armazena tupla quando há parâmetros
        else:
            print(f"-> {cmd_history[index]}\n")
            execute(*cmd_history[index]) 
    cmd_history.pop() # Deletei o último porque, para entrar na função, é preciso adicionar "!!" no histórico, então apaguei
    try:
        if index == None:
            exec_hist(-1)
        else:
            exec_hist(int(index))
    except IndexError:
        print("o histórico solicitado não está armazenado.\n")
def execute(*functools):
    if len(functools) == 1:
        cmd_history.append(functools[0])
        paramters[functools[0]][0]()
    else:
        cmd_history.append(functools)
        paramters[functools[0]][0](functools[1])#:

def catch_typing_errors(command, qtparams):
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
             "!!": (history, 0),
             "!": (history, 1),
             "exit": (exit, 0),
             }
PATHDIR = Directory(Path(__file__).parent)
cmd_history = []
while True:
    entrada = input(f"{PATHDIR}>").strip().split(" ")
    if catch_typing_errors(entrada[0], len(entrada) - 1):
        execute(*entrada)