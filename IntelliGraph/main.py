import csv
#http://research.iac.es/sieinvens/python-course/source/matplotlib.html
path = "./files/datos.csv" #Reemplazar

def read_file(path_file):
    try:
        with open(path_file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                
                for row in csv_reader:
                    lo_que_nosinteresa = row[3:]
                    print(lo_que_nosinteresa)
    except:
        print("No es posible leer el archivo!")

if __name__ == '__main__':
    read_file(path)