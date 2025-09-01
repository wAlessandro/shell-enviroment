from pathlib import Path
import os
from directory_management import Directory
#HELP
def _help():
    print("""
CD          Altera o caminho atual de gerenciamento.
!!          Executa o último comando digitado.
!           Executa o comando indexado, a partir do histórico.
EXIT        Fecha o terminal. 
SHOWH       Imprime os comandos do histórico. 
START       Executa um programa do diretório atual.
CLS         Limpa o terminal.
COLOR       Altera a cor do terminal.
""")
def changeColor(color: tuple):
    colors = {
              "blue": 1,
              "green": 2,
              "aqua": 3,
              "red": 4,
              "purple": 5,
              "yellow": 6,
              "white": 7}
    if color[0] not in colors.keys():
        print("Parâmetro inválido.\n")
        print("|Cores disponíveis")
        for key in colors.keys():
            print("-", key.upper())
        return
    os.system(f"COLOR {colors[color[0]]}")
def clearTerminal():
    os.system("cls")
def showSubDirs():
    print()
    for subd in os.listdir(PATHDIR.get):
        print("|", subd)
    print()
def showHistory():
    print("_"*30)
    for i in range(len(cmd_history)):
        print(i,"->", cmd_history[i][0], "(", end="")
        for j in range(1,len(cmd_history[i])):
            print(f"'{cmd_history[i][j]}'", end=", ")
        print(")")
    print("-"*30)    
def changeDir(arg: tuple[str] = None):
    if arg[0] == "..":
        PATHDIR.back()
    elif arg[0].count(".") > 2:
        return
    else:
        __dir = PATHDIR.get / arg[0]
        if os.path.isdir(__dir):
            PATHDIR.add(arg[0])
        else:
            print(f"{__dir} é um diretório inválido.\n")
def revert(index: tuple[str] = None):
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
def startProgram(program_name: tuple):
    file_path = PATHDIR.get / program_name[0]
    if os.system(f"start {file_path} 2>nul") != 0:
        print(f"O sistema não pôde encontrar o arquivo {file_path}\n")

def catchTypingErrors(command: str, qtparams: int) -> bool:
    if command not in paramters.keys():
        print(f"'{command}' não é reconhecido como comando interno ou externo,\nprograma operável ou arquivo batch.\n")
        return False
    elif qtparams != paramters[command][1]:
        qt_func_params = paramters[command][1]
        print(f"'{command}' deve haver {qt_func_params} parâmetro(s).\n")
        return False
    else:
        return True
def execute(*functools: str):
    if catchTypingErrors(functools[0], len(functools) - 1):
        if len(functools) == 1:
            paramters[functools[0]][0]()
        else:
            paramters[functools[0]][0](functools[1:])
paramters: dict[str, tuple] = {
            "dir": (showSubDirs, 0),
             "cd": (changeDir, 1),
             "!!": (revert, 0),
             "!": (revert, 1),
             "exit": (exit, 0),
             "showh": (showHistory, 0),
             "start": (startProgram, 1),
             "cls": (clearTerminal, 0),
             "color": (changeColor, 1),
             "help": (_help, 0),
             }
PATHDIR: Directory = Directory(Path(__file__).parent)
cmd_history: list = []
while True:
    entrada: str = input(f"{PATHDIR.get}>").lower().strip().split(" ")
    cmd_history.append(tuple(entrada))
    execute(*entrada)