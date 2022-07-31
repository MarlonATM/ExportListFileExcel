from tkinter import *
import os
import pandas as pd

#tkinter definitions
root = Tk()
root.title('VN2R App') #Title of application. Showed in the header.
root.iconbitmap('C:\icone.ico') #Icon of the application. Showed in the header.
root.geometry('600x200') #Height and width of the window

res = [] #Defining a variable to be a list

#function that runs when clicked in the button
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

#First text that appears in the app
diretorio = Label(root, text='Especifique o diretório raiz:')
diretorio.pack()

#First textbox that appears in the app. Input for the path of folder.
txtDiretorio = Entry(root, width=80)
txtDiretorio.pack()

#Second text that appears in the app
ext = Label(root, text='Especifique a extensão pretendida (Ex: .dwg):')
ext.pack()

#Second textbox that appears in the app. Input for the path of folder.
txtExt = Entry(root, width=20)
txtExt.pack()

#Create button
enviar = Button(root, text='Enviar', command=code)
enviar.pack()

root.mainloop()
