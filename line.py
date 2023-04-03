
def get_the_value(mas, name, find):
    file = open(f"var_0522/{name}.txt", "r")

    i = int(0)
    ind = int(0)
    FIND = find
    i += 1
    lines = file.readlines()
    var = file.close
    n = int(0)


    for i in range(0, len(lines)):
        if FIND in lines[i]:
            n = i+1
            while lines[n] != ' \n' and lines[n] != '\n':
                if "-0" in lines[n]:
                    lines[n].replace("-0", "  uu")
                    print(lines[n])

                mas_of_values = lines[n].split()
                n += 1
                if find == 'PRES':
                    mas.append([float(mas_of_values[0]), float(mas_of_values[3])])
                else:
                    mas.append([float(mas_of_values[0]), float(mas_of_values[4])])
    return mas

def fill_mas(find):
    name_raw = ""
    name_ready = ""

    for k in range(1, 11):
        string=[]
        for i in range(1,4):
            for j in range(1, 5):
                name_raw += "material " + str(i) + "/" + "Material_" + str(i) +"_p_line_" + str(j) + "_Cont_F_"+ str(k*100)
                name_ready += "Material " + str(i) + "/" + "line " + str(j) + "/" + "Material_" + str(i) + "_p_line_" + str(j) + "_Cont_F_" + str(k*100) + "_"+str(find)

                string.clear()
                get_the_value(string, name_raw, find)
                write_file(string, name_ready)

                name_raw = ""
                name_ready = ""



def write_file(mas, name_ready):

    f = open(f"{name_ready}.txt", "w")
    for i in range(len(mas)):
        f.write(str(mas[i][0]) + " " + str(mas[i][1]) + '\n')


fill_mas('PRES')
fill_mas('SFRI')