import ctypes
import imghdr
import os
from collections import *
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

from PIL import Image, ImageTk, ImageOps, ImageDraw



def newImage(canvas):
    imageName = askopenfilename()
    filetype = ""

    try:
        filetype = imghdr.what(imageName)
    except:
        messagebox.showinfo(title="Image File", message="Choose an Image File!", parent=canvas.data.mainWindow)

    if filetype in ['jpeg', 'bmp', 'png', 'tiff']:
        canvas.data.imageLocation = imageName
        im = Image.open(imageName)
        canvas.data.image = im
        canvas.data.originalImage = im.copy()
        canvas.data.undoQueue.append(im.copy())
        canvas.data.imageSize = im.size  # Original Image dimensions
        canvas.data.imageForTk = makeImageForTk(canvas)
        drawImage(canvas)
    else:
        messagebox.showinfo(title="Image File", message="You have to choose image!", parent=canvas.data.mainWindow)

def makeImageForTk(canvas):
    im = canvas.data.image
    if canvas.data.image is not None:


        imageWidth = canvas.data.image.size[0]
        imageHeight = canvas.data.image.size[1]

        if imageWidth > imageHeight:
            resizedImage = im.resize((canvas.data.width,
                                      int(round(float(imageHeight) * canvas.data.width / imageWidth))))

            canvas.data.imageScale = float(imageWidth) / canvas.data.width
        else:
            resizedImage = im.resize((int(round(float(imageWidth) * canvas.data.height / imageHeight)),
                                      canvas.data.height))
            canvas.data.imageScale = float(imageHeight) / canvas.data.height

        canvas.data.resizedIm = resizedImage
        return ImageTk.PhotoImage(resizedImage)

def drawImage(canvas):
    if canvas.data.image is not None:

        canvas.create_image(canvas.data.width / 2.0 - canvas.data.resizedIm.size[0] / 2.0,
                            canvas.data.height / 2.0 - canvas.data.resizedIm.size[1] / 2.0,
                            anchor=NW, image=canvas.data.imageForTk)
        canvas.data.imageTopX = int(round(canvas.data.width / 2.0 - canvas.data.resizedIm.size[0] / 2.0))
        canvas.data.imageTopY = int(round(canvas.data.height / 2.0 - canvas.data.resizedIm.size[1] / 2.0))


'''Merge Items jako opcja w menu'''


'''def newImage2(canvas):
    imageName2 = askopenfilename()
    filetype2 = ""

    try:
        filetype2 = imghdr.what(imageName2)
    except:
        messagebox.showinfo(title="Image File", message="Choose an Image File!", parent=canvas.data.mainWindow)

    if filetype2 in ['jpeg', 'bmp', 'png', 'tiff']:
        canvas.data.imageLocation = imageName2
        im2 = Image.open(imageName2)
        canvas.data.image = im2
        canvas.data.originalImage = im2.copy()
        canvas.data.undoQueue.append(im2.copy())
        canvas.data.imageSize = im2.size  # Original Image dimensions
        canvas.data.imageForTk = makeImageForTk2(canvas)
        drawImage2(canvas)
    else:
        messagebox.showinfo(title="Image File", message="You have to choose image!", parent=canvas.data.mainWindow)

### Dodajemy drugie zdjęcie

def makeImageForTk2(canvas):
    im2 = canvas.data.image2
    if canvas.data.image2 is not None:


        imageWidth2 = canvas.data.image.size2[0]
        imageHeight2 = canvas.data.image.size2[1]

        if imageWidth2 > imageHeight2:
            resizedImage2 = im2.resize((canvas.data.width2,
                                      int(round(float(imageHeight2) * canvas.data.width / imageWidth2))))

            canvas.data.imageScale2 = float(imageWidth2) / canvas.data.width2
        else:
            resizedImage2 = im2.resize((int(round(float(imageWidth2) * canvas.data.height / imageHeight2)),
                                      canvas.data.height2))
            canvas.data.imageScale = float(imageHeight2) / canvas.data.height2

        canvas.data.resizedIm2 = resizedImage2
        return ImageTk.PhotoImage(resizedImage2)


def drawImage2(canvas):
    if canvas.data.image is not None:

        canvas.create_image(canvas.data.width / 2.0 - canvas.data.resizedIm.size2[0] / 2.0,
                            canvas.data.height / 2.0 - canvas.data.resizedIm.size2[1] / 2.0,
                            anchor=NE, image=canvas.data.imageForTk2)
        canvas.data.imageTopX = int(round(canvas.data.width2 / 2.0 - canvas.data.resizedIm.size2[0] / 2.0))
        canvas.data.imageTopY = int(round(canvas.data.height2 / 2.0 - canvas.data.resizedIm.size2[1] / 2.0))







'''




def closeBrightnessWindow(canvas):
    if canvas.data.image is not None:
        save(canvas)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.brightnessWindowClose = True


