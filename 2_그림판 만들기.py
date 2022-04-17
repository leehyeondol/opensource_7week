from tkinter import*
from tkinter.colorchooser import*
from tkinter.simpledialog import*

def mouseClick(event): ##마우스를 클릭하는 시점의 시작점의 x1,y1값을 지정
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event): ##마우스를 놓는 시점의 끝점 x2,y2값을 지정
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width = penWidth, fill = penColor)

def getColor(): ##색을 선택할때 나타나는 메뉴 함수 실행
    global penColor
    color = askcolor()
    penColor = color[1]

def getWidth():
    global penWidth
    penWidth = askinteger("선 두께", "선 두께(1~10)를 입력하세요.", minvalue = 1, maxvalue = 10)

##2019038085 이현도

window = None
canvas = None
x1, y1, x2, y2 = [None] * 4
penColor = 'black'
penWidth = 5

if __name__=="__main__":
    window = Tk()
    window.title("그림판 만들기")
    canvas = Canvas(window, height = 500, width = 500)
    canvas.bind("<Button-1>", mouseClick)
    canvas.bind("<ButtonRelease-1>", mouseDrop)
    canvas.pack()

    mainMenu = Menu(window)
    window.config(menu = mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "설정", menu = fileMenu)
    fileMenu.add_command(label = "선 색상 선택", command = getColor)
    fileMenu.add_separator()
    fileMenu.add_command(label = "선 두께 설정", command = getWidth)

    window.mainloop()
