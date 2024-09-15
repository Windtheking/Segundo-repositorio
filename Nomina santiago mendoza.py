HorasT = int(input("valor horas trabajadas "))
#horas trabajadas (no se sabe si semanales o diarias)
ValorHT = int("5532")
#valor hora trabajada
ThorasT = 192
#Total Horas Trabajadas
VhorasED = 6915 
#valor horas extra diurnas (25%), 6am - 8:59pm; $1383 + $5532 = $6915
VhorasEN = ValorHT * 1.75
#valor horas extra nocturnas (75%), 9pm - 5:59am; $4149 + $5532 = $9618
VhorasEDFD = ValorHT * 2
#Valor Horas extra Dominicales Diurnas y festivos (100%), 6am - 9:00pm; $11064
VhorasEDFN = ValorHT*2.5
#Valor Horas extra Dominicales Nocturnas (150%), 9pm - 5:59am; $13830
RecargoNOr = ValorHT * 1.35
#Recargo Nocturno Ordinario (35%), 9pm - 5:59am; $1936 + $5532 = $7468
VHorasOrdDFDiurnas = ValorHT * 1.75
#Valor Horas Ordinarias Domingos y Festivos Diurnas (75%), 6am - 9:00pm; $4149 + $5532 = $9618
VRecargoDFN = ValorHT * 2.1
#Valor Recargo Domingos y Festivos Ncoturnos(110%), 9pm - 5:59am; $11617
DescansoComp = 1.75 * ValorHT * 24
#Descanso compensatorio de 3 domingos trabajados
NumHorasextra = 5

print("Santiago Mendoza")
def nomina():
    nomina = ThorasT * ValorHT + NumHorasextra * VhorasED + VhorasEN + VhorasEDFD + VhorasEDFN + RecargoNOr + VHorasOrdDFDiurnas + VRecargoDFN + DescansoComp
    print(nomina)

nomina()