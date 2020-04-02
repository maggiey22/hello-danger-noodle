import pyperclip

def removeArrows():
    text = str(pyperclip.paste())
    lines = text.split('\n')
    result = []
    for l in lines:
        if ">>> " in l:
            result.append(l.replace(">>> ", ""))
    result = '\n'.join(result)
    pyperclip.copy(result)

def commentOut():
    text = str(pyperclip.paste())
    lines = text.split('\n')
    result = []
    for l in lines:
        result.append("#" + l)
    result = '\n'.join(result)
    pyperclip.copy(result)

def echoHTML():
    text = str(pyperclip.paste())
    lines = text.split('\n')
    result = []
    for l in lines:
        result.append("echo \'" + l + "';")
    result = '\n'.join(result)
    pyperclip.copy(result)
