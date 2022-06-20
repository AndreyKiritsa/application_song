class mainWindow(object):#создание главного окна
    def __init__(self, root ):
        root.title('Application')
        #root.geometry()
        root.resizable(FALSE, FALSE)
        self.menuBar = Menu(root)#создание области главного меню
        self.firstMenu()#выбор нужного файла
        self.FunctionApplication()
        root['menu'] = self.menuBar

        self.content = Frame(root)#создание фрейма 0
        self.text = Text(self.content, width=45)#область вывода информации
        self.text.grid(column=0,row=0)

        self.content1 = Frame(root) #создание кнопок и функионала

        self.textLabel()# окно виджета Label
        self.getButton()# окно виджета Button

        self.content1.grid(column=1, row=0, sticky='nsew')# вывод Frame в основное окно
        self.content.grid(column = 0, row=0)

    def getButton(self):
        self.button1 = Button(self.content1, width=10, text='STFT', command = self.stft_class)
        self.button1.grid(column=0, row=1, pady=5, padx = 5)

        self.button1 = Button(self.content1, width = 10, text = 'Song', command = self.song) #функция вывода огибающей входного сигнала
        self.button1.grid(column = 1, row = 1, pady=5, padx = 5)

        self.button1 = Button(self.content1, width = 10, text = 'HPSS', command = self.metHPSS) #функция вычисления гармонической и ударной составляющей
        self.button1.grid(column = 0, row = 3, pady=5, padx = 5)

        self.button1 = Button(self.content1, width = 10, text = 'Beat and Temp', command = self.BeatTemp)
        self.button1.grid(column = 1, row = 3, pady = 5, padx = 5)

        self.button1 = Button(self.content1, width = 10, text = 'Onset', command = self.onsetMethod)
        self.button1.grid(column = 0, row = 4, pady = 5, padx = 5)

    def textLabel(self):
        self.label = Label(self.content1, width = 20, text = 'Основные функции')  # окно информирование
        self.label.grid(column = 0, row = 0)

    def firstMenu(self):#отображения пункта меню "Open File"
        self.file_open = Menu(self.menuBar)
        self.menuBar.add_cascade(menu=self.file_open, label = 'File')
        self.file_open.add_command(label = 'Open File', command = self.openFile)

    def FunctionApplication(self) :
        self.OpenFunction = Menu(self.menuBar)
        self.menuBar.add_cascade(menu = self.OpenFunction, label = 'Function')
        self.OpenFunction.add_command(label = 'Harmonic', command = self.FunctionHarmonic)
        self.OpenFunction.add_command(label = 'Percusive', command = self.FunctionPercusive)
        self.OpenFunction.add_command(label = 'STFT', command = self.FunctionSTFT)
        self.OpenFunction.add_command(label = 'Song', command = self.FunctionGraphs)
        self.OpenFunction.add_command(label = 'Beat', command = self.FunctionBeat)
        self.OpenFunction.add_command(label = 'Temp', command = self.FunctionTempo)
        self.OpenFunction.add_command(label = 'Огибающая', command = self.FunctionOnsetStandart)
        self.OpenFunction.add_command(label = 'Огибающая медианная', command = self.FunctionOnsetMedian)
        return

    def FunctionHarmonic(self):
        frequency = 22050
        try:
            harmonicChoise(frequency, self.y)
        except:
            self.printText("Ошибка выполнения функции, возможно, вы не выбрали файл")
        return

    def FunctionPercusive(self):
        frequency = 22050
        try:
            percussiveChoise(frequency, self.y)
        except:
            self.printText("Ошибка выполнения функции, возможно, вы не выбрали файл")
        return

    def FunctionSTFT(self):
        massiv = ["specshow"]
        try:
            stft(self.y, 22050, massiv)
        except:
            self.printText("Ошибка выполнения функции, возможно, вы не выбрали файл")
        return

    def FunctionGraphs(self):
        try:
            graphWaveshow(self.y, self.sr)
        except:
            self.printText("Ошибка выполнения функции, возможно, вы не выбрали файл")
        return

    def FunctionBeat(self):
        doIt = ['beatDef']
        BeatTempoDef(self.y, self.sr, doIt)
        return

    def FunctionTempo(self) :
        doIt = ['tempoDef']
        BeatTempoDef(self.y, self.sr, doIt)
        return

    def FunctionOnsetStandart(self) :
        funOnsetStandart(self.y, self.sr)
        return

    def FunctionOnsetMedian(self) :
        funOnsetMedian(self.y, self.sr)
        return

        #вызов метода для открытия диалогового окна
    def openFile(self):#метод для запуска диалогового окна для выборв нужного файла
        from tkinter import filedialog
        self.name = StringVar()
        self.name = filedialog.askopenfilename()
        self.printText(self.name)#вызов меода для отображения информации в области Text
        self.frequency = 22050
        self.monoLoad = True
        self.loadFile()

    def printText(self, textRes):#вывод информации в область Text
        self.textRes = textRes
        self.text.insert('end', self.textRes+'\n')


    ################### кнопка STFT
    def stft_class(self): # кнопка быстрого преобразования фурье
        t = Toplevel(self.content1) #определения нового окна
        t.resizable(FALSE, FALSE)
        t.title('STFT')

        lable = Label(t, text = 'Выбор частоты дискретизации\n(рекомендуемая 22050 Гц)').grid(column=0, row = 0 ) #текстовое поле

        self.data = IntVar()
        inputData = Entry(t, textvariable=self.data)#поле ввода

        lable_radButton = Label(t, text = 'Выберете тип графика:')#текстовое поле

        self.graph1 = StringVar()
        self.graph2 = StringVar()
        self.graph1.set('NO')
        self.graph2.set('NO')#выбор типов графиков
        graph_first = Checkbutton(t, text = 'Waveshow', variable = self.graph1, onvalue = 'waveshow', offvalue = 'NO', state='disabled')
        graph_two = Checkbutton(t, text = 'Спектрограмма', variable = self.graph2, onvalue = 'specshow', offvalue = 'NO')

        button_stft = Button(t, text = 'Ok',command = self.getToStft)#кнопка подтверждения

        button_stft.grid(column = 0, row = 3)#определение положения виджетов в поле
        inputData.grid(column = 1, row = 0)
        lable_radButton.grid(column = 0, row = 1)
        graph_first.grid(column = 0, row = 2)
        graph_two.grid(column = 1, row = 2)
        t.grid()

    def getToStft(self, *args): # метод обработчика для функции (stft)
        self.monoLoad = True
        self.graphicsChoise = []
        self.frequency = self.data.get() # частота введёная пользователем
        self.waveshow = self.graph1.get() # выбор графика пользователем, если пользователь не выбрал график спектрограммы,то = No
        self.specshow = self.graph2.get()# выбор графика пользователем, если пользователь не выбрал график огибающей ,то = No
        self.graphicsChoise.append(self.waveshow)
        self.graphicsChoise.append(self.specshow)
        try:
            self.loadFile()
        except :
            self.printText('Не выбран файл для преобразования')
        if self.frequency > 200:
            try:
                stft(self.y, self.sr, self.graphicsChoise)
            except:
                self.printText('Ошибка вычисления STFT - быстрое преобразование Фурье: \n1.Вы не выбрали исследуемый файл'
                               '\n2.Превысили возможную частоту дискретизации')
        else:
            self.printText('Слишком низкая частота дискретизации, возможная (512 - 44100)')

    def loadFile(self, *args) :  # считывание входных данных при частоте заданных пользователем
        self.y, self.sr = librosa.load(self.name, sr = self.frequency, mono = self.monoLoad)
    #####################################1

    ##################################### кнопка SONG (огибающая входного сигнала)
    def song(self):
        t1 = Toplevel(self.content1)
        t1.resizable(FALSE,FALSE)
        t1.title('SONG')

        label = Label(t1, text = "Отображение формы входного сигнала").grid(column=0, row=0) #информация для пользователя

        label1 = Label(t1, text = "Выберите тип считывания звукового файла:").grid(column=0, row=1) #информация для пользователя

        self.mono = StringVar()
        self.stereo = StringVar()
        self.mono.set('NO')
        self.stereo.set('NO')

        self.monoCheck = Checkbutton(t1, text = 'Mono', variable = self.mono, onvalue = 'monoYES', offvalue = 'NO') #выбор функции MONO
        self.stereoCheck = Checkbutton(t1, text = 'Stereo', variable = self.stereo, onvalue = 'stereoYES', offvalue = 'NO') #выбор функции STEREO
        self.buttonLoad = Button(t1, text = 'Ok', command = self.example ,width = 7) #отправка входных данных для обработки

        t1.grid()   #вывод виджетов
        self.monoCheck.grid(column = 0, row=3)
        self.stereoCheck.grid(column = 1, row=3)
        self.buttonLoad.grid(column = 0, row = 4)
    #####################################

    ###################################### кнопка HPSS
    def metHPSS(self):
        t2 = Toplevel(self.content1)
        t2.resizable(FALSE, FALSE)
        t2.title('HPSS')

        self.labelHpss = Label(t2, text = 'Функция разделения входного сигнала\n на гармоническую и ударные составляющие').grid(column = 0, row = 0)

        self.labelChoice = Label(t2, text = 'Веберете выходную информацию для отображения:').grid(column = 0, row = 1)

        self.setHarmonic = StringVar()
        self.setPercussive = StringVar()
        self.setHarmonic.set('NO')
        self.setPercussive.set('NO')
        self.harmonic = Checkbutton(t2, text='Harmonic', variable = self.setHarmonic, onvalue = 'harmonicChoise', offvalue = 'NO')
        self.percussive = Checkbutton(t2, text = 'Percussive', variable = self.setPercussive, onvalue = 'percussiveChoise', offvalue = 'NO')
        self.buttonHttp = Button(t2, text = 'OK', width = 7, command = self.hpssEvents)
        t2.grid()
        self.harmonic.grid(column = 0, row = 2)
        self.percussive.grid(column = 1, row = 2)
        self.buttonHttp.grid(column = 0, row = 3)
        return

    def hpssEvents(self, *args): # обработчик для вызова функции для вывода графиков составляющих сигнала
        self.monoLoad = True
        choiseFunction = {'harmonicChoise':harmonicChoise, 'percussiveChoise':percussiveChoise}
        self.graph = []
        self.frequency = 22050
        self.graph.append(self.setHarmonic.get())
        self.graph.append(self.setPercussive.get())
        for i in self.graph:
            if i != 'NO':
                try:
                    choiseFunction[i](self.frequency, self.y)
                except:
                    self.printText('Ошибка, не выбран файл')
        return
    ###############################################
    def example(self, *args):  #метод обработка данных
        self.dounloudSong = []
        self.frequency = 22050  #параметры
        self.dounloudSong.append(self.mono.get())
        self.dounloudSong.append(self.stereo.get())
        if self.dounloudSong[0] != 'NO' and self.dounloudSong[1] != 'NO': #проверка на ошибки и выбранного функционала
            self.printText('Выберете один тип считывания звукового файла')
        else:
            if self.dounloudSong[0] == "NO" and self.dounloudSong[1] != 'NO':
                self.monoLoad = False   # mono = FALSE
            elif self.dounloudSong[0] != "NO" and self.dounloudSong[1] == 'NO':
                self.monoLoad = True   #mono = TRUE
            try:
                #self.loadFile() #обработка входного файла
                graphWaveshow(self.y, self.sr)  #вывод графика огибающей
            except:
                self.printText('Ошибка: выберите исследуемый файл')

    ################################################################# BEAT AND TEMP
    def BeatTemp(self, *args):
        t3 = Toplevel(self.content1)
        t3.resizable(FALSE, FALSE)
        t3.title('BEAT AND TEMPO')

        self.labelAbout = Label(t3, text='Расчёт глобального (темпа)tempo и\n расчёт местоположения событий (beat)')
        self.labelAbout.grid(column=0, row=0)
        self.beat = StringVar()
        self.tempo = StringVar()
        self.beat.set('NO')
        self.tempo.set('NO')
        labelInfo = Label(t3, text = 'Информация для вывода:')
        labelInfo.grid(column = 0, row = 1)
        beatCheck = Checkbutton(t3, text = 'Beat', variable = self.beat, onvalue = 'beatDef', offvalue = 'NO')
        tempoCheck = Checkbutton(t3, text = 'Tempo', variable = self.tempo, onvalue = 'tempoDef', offvalue = 'NO')
        buttonBT = Button(t3, text = 'OK', width = 7, command = self.BeTeData)
        beatCheck.grid(column = 0, row = 2)
        tempoCheck.grid(column = 1, row = 2)
        buttonBT.grid(column = 0, row = 3)
        return

    def BeTeData(self, *args): #проверка на ошибку и отправка выбранной информации (обработка)
        doIt = []
        doIt.append(self.beat.get())
        doIt.append((self.tempo.get()))
        try:
            BeatTempoDef(self.y, self.sr, doIt)
        except:
            self.printText('Ошибка, возможно, вы не выбрали файл')
        return
    ###############################################################################

    ############################################################################### ONSET
    def onsetMethod(self, *args):
        t4 = Toplevel(self.content1)
        t4.resizable(FALSE, FALSE)
        t4.title('Onset')

        labelOnset = Label(t4, text = 'Вычисление огибающей силы:')
        labelOnset.grid(column = 0, row = 0)

        self.onsetStan = StringVar()
        self.onsetStan.set('NO')
        butStandart = Checkbutton(t4, text = 'Стандартная', variable = self.onsetStan, onvalue='funOnsetStandart', offvalue='NO')
        butStandart.grid(column = 0, row = 1)

        self.onsetMedian = StringVar()
        self.onsetMedian.set('NO')
        butMedian = Checkbutton(t4, text = 'Медианная', variable = self.onsetMedian, onvalue = 'funOnsetMedian', offvalue = 'NO')
        butMedian.grid(column = 1, row = 1)


        buttonOk = Button(t4, text = 'Ok', width = 7, command = self.checkOnset)
        buttonOk.grid(column = 0, row = 2)
        return
    ###############################################################################

    ###############################################################################
    def checkOnset(self,*args):
        doIt = []
        doIt.append(self.onsetStan.get())
        doIt.append(self.onsetMedian.get())
        dictDo = {'funOnsetStandart':funOnsetStandart, 'funOnsetMedian':funOnsetMedian}
        for i in doIt:
            if i != 'NO':
                try:
                    dictDo[i](self.y, self.sr)
                except:
                    self.printText('Ошибка выполнения функций')
        return
    ###############################################################################
