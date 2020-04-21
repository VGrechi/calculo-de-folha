from datetime import datetime

class DateUtils:

    @staticmethod
    def converteStringParaData(listaDatas):
        listaDatas = map(lambda f: datetime.strptime(f, "%d/%m/%Y"), listaDatas)
        listaDatas = sorted(listaDatas)
        return listaDatas
       

    @staticmethod
    def estaoNaMesmaSemana(data1, data2):
        lista = sorted([data1, data2])
        atual = lista[0]
        proximo = lista[1]

        datediff = (proximo - atual).days
        if datediff <= 7:
            if proximo.weekday() > atual.weekday():
                return True