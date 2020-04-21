class IRRF:

    FAIXAS = [1903.98, 2826.65, 3751.05, 4664.68]

    @staticmethod
    def calcular(baseCalculo, numDependentes):
        FAIXAS = IRRF.FAIXAS
        imposto = 0

        if (baseCalculo > FAIXAS[0]):
            faixa = baseCalculo - FAIXAS[0]
            if faixa > (FAIXAS[1] - FAIXAS[0]):
                faixa = (FAIXAS[1] - FAIXAS[0])
            imposto += faixa * 0.075
        
        if (baseCalculo > FAIXAS[1]):
            faixa = baseCalculo - FAIXAS[1]
            if faixa > (FAIXAS[2] - FAIXAS[1]):
                faixa = (FAIXAS[2] - FAIXAS[1])
            imposto += faixa * 0.15
        
        if (baseCalculo > FAIXAS[2]):
            faixa = baseCalculo - FAIXAS[2]
            if faixa > (FAIXAS[3] - FAIXAS[2]):
                faixa = (FAIXAS[3] - FAIXAS[2])
            imposto += faixa * 0.225
        
        if (baseCalculo > FAIXAS[3]):
            faixa = baseCalculo - FAIXAS[3]
            imposto += faixa * 0.275

        return round(imposto, 2)

    @staticmethod
    def calcularRef(baseCalculo):
        FAIXAS = IRRF.FAIXAS
        if baseCalculo <= FAIXAS[0]:
            return 0
        
        if (baseCalculo > FAIXAS[0] and baseCalculo <= FAIXAS[1]):
            return 7.5

        if (baseCalculo > FAIXAS[1] and baseCalculo <= FAIXAS[2]):
            return 15

        if (baseCalculo > FAIXAS[2] and baseCalculo <= FAIXAS[3]):
            return 22.5

        if (baseCalculo > FAIXAS[3]):
            return 27.5