def changeBrightness(canvas, brightnessWindow, brightnessSlider, previousVal):
    if canvas.data.brightnessWindowClose:
        brightnessWindow.destroy()
        canvas.data.brightnessWindowClose = False

    else:

        if canvas.data.image is not None and brightnessWindow.winfo_exists():
            sliderVal = brightnessSlider.get()
            scale = (sliderVal - previousVal) / 100.0
            canvas.data.image = canvas.data.image.point(lambda i: i + int(round(i * scale)))
            canvas.data.imageForTk = makeImageForTk(canvas)
            drawImage(canvas)
            canvas.after(200,
                         lambda: changeBrightness(canvas, brightnessWindow, brightnessSlider, sliderVal))


def brightness(canvas):
    canvas.data.colourPopToHappen = False
    canvas.data.cropPopToHappen = False
    canvas.data.drawOn = False
    brightnessWindow = Toplevel(canvas.data.mainWindow)
    brightnessWindow.title("Brightness")
    brightnessSlider = Scale(brightnessWindow, from_=-100, to=100, orient=HORIZONTAL)
    brightnessSlider.pack()
    OkBrightnessFrame = Frame(brightnessWindow)
    OkBrightnessButton = Button(OkBrightnessFrame, text="OK", command=lambda: closeBrightnessWindow(canvas))
    OkBrightnessButton.grid(row=0, column=0)
    OkBrightnessFrame.pack(side=BOTTOM)
    changeBrightness(canvas, brightnessWindow, brightnessSlider, 0)
    brightnessSlider.set(0)
def histogram(canvas):
    canvas.data.colourPopToHappen = False
    canvas.data.cropPopToHappen = False
    canvas.data.drawOn = False
    histWindow = Toplevel(canvas.data.mainWindow)
    histWindow.title("Histogram")
    canvas.data.histCanvasWidth = 350
    canvas.data.histCanvasHeight = 475
    histCanvas = Canvas(histWindow, width=canvas.data.histCanvasWidth,
                        height=canvas.data.histCanvasHeight)
    histCanvas.pack()

    redSlider = Scale(histWindow, from_=-100, to=100,
                      orient=HORIZONTAL, label="R")
    redSlider.pack()
    blueSlider = Scale(histWindow, from_=-100, to=100,
                       orient=HORIZONTAL, label="B")
    blueSlider.pack()
    greenSlider = Scale(histWindow, from_=-100, to=100,
                        orient=HORIZONTAL, label="G")
    greenSlider.pack()
    OkHistFrame = Frame(histWindow)
    OkHistButton = Button(OkHistFrame, text="OK",
                          command=lambda: closeHistWindow(canvas))
    OkHistButton.grid(row=0, column=0)
    OkHistFrame.pack(side=BOTTOM)
    initialRGB = (0, 0, 0)
    changeColours(canvas, redSlider, blueSlider, greenSlider, histWindow, histCanvas, initialRGB)
def changeColours(canvas, redSlider, blueSlider, greenSlider, histWindow, histCanvas, previousRGB):
    if canvas.data.histWindowClose:
        histWindow.destroy()
        canvas.data.histWindowClose = False
    else:

        if canvas.data.image is not None and histWindow.winfo_exists():
            r, g, b = canvas.data.image.split()
            sliderValR = redSlider.get()
            (previousR, previousG, previousB) = previousRGB
            scaleR = (sliderValR - previousR) / 100.0
            r = r.point(lambda i: i + int(round(i * scaleR)))
            sliderValG = greenSlider.get()
            scaleG = (sliderValG - previousG) / 100.0
            g = g.point(lambda i: i + int(round(i * scaleG)))
            sliderValB = blueSlider.get()
            scaleB = (sliderValB - previousB) / 100.0
            b = b.point(lambda i: i + int(round(i * scaleB)))
            canvas.data.image = Image.merge(canvas.data.image.mode, (r, g, b))

            canvas.data.imageForTk = makeImageForTk(canvas)
            drawImage(canvas)
            displayHistogram(canvas, histWindow, histCanvas)
            previousRGB = (sliderValR, sliderValG, sliderValB)
            canvas.after(200, lambda: changeColours(canvas, redSlider,
                                                    blueSlider, greenSlider, histWindow, histCanvas, previousRGB))