def forOnset(y):
    D = np.abs(makeSTFT(y))
    times = librosa.times_like(D)
    return times

def funOnsetStandart(y, sr):
    times = forOnset(y)
    onset_env = librosa.onset.onset_strength(y = y, sr = sr)
    graphPlot(times,2,onset_env)
    return

def funOnsetMedian(y, sr):
    times = forOnset(y)
    onset_env = librosa.onset.onset_strength(y = y, sr = sr, aggregate = np.median, fmax = 8000, n_mels = 256)
    graphPlot(times, 1, onset_env)
    return

def BeatTempoDef(y, sr, doIt): # обработка событий для beat and tempo
    output = []
    onset_env = librosa.onset.onset_strength(y = y, sr = sr, aggregate = np.median)
    tempo, beats = librosa.beat.beat_track(onset_envelope = onset_env, sr = sr)
    beats = librosa.frames_to_time(beats, sr = sr)
    beatsAround = np.around(beats, decimals = 2)
    for functionMake in doIt:
        if functionMake == 'beatDef':
            beatDef(beatsAround)
        if functionMake == 'tempoDef':
            tempoDef(tempo)
    return

def beatDef(beats): #вывод beat в консоль
    classApp.printText('расчёт местоположения событий биений (временные метки)')
    classApp.printText('beats >> '+' '.join(map(str,beats)))
    return

def tempoDef(tempo): #вывод teamp в консоль
    classApp.printText('расчёт глобального темпа (в ударах в минуту)')
    classApp.printText('temp >> '+str(tempo))
    return

def harmonicChoise(Sr, y): # вывод гармонической составляющей сигнала
    D = makeSTFT(y)
    H, P = librosa.decompose.hpss(D)
    D_db = librosa.amplitude_to_db(np.abs(P))
    graphSpecshow(D_db, Sr)
    return

def percussiveChoise(Sr, y): #вывод ударной составляющей сигнала
    D = makeSTFT(y)
    H, P = librosa.decompose.hpss(D)
    D_db = librosa.amplitude_to_db(np.abs(H))
    graphSpecshow(D_db, Sr)
    return

def makeSTFT(y):
    S = librosa.stft(y, n_fft = 2048)
    return S

def stft(y, sr, massiv): #функция быстрого преобразования фурье
    showGraphs = {'specshow':graphSpecshow,'waveshow':graphWaveshow}
    S = makeSTFT(y)
    S_db = librosa.amplitude_to_db(np.abs(S))
    for i in massiv:
        if i!='NO':
            showGraphs[i](S_db,sr)
    return

def graphPlot(time, const,mass):
    fig, ax = plt.subplots()
    ax.plot(time, const + mass/mass.max(), alpha = 1)
    plt.ylabel('Normalized strength')
    plt.show()
    return

def graphSpecshow(S_db,sr):# функция вывода спектрограммы
    fig, ax = plt.subplots()
    img = librosa.display.specshow(S_db,sr = sr, x_axis = 'time', y_axis = 'linear', ax = ax)
    fig.colorbar(img, ax = ax, format="%+2.f dB")
    plt.show()


def graphWaveshow(S, sr):# график отображения формы волна во временной области
    librosa.display.waveshow(S, sr = sr)
    plt.show()

if __name__ == '__main__':
    from tkinter import *
    from tkinter import ttk
    import librosa
    import numpy as np
    import matplotlib.pyplot as plt
    import librosa.display
    root = Tk()
    classApp = mainWindow(root)
    root.mainloop()