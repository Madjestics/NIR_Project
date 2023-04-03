import io

def get_the_value(mas, name, n):
    with io.open(f"зуб/{name}.txt", encoding = 'utf-8') as file:
        for line in file:
            if line != '\n' and line != ' \n':
                mas_of_values = line.split()
                if 'VALUE' == mas_of_values[0]:
                    mas.append(mas_of_values[n])
    return mas

def fill_mas(points):
    name = ""
    mas=[]
    for k in range(1, 11):
        name_end = str(k*100)
        string=[]
        for i in range(1,4):
            name += "мат" + str(i) + "/" + "Material_" + str(i) +"_" + str(points) + "_point_10_Cont_F_"+name_end
            for j in range(3, 6):
                get_the_value(string, name, j)
            name = ""
        mas.append(string)
    return mas

def write_file(mas, k):
    string = "result_" + str(k) +".txt"
    f = open(string, 'w')
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            f.write(str(mas[i][j]))
            f.write('\t')
        f.write('\n')


mas_1 = fill_mas(1)
mas_2 = fill_mas(2)
mas_4 = fill_mas(4)
for i in range(len(mas_1)):
    print(mas_1[i])
print()
write_file(mas_1, 1)
for i in range(len(mas_2)):
    print(mas_2[i])
print()
write_file(mas_2, 2)
for i in range(len(mas_4)):
    print(mas_4[i])
write_file(mas_4, 4)