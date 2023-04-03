import io
import math
from decimal import Decimal

def get_the_value(mas, name):
    with io.open(f"coor/{name}.txt", encoding = 'utf-8') as file:
        for line in file:
            if line != '\n' and line != ' \n':
                mas_of_values = line.split()
                mas.append(mas_of_values)
    return mas

def local(mas):
    mas_local = []
    mas_local.append([mas[0][0], 0])
    for i in range(1, len(mas)):
        local = Decimal(math.sqrt((math.pow(Decimal(mas[i-1][1])-Decimal(mas[i][1]), 2)+math.pow(Decimal(mas[i-1][2])-Decimal(mas[i][2]), 2))))
        print(local)
        mas_local.append([mas[i][0], local])
    return mas_local

def write_file(mas, name_ready):
    f = open(f"{name_ready}.txt", "w")
    for i in range(len(mas)):
        f.write(str(mas[i][0]) + " " + str(mas[i][1]) + '\n')

def fill_local(k):
    mas = []
    get_the_value(mas, "coor_line_" + str(k) +"_F_Y")
    for i in range(len(mas)):
        for j in range(3):
            mas[i][j] = float(mas[i][j])
    mas.sort(key=lambda x : x[1], reverse=True)
    mas_local = local(mas)
    mas_local.sort(key=lambda x:x[1])
    write_file(mas_local, "coor/coor_line_" + str(k) +"_F_Y")
    return mas_local

mas_all = []
for i in range(1, 5):
    mas_all.append(fill_local(i))

print(mas_all)

def import_data_line(name_line, name_coord, mas_line):
    name_c = open(f"{name_coord}.txt", "r")
    line_coor = name_c.readlines()
    for el in line_coor:
        mas = el.split(" ")
        name_l = open(f"{name_line}.txt", "r")
        line_local = name_l.readlines()
        for line in line_local:
            mas_local = line.split(" ")
            if mas[0] in line:
                mas_line.append(float(mas_local[1]))
                break
        name_l.close()
    name_c.close()

def write_line(mas, name_ready):

    f = open(f"{name_ready}.txt", "w")
    for i in range(len(mas)):
        f.write(str(mas[i]) + '\n')


def fill(find):
    name_raw = ""
    name_ready = ""
    mas = []

    for k in range(1, 11):
        string=[]
        for i in range(1,4):
            for j in range(1, 5):
                name_raw += "Material " + str(i) + "/" + "line " + str(j) + "/" + "Material_" + str(i) + "_p_line_" + str(j) + "_Cont_F_" + str(k*100) + "_" + str(find)
                name_ready += "Material " + str(i) + "/" + "line " + str(j) + "/" + "Material_" + str(i) + "_p_line_" + str(j) + "_Cont_F_" + str(k*100) + "_" + str(find)

                string.clear()
                import_data_line(name_raw, "coor/coor_line_" + str(j) +"_F_Y", string)
                #mas.append(string)
                write_line(string, name_ready)

                name_raw = ""
                name_ready = ""

fill("SFRI")
fill("PRES")

def write_local(mas, name_ready):

    f = open(f"{name_ready}.txt", "w")
    for i in range(len(mas)):
        f.write(str(mas[i][1]) + '\n')

for i in range (1, 5):
    write_local(mas_all[i-1], "coor/coor_line_" + str(i) +"_F_Y")