def displayHistogram(canvas, histWindow, histCanvas):
    histCanvasWidth = canvas.data.histCanvasWidth
    histCanvasHeight = canvas.data.histCanvasHeight
    margin = 50
    if canvas.data.image is not None:
        histCanvas.delete(ALL)
        im = canvas.data.image

        histCanvas.create_line(margin - 1, histCanvasHeight - margin + 1,
                               margin - 1 + 258, histCanvasHeight - margin + 1)
        xmarkerStart = margin - 1
        for i in range(0, 257, 64):
            xmarker = "%d" % i
            histCanvas.create_text(xmarkerStart + i,
                                   histCanvasHeight - margin + 7, text=xmarker)

        histCanvas.create_line(margin - 1,
                               histCanvasHeight - margin + 1, margin - 1, margin)
        ymarkerStart = histCanvasHeight - margin + 1
        for i in range(0, histCanvasHeight - 2 * margin + 1, 50):
            ymarker = "%d" % i
            histCanvas.create_text(margin - 1 - 10,
                                   ymarkerStart - i, text=ymarker)

        r, g, b = im.histogram()[:256], im.histogram()[256:512], im.histogram()[512:768]
        for i in range(len(r)):
            pixelNo = r[i]
            histCanvas.create_oval(i + margin,
                                   histCanvasHeight - pixelNo / 100.0 - 1 - margin, i + 2 + margin,
                                   histCanvasHeight - pixelNo / 100.0 + 1 - margin,
                                   fill="red", outline="red")
        for i in range(len(g)):
            pixelNo = g[i]
            histCanvas.create_oval(i + margin,
                                   histCanvasHeight - pixelNo / 100.0 - 1 - margin, i + 2 + margin,
                                   histCanvasHeight - pixelNo / 100.0 + 1 - margin,
                                   fill="green", outline="green")
        for i in range(len(b)):
            pixelNo = b[i]
            histCanvas.create_oval(i + margin,
                                   histCanvasHeight - pixelNo / 100.0 - 1 - margin, i + 2 + margin,
                                   histCanvasHeight - pixelNo / 100.0 + 1 - margin,
                                   fill="blue", outline="blue")

def closeHistWindow(canvas):
    if canvas.data.image is not None:
        save(canvas)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.histWindowClose = True




def init(root, canvas):
    buttonsInit(root, canvas)
    menuInit(root, canvas)
    canvas.data.image = None
    canvas.data.angleSelected = None
    canvas.data.rotateWindowClose = False
    canvas.data.brightnessWindowClose = False
    canvas.data.brightnessLevel = None
    canvas.data.histWindowClose = False
    canvas.data.solarizeWindowClose = False
    canvas.data.posterizeWindowClose = False
    canvas.data.colourPopToHappen = False
    canvas.data.cropPopToHappen = False
    canvas.data.endCrop = False
    canvas.data.drawOn = True

    canvas.data.undoQueue = deque([], 10)
    canvas.data.redoQueue = deque([], 10)
    canvas.pack()


def buttonsInit(root, canvas):
    backgroundColour = "white"
    buttonWidth = 14
    buttonHeight = 2
    toolKitFrame = Frame(root)

    brightnessButton = Button(toolKitFrame, text="Brightness",
                              background=backgroundColour,
                              width=buttonWidth, height=buttonHeight,
                              command=lambda: brightness(canvas))
    brightnessButton.grid(row=2, column=0)
    histogramButton = Button(toolKitFrame, text="Change RGB",
                             background=backgroundColour,
                             width=buttonWidth, height=buttonHeight,
                             command=lambda: histogram(canvas))
    histogramButton.grid(row=3, column=0)
    contrastButton = Button(toolKitFrame, text="Change Constrast",
                            background=backgroundColour, width=buttonWidth,
                            height=buttonHeight, command=lambda: brightness(canvas))
    contrastButton.grid(row=4, column=0)
    resetButton = Button(toolKitFrame, text="Reset",
                         background=backgroundColour, width=buttonWidth,
                         height=buttonHeight, command=lambda: reset(canvas))
    resetButton.grid(row=9, column=0)



    toolKitFrame.pack(side=LEFT)


def menuInit(root, canvas):
    menubar = Menu(root)
    menubar.add_command(label="Open", command=lambda: newImage(canvas))
   #menubar.add_command(label="Open_Second", command=lambda: newImage2(canvas))
    menubar.add_command(label="Save", command=lambda: save(canvas))
    menubar.add_command(label="Save As", command=lambda: saveAs(canvas))
    root.config(menu=menubar)

    filtermenu = Menu(menubar, tearoff=0)
    filtermenu.add_command(label="Negativ", command=lambda: invert(canvas))
    menubar.add_cascade(label="Filter", menu=filtermenu)
    root.config(menu=menubar)
def invert(canvas):
    canvas.data.colourPopToHappen = False
    canvas.data.cropPopToHappen = False
    canvas.data.drawOn = False
    if canvas.data.image is not None:
        canvas.data.image = ImageOps.invert(canvas.data.image)
        save(canvas)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.imageForTk = makeImageForTk(canvas)
        drawImage(canvas)
def reset(canvas):
    canvas.data.colourPopToHappen = False
    canvas.data.cropPopToHappen = False
    canvas.data.drawOn = False

    if canvas.data.image is not None:
        canvas.data.image = canvas.data.originalImage.copy()
        save(canvas)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.imageForTk = makeImageForTk(canvas)
        drawImage(canvas)
def save(canvas):
    if canvas.data.image is not None:
        im = canvas.data.image
        im.save(canvas.data.imageLocation)
def saveAs(canvas):

    if canvas.data.image is not None:
        filename = asksaveasfilename(defaultextension=".jpg")
        im = canvas.data.image
        im.save(filename)

def run():
    root = Tk()
    root.title("Image Editor v. 1.0")
    canvasWidth = 500
    canvasHeight = 500
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight, background="gray")

    class Struct: pass

    canvas.data = Struct()
    canvas.data.width = canvasWidth
    canvas.data.height = canvasHeight
    canvas.data.mainWindow = root
    init(root, canvas)

    root.mainloop()


run()