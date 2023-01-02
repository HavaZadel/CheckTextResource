import re
import numpy as np
import pandas as pd 
import PySimpleGUI as sg

sg.theme('Light Blue 2')

layout = [[sg.Text('Enter 1 files to check')],
          [sg.Text('File 1', size=(8, 1)), sg.Input(key='Input_1'), sg.FileBrowse()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Shaker', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Cancel"):
        break
    elif event == 'Submit':
        excel_without_error = True
        excel_file = values['Input_1']
        data_frame = pd.read_excel(excel_file)
        excel_matrix= pd.DataFrame(data_frame)
        original_english_translation = str(excel_matrix.iloc[1,4])
        original_tag_variable = re.findall("({.*?}|<.*?>)", original_english_translation)
        if len(original_tag_variable) > 0:
            for i in range(5,36):
                foreign_translation = str(excel_matrix.iloc[1,i])
                foreign_tag_variable = re.findall("({.*?}|<.*?>)", foreign_translation) or []
                if not np.array(np.array(foreign_tag_variable) == np.array(original_tag_variable)).all():
                    sg.Print(str(excel_matrix.iloc[0,i]))
                    sg.Print(foreign_tag_variable,"\n")
                    excel_without_error = False
        if excel_without_error:
            sg.Print("The translation is okay ! (really ?)")
window.close()
