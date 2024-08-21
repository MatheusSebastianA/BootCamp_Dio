import datetime

data_hora = datetime.datetime.now()

#Formatação para data e hora no Brasil
print(data_hora.strftime("%d/%m/%Y %H:%M:%S" ))