class HorasExtras:

    @staticmethod
    def calculaHE50(baseCalculo, cargaSemanal, quantHoras):
        valorHora = baseCalculo / (cargaSemanal * 5)
        return round(valorHora * quantHoras * 1.5, 2)

    @staticmethod
    def calculaHE75(baseCalculo, cargaSemanal, quantHoras):
        valorHora = baseCalculo / (cargaSemanal * 5)
        return round(valorHora * quantHoras * 1.75, 2)

    @staticmethod
    def calculaHE100(baseCalculo, cargaSemanal, quantHoras):
        valorHora = baseCalculo / (cargaSemanal * 5)
        return round(valorHora * quantHoras * 2, 2)