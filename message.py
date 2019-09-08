import requests,json,_thread,time
from PyQt5.QtWidgets import QApplication,QWidget
from Ui_messageUI import Ui_messageFly
def sendMessage(threadName,phoneNum,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        url_json = 'aHR0cDovL3N2aXAuMjVjbS50b3AvYXBwL2luZGV4LnBocD9pPTImYz1lbnRyeSZkbz1jaGVjayZtPWFnZW50X3NpdGU='
        data = {'phone':phoneNum,'verify':''}
        r_json = requests.post(url_json,data)
        ui.textEdit.append(threadName+"第"+str(count)+"次发送："+str(phoneNum)+str(r_json.text)+"\r\n")
def on_click(self):
    phoneValue =  int(ui.lineEdit.text())
    threadNum = int(ui.comboBox.currentText())
    for i in range(threadNum):
        print(i)
        _thread.start_new_thread(sendMessage,("线程_"+str(i),phoneValue,1))
if __name__ == "__main__":
    app = QApplication([])
    window= QWidget()
    ui=Ui_messageFly()
    ui.setupUi(window)
    ui.pushButtonStart.clicked.connect(on_click)
    window.show()
    app.exec()
