import turtle
from PIL import Image
from PIL import EpsImagePlugin
import io

# ------------------------- Funciones ------------------------- #
def line(x_1, y_1, x_2,  y_2, t):
    pensize = t.pensize()
    t.pensize(1)
    t.penup()
    t.goto(x_1, y_1)
    t.pendown()
    t.goto(x_2, y_2)
    t.penup()
    t.pensize(pensize)

def buscar_nodo(nodos, nombre):
    for capa in nodos:
        for nodo in capa:
            if nodo.nombre == nombre:
                return nodo
    return -1




# ------------------------- Clase Nodo ------------------------- #
class nodo: 

    def __init__(self, nombre, duracion, x, y, es = 0, ef = 0, ls = 0, lf = 0, radio = 50):
        self.nombre = nombre
        self.duracion = duracion
        
        self.es = es
        self.ef = ef
        self.ls = ls
        self.lf = lf

        self.x = x
        self.y = y
        self.radio = radio
        self.dock_right = x + radio
        self.dock_left = x - radio
        self.font = "Arial"
        self.size = 15
        self.format = "normal"


    def draw(self, tort):
        # ---------------- Circulo ---------------- #
        tort.penup()
        tort.goto(self.x, self.y - self.radio)
        tort.pendown()

        tort.circle(self.radio)

        # ---------- Cruz (20% de radio) ---------- #
        # 20% of radius
        padding = round(self.radio * 0.2 / 2)
        length = round(self.radio * 0.8)

        # |
        line(self.x, self.y - padding,
             self.x, self.y - padding - length, tort)

        # --
        line(self.x + length / 2 , self.y - self.radio / 2,
             self.x + length / 2 - length, self.y - self.radio / 2, tort)

        # ---------- Texto ----------
        if self.duracion != 0:

            # Name
            tort.goto(self.x - (self.radio / 3) , self.y + self.radio / 4)
            tort.write(self.nombre, align="center", font=(self.font, self.size, self.format))

            # Duration
            tort.goto(self.x + self.radio / 3 , self.y + self.radio / 4)
            tort.write(self.duracion, align="center", font=(self.font, self.size, self.format))

        else:

            # Name
            tort.goto(self.x, self.y + self.radio / 4)
            tort.write(self.nombre, align="center", font=(self.font, self.size, self.format))

        '''
            ES | EF
            -------
            LS | LF
        '''
        # ES
        tort.goto(self.x - self.radio / 4 , self.y - self.radio / 2 )
        tort.write(self.es, align="center", font=(self.font, self.size, self.format))

        # EF
        tort.goto(self.x + self.radio / 4 , self.y - self.radio / 2 )
        tort.write(self.ef, align="center", font=(self.font, self.size, self.format))

        # LS
        tort.goto(self.x - self.radio / 4 , self.y - self.radio + padding)
        tort.write(self.ls, align="center", font=(self.font, self.size, self.format))

        # LF
        tort.goto(self.x + self.radio / 4 , self.y - self.radio + padding)
        tort.write(self.lf, align="center", font=(self.font, self.size, self.format))


    def connect_left(self, nodo, tort):
        line(self.dock_left , self.y, nodo.dock_right,  nodo.y, tort)



# ------------------------- Clase Graficador ------------------------- #
class graficador:

    def __init__(self, nodos, dependencias):
        self.nodos = nodos
        self.dependencias = dependencias
        self.tort = turtle.Turtle()
        self.tort.hideturtle()
        self.tort._tracer(False)
        self.tort.pensize(2)

    def draw(self):
        capa_x = -900
        screen = turtle.Screen()
        screen.setup(1920, 1080)
        counter = 0
        ultimos = []

        for capa in self.nodos:
            cantidad_nodos = len(capa)
            nodo_y = 0

            if cantidad_nodos == 1:
                nodo_y = 0
            else:
                nodo_y += ( (cantidad_nodos - 1) * 2 * nodo.radio)
                    
            for nodo in capa:
                nodo.x = capa_x
                nodo.y = nodo_y
                nodo.draw(self.tort)
                nodo_y -= + (4 * nodo.radio)

                if capa == self.nodos[-1]:
                    for nodo_anterior in ultimos:
                        nodo.connect_left(nodo_anterior, self.tort)
                elif capa != self.nodos[0]:                
                    ultimos.append(nodo)

                    for char in self.dependencias[counter]:
                        if char == '-':
                            nodo.connect_left(buscar_nodo(self.nodos, "Inicio"), self.tort)
                        elif char != ',':
                            nodo.connect_left(buscar_nodo(self.nodos, char), self.tort)
                    counter += 1

            capa_x += (3 * nodo.radio)


    def save(self):
        ps = self.tort.getscreen().getcanvas().postscript(colormode="color")
        EpsImagePlugin.gs_windows_binary = "./Ghostscript/gs10.03.0/bin/gswin64c.exe"
        im = Image.open(io.BytesIO(ps.encode("utf-8")))
        im.save('RED.png', format="PNG")
