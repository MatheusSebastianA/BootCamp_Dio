from datetime import datetime

data_hora_str = "2024-8-21 10:20"
mascara_ptbr = "%d/%m/%Y %H:%M"
mascara_en = "%Y-%m-%d %H:%M"
data_hora = datetime.now()

print(data_hora.strftime(mascara_ptbr))
print()
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(data_convertida.strftime(mascara_ptbr))