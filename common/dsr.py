from utils.dateutils import DateUtils

class DSR:

    @staticmethod
    def calcularProventos(valorHE, numDiasUteis, numDiasNaoUteis):
        proventos = valorHE * numDiasNaoUteis / numDiasUteis
        return round(proventos, 2)

    @staticmethod
    def calcularDescontos(baseCalculo, listaFaltas, listaFeriados):
        numSemanas = DSR.calcularDescontosRef(listaFaltas, listaFeriados)

        valorDia = baseCalculo / 30
        return round(valorDia * numSemanas, 2)

    @staticmethod
    def calcularDescontosRef(listaFaltas, listaFeriados):
        numFaltas = len(listaFaltas)
        numFeriados = len(listaFeriados)

        try:
            listaFaltas = DateUtils.converteStringParaData(listaFaltas)
        except:
            return 0

        try:
            listaFeriados = DateUtils.converteStringParaData(listaFeriados)
        except:
            return 0
     
        mesmaSemana = 0
        feriados = 0
        novaListaFaltas = []

        for i in range(numFaltas - 1):
            proximo = listaFaltas[i + 1]
            atual = listaFaltas[i]

            if (DateUtils.estaoNaMesmaSemana(atual, proximo)):
                mesmaSemana += 1

                if(atual in novaListaFaltas):
                    novaListaFaltas.remove(atual)

            novaListaFaltas.append(proximo)

        numSemanas = len(novaListaFaltas)
        for i in range(numSemanas):
            atual = novaListaFaltas[i]

            for j in range(numFeriados):
                if (DateUtils.estaoNaMesmaSemana(atual, listaFeriados[j])):
                    feriados += 1

        return numFaltas + feriados - mesmaSemana
   