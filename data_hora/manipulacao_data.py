from datetime import datetime, timedelta

data_hora = datetime.utcnow()
data_hora += timedelta(weeks=1)

print(f"Data e hora Semana que vem: {data_hora}")
print(f"Data semana que vem: {data_hora.date()}")
print(f"Hora semana que vem: {data_hora.time()}")