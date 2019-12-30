import pyautogui
from datetime import date
pyautogui.PAUSE = .5

#Constants
date = date.today()
pdfName = 'WU_Receipt' + date.strftime('%m/%d/%Y')

pyautogui.hotkey('command','space')
pyautogui.typewrite('chrome')
pyautogui.hotkey('enter')
pyautogui.hotkey('ctrl','command','f')
pyautogui.hotkey('command','t')
pyautogui.hotkey('command','l')
pyautogui.typewrite('https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2Foauth%2Fauthorize%3Fclient_id%3Dmy-account-web%26prompt%3Dlogin%26redirect_uri%3Dhttps%253A%252F%252Fpayments.xfinity.com%252Foauth%252Fcallback%26response_type%3Dcode%26state%3Dhttps%253A%252F%252Fpayments.xfinity.com%252Fnew%26response%3D1&forceAuthn=1&client_id=my-account-web&reqId=915ca993-0a04-479f-87f3-fe04da1af7ae')
pyautogui.hotkey('enter')
pyautogui.moveTo(935,311)
pyautogui.click()
pyautogui.typewrite('isalago1@comcast.net')
pyautogui.moveTo(941,361)
pyautogui.click()
pyautogui.typewrite('Santarem@1963')
pyautogui.moveTo(236,456)
pyautogui.click()
pyautogui.hotkey('return')

#pyautogui.hotkey('enter')
#pyautogui.typewrite(pdfName)
