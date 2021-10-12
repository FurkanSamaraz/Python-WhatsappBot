import smtplib
from selenium import webdriver

#intarnete erişmek için
path = 'C:\\Users\samar\Desktop\WhatsapBott\geckodriver-v0.29.1-win64\geckodriver.exe'

browser = webdriver.Firefox(executable_path=path)

browser.get('https://web.whatsapp.com/')


def mailgonder(mesaj):
    sahip='samaraz4545@gmail.com'
    alici='samaraz545454@gmail.com'
    giris='samaraz4545@gmail.com'
    sifre='samaraz172754'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(giris,sifre)
    server.sendmail(sahip,alici,mesaj)
    server.quit()





kontrol = True
kontrol2 = True

while True:
  try:
    browser.find_element_by_xpath("//span[text()='çevrimiçi']")
    if kontrol==True:
      msg2 = "cevrimici!"
      mailgonder(msg2)
      kontrol=False
  except:
    kontrol=True
    if kontrol2==True:
      msg ="cevrimdisi!"
      mailgonder(msg)
      kontrol2=False