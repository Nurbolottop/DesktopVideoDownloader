from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUi
from pytube import YouTube
import sys

class Form(QMainWindow):


    def __init__(self):
            super(Form, self).__init__()

            loadUi('ytdown.ui', self)

            self.audio.clicked.connect(self.audio_self)
            self.video.clicked.connect(self.video_self)


    def download(url, type):
        yt = YouTube(url)
        if type == "audio":
            yt.streams.filter(only_audio=True).first().download("audio", f"{yt.title}.mp3")
            return f"{yt.title}.mp3"
        elif type == "video":
            yt.streams.filter(progressive=True, file_extension="mp4").first().download("video", f"{yt.title}.mp4")
            return f"{yt.title}.mp4"

    def audio_self(self):
        try:
            url = str(self.input1.text())
            yt = YouTube(url)
            yt.streams.filter(only_audio=True).first().download("audio", f"{yt.title}.mp3")
            
            self.eror.setText("Все установилось! ")

            self.downloader.setValue(100)

            

        except:
            self.eror.setText("Произошла ошибка, повторите заного !!!")    

    def video_self(self):
        try:
            url = str(self.input1.text())

            yt = YouTube(url)
            yt.streams.filter(progressive=True, file_extension="mp4").first().download("video", f"{yt.title}.mp4")
            
            self.eror.setText("Все установилось! ")

            self.downloader.setValue(100)

            

        except:
            self.eror.setText("Произошла ошибка, повторите заного !!!")   






app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()