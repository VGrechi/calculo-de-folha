class HorasExtras:

    @staticmethod
    def calcularHE50(baseCalculo, cargaSemanal, quantHoras):
        valorHora = baseCalculo / (cargaSemanal * 5)
        return valorHora * quantHoras * 1.5

    @staticmethod
    def calcularHE75(baseCalculo, cargaSemanal, quantHoras):
        valorHora = baseCalculo / (cargaSemanal * 5)
        return valorHora * quantHoras * 1.75

    @staticmethod
    def calcularHE100(baseCalculo, cargaSemanal, quantHoras):
        valorHora = baseCalculo / (cargaSemanal * 5)
        return valorHora * quantHoras * 2