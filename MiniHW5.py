def sort_csv_columns(csv_file_content):
    lines = csv_file_content.split("\\n")

    for i in range(0, len(lines)) :
        lines[i] = lines[i].split(";")
    
    col = [[lines[i][j] for i in range(len(lines))] for j in range(len(lines[0]))]

    for i in range(len(col)):
        for j in range(len(col)):
            if col[i][0].lower() < col[j][0].lower():
                k = col[i]
                col[i] = col[j]
                col[j] = k

    return convert_to_string(col) 

def convert_to_string (col):
    val = ''
    for i in range(len(col[0])):
            for j in range(len(col)):
                val = val + col[j][i]
                if(j == len(col) - 1):
                    val = val + "\n"
                else:
                    val = val + ";"
    return val 

#myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n17945;10091;10088;3907;10132\n2;12;13;48;11

