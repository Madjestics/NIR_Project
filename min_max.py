
def get_the_value(mas, name):
    file = open(f"{name}.txt", "r")

    i = int(0)
    kolvo_el = int(0)
    sum = float(0)
    FIND = 'MAX'
    i += 1
    lines = file.readlines()
    var = file.close
    n = int(0)
    kolvo_el = int(0)

    for i in range(0, len(lines)):
        if FIND in lines[i]:
            # line = lines[i+1].split()
            # ind = int(FIND.index(lines[i]))
            # print(f'Индекс столбца = {ind}')
            n = i + 2
            if lines[n] != ' \n' and lines[n] != '\n':
                mas_of_values = lines[n].split()
                print(mas_of_values[-1])
                return mas_of_values[-1]


def fill_mas():
    mas = []

    for n_Mater in range(1, 4):
        for region in range(1, 4):
            if region == 1:
                region = "dent"
            elif region == 2:
                region = "emal"
            elif region == 3:
                region = "vkl"
            for measure in range(1, 3):
                if measure == 1:
                    str_meas = "eint"
                elif measure == 2:
                    str_meas = "sint"

                for force in range(1, 11):
                    name_read = "материал " + str(n_Mater) + "/" + "Material_" + str(
                        n_Mater) + "_" + region + "_" + str_meas + "_" + str(force * 100)
                    string = []
                    average_value = get_the_value(string, name_read)  # среднее значение
                    mas.append(average_value)

                    name_write = "Material " + str(n_Mater) + "/" + region + "/" + str_meas + "/" + \
                                 "Material_" + str(n_Mater) + "_" + region + "_" + str_meas + "_" + "maximum"
                    write_file(mas, name_write)
                    name_read = ""
                    name_write = ""
                mas.clear()


def write_file(mas, name_write):
    f = open(f"{name_write}.txt", "w")
    for i in range(len(mas)):
        f.write(str(mas[i]) + '\n')


fill_mas()