
import os,csv

from . import NUM_RECORDS

class Records:

    file_name = 'scores.csv'
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, 'data', file_name)

    def __init__(self):
        self.game_records = []
        self.comprobar_Archivo()

    def comprobar_Archivo (self):
        dir_data = os.path.dirname(self.path)
        if not os.path.isdir(dir_data):
            print('el directorio de datos no esxiste lo estoy creando para ti')
            os.makedirs(dir_data)
        if not os.path.exists(self.path):
            print('el archivo records no esxiste: creandolo sin datos')
            self.reset()

    def guardar(self):
        with open(self.path, "w") as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(['nombre', 'puntos'])
            writer.writerows(self.game_records)

    def cargar(self):
        with open(self.path, mode='r')as file:
            reader = csv.reader(file, lineterminator='\n')
            self.game_records = []
            contador = 0
            for line in reader:
                contador += 1
                if contador == 1:
                    continue
                self.game_records.append([line[0], int(line[1])])
            

    def insertar_record(self, nombre, puntuacion):
        pass

    def puntuacion_menor(self):
        return 0
    
    def reset(self):
        self.game_records = []
        for cont in range(NUM_RECORDS):
            self.game_records.append(['-------', 0000])
        self.guardar()
