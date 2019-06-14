#execute_word.py

#imports
from log import Log
from datetime import datetime
from pywinauto.application import Application


Log.open()

#Here starting the automation
Log.print('>>>The execution STARTS HERE!\n\n')
dateExecution = datetime.now().strftime('%Y%m%d_%H%M%S')

app = Application(backend='uia')
app.start('C:\Program Files\Microsoft Office\Office15\WINWORD.exe')
word = app.Dialog

#Creating a blank document
word.child_window(title="Documento em branco", auto_id="AIOStartDocument", control_type="Hyperlink").type_keys('{ENTER}')

#Typing and personalizing the document
word.type_keys('Estou{SPACE}')
word.child_window(title="Sublinhado", control_type="Button").click()
word.child_window(title="Página 1", auto_id="UIA_AutomationId_Word_Page_1", control_type="Custom").type_keys('testando')
word.child_window(title="Sublinhado", control_type="Button").click()
word.child_window(title="Página 1", auto_id="UIA_AutomationId_Word_Page_1", control_type="Custom").type_keys('{SPACE}o{SPACE}Word.')

#Saving the document
word.child_window(title="Salvar", control_type="Button").click()
word.child_window(title="Área de Trabalho", control_type="Button").click()

#Encontrando a janela Salvar Como
#word.child_window(title="Nome do arquivo:", auto_id="1001", control_type="Edit").set_text(dateExecution)
word.child_window(title="Salvar", auto_id="1", control_type="Button").click()

#word.close()
Log.print('>>>The execution FINISHES HERE!\n\n')

Log.close()
exit()  
    
