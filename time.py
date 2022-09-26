from datetime import datetime, timedelta

with open('time.txt') as file:
    inicio = fim = datetime.now()
    tempo = timedelta(days=0, seconds=0, microseconds=0)
    datas = []
    for f in file.readlines():
        line = f.strip("\n").split("\t")
        try:
            inicio = datetime.strptime(line[0], "%H:%M %d/%m/%Y")
            fim = datetime.strptime(line[1], "%H:%M %d/%m/%Y")
            tempo = tempo+(fim-inicio)
        except:
            print(line)
        # print(inicio, fim, line, fim-inicio)
        
    print(tempo.total_seconds()/3600*42)