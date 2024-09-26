#importar biblioteca
import calendar

#usuário informa o mês e ano desejados
mes = int(input("Informe o número do mês desejado: "))
ano = int(input("Informe o ano desejado: "))

if mes > 0 and mes <= 12:
    print(calendar.month(ano, mes))
else:
    print("Mês inválido!")