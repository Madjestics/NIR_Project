
def get_the_value(mas, name):
    file = open(f"var_0522/{name}.txt", "r")

    i = int(0)
    FIND = 'THZX'
    lines = file.readlines()
    var = file.close
    n = int(0)

    for i in range(len(lines)):
        if FIND in lines[i]:
            n = i+1
            while lines[n] != ' \n' and lines[n] != '\n':
                mas_of_values = lines[n].split()
                print(mas_of_values[2])
                mas_temp = []
                mas_temp.append(mas_of_values[0])
                mas_temp.append(mas_of_values[1])
                mas_temp.append(mas_of_values[2])
                mas.append(mas_temp)
                n += 1
                if len(lines) == n:
                    break

    return mas

def fill_mas():
    mas = []
    for mtrl in range(1, 4):
        for force in range(1,5):
            name_read = "material " + str(mtrl) + "/" + "Material_" + str(mtrl) + "_" + "line_" + str(force) + "_coor_F_" + str(100)
            string = []
            get_the_value(string, name_read)

            name_write = "coor" + "/" + "coor_line_" + str(force)+"_F_Y"
            write_file(string, name_write)
            name_read = ""
            name_write = ""
            mas.clear()



def write_file(mas, name_write):
    f = open(f"{name_write}.txt", "w")

    for i in range(len(mas)):
        f.write(str(mas[i][0]) + " " + str(mas[i][1]) + " " + str(mas[i][2]) + '\n')


fill_mas()