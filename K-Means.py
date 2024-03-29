from bokeh.plotting import figure, show
import random

class F_Vector:
    def __init__(self, c_1, c_2):
        self.x = c_1
        self.y = c_2
        self.grupo = Semilla(0, 0)  # aún no pertenece a ningún grupo
        self.color = self.grupo.color  # toma el color de su semilla

    def medir_d_semilla(self, semillas):
        '''Define a qué grupo pertenece
        según su distancia con cada semilla
        '''
        assert type(semillas) == list, 'El arg debe ser una lista de Semillas'
        distancias = {}  # {distancia : semilla}
        for i in semillas:
            assert type(i) == Semilla, 'Debe ser un arreglo de semillas'
            dx = self.x - i.x
            dy = self.y - i.y
            deucl = (dx**2 + dy**2)**(0.5)
            distancias[deucl] = i  # {distancia : semilla}
        d_min = min(distancias)  # pertenece al grupo de la semilla más cercana
        self.grupo = distancias[d_min]

class Semilla:
    def __init__(self, x, y, nombre='Sin asignar', color_sem='#000000'):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.color = color_sem
        self.distancia_recorrida = 0

    def mover_semilla(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        self.distancia_recorrida += ((nuevo_x - self.x) ** 2 + (nuevo_y - self.y) ** 2) ** 0.5
        
class Campo:
    def __init__(self, ancho=200, alto=200):
        self.ancho = ancho
        self.alto = alto
        self.vectors = []
        self.semillas = []

    def agregar_F_Vector(self):
        randx = random.randint(0, self.ancho)
        randy = random.randint(0, self.alto)
        self.vectors.append(F_Vector(randx, randy))

    def agregar_Semilla(self):
        randx = random.randint(0, self.ancho)
        randy = random.randint(0, self.alto)
        self.semillas.append(Semilla(randx, randy, color_sem=generar_color()))

    def mostrar_campo(self):
        figura = figure()
        for i in self.vectors:
            figura.circle(i.x, i.y, color=i.color, size=7)
        for i in self.semillas:
            figura.asterisk(i.x, i.y, color=i.color, size=20)
        show(figura)

def K_means(campo):
    romper_bucle = False
    while True:
        # medir las distancias de cada FV con cada semilla
        for F in campo.vectors:
            F.medir_d_semilla(campo.semillas)  # asignarle un grupo a cada vector
            F.color = F.grupo.color
        campo.mostrar_campo()
        # calcular centroides
        for S in campo.semillas:
            dist_x = 0
            dist_y = 0
            cantidad_Vectores = 0
            for V in campo.vectors:
                if V.grupo == S:
                    dist_x += V.x
                    dist_y += V.y
                    cantidad_Vectores += 1
            if cantidad_Vectores != 0:
                new_x = dist_x / cantidad_Vectores  # Medias
                new_y = dist_y / cantidad_Vectores
                S.mover_semilla(new_x, new_y)
        campo.mostrar_campo()
        distancias_recorridas = [sem.distancia_recorrida for sem in campo.semillas]
        print(distancias_recorridas)
        if max(distancias_recorridas) < 0.5:
            romper_bucle = True
        print(romper_bucle)
        if romper_bucle:
            break
    campo.mostrar_campo()

def generar_color():
    letras = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    n = '#'
    for _ in range(6):
        n = n + random.choice(letras)
    return n

if __name__ == '__main__':
    campo = Campo()
    num = int(input('¿Cuantos Vectores hay? : '))
    for _ in range(num):
        campo.agregar_F_Vector()
    num_semillas = int(input('¿Cuantos grupos quieres formar? : '))
    for _ in range(num_semillas):
        campo.agregar_Semilla()
    campo.mostrar_campo()
    K_means(campo)
