from tkinter import *
import os
import pandas as pd

root = Tk()
root.title('VN2R App')
root.iconbitmap('Y:/00-MARLON MATOS/icone.ico')
root.geometry('600x200')

# list to store the path and name of files
res = []
def code():
    for root, dirs, files in os.walk(txtDiretorio.get()):
        for file in files:
            if file.endswith(txtExt.get()):
                res.append(os.path.join(root, file))
    caminho, ficheiro = zip(*(s.rsplit('\\', 1) for s in res))
    d = {'Caminho':caminho, 'Ficheiro':ficheiro}
    df = pd.DataFrame(data=d)
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1', index=False)
    writer.save()

diretorio = Label(root, text='Especifique o diretório raiz:')
diretorio.pack()

txtDiretorio = Entry(root, width=80)
txtDiretorio.pack()

ext = Label(root, text='Especifique a extensão pretendida (Ex: .dwg):')
ext.pack()

txtExt = Entry(root, width=20)
txtExt.pack()

enviar = Button(root, text='Enviar', command=code)
enviar.pack()

root.mainloop()
