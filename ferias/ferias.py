from common.irrf import IRRF
from common.inss import INSS
from common.dsr import DSR
from common.horasextras import HorasExtras 
from common.adicionalnoturno import AdicionalNoturno
from common.holerite import Holerite

class Ferias:

    # https://www.calcule.net/trabalhista/calculo-de-ferias/#topnav

    @staticmethod
    def run():
        repetir = True
        while(repetir):
            # Entradas
            salario = float(input("Salário Bruto: ").replace(",", "."))
            numDependentes = int(input("Número de Dependentes: "))
            cargaSemanal = int(input("Carga Horária Semanal: "))
            horasExtras50 = float(input("Quantidade de HE no ano (50%): ").replace(",", "."))
            horasExtras75 = float(input("Quantidade de HE no ano (75%): ").replace(",", "."))
            horasExtras100 = float(input("Quantidade de HE no ano (100%): ").replace(",", "."))
            horasAdcNoturno = float(input("Quantidade de Horas Adicional Noturno no ano: ").replace(",", "."))
            insalubridade = float(input("Adicional Insalubridade: ").replace(",", "."))
            periculosidade = float(input("Adicional Periculosidade: ").replace(",", "."))
            numDias = int(input("Período de férias em dias: "))
            vendaDias = int(input("Venda de férias em dias: "))
            adiantamento = input("Adiantar 1ª Parcela 13º? (sim/nao) ")

            # Main
            holerite = Holerite()
            gozo = numDias / 30
            venda = vendaDias / 30
    
            valorHE50 = HorasExtras.calcularHE50(salario, cargaSemanal, horasExtras50)
            valorHE75 = HorasExtras.calcularHE75(salario, cargaSemanal, horasExtras75)
            valorHE100 = HorasExtras.calcularHE100(salario, cargaSemanal, horasExtras100)
            valorHAN = AdicionalNoturno.calcular(salario, cargaSemanal, horasExtras100)
            salario += insalubridade + periculosidade + valorHE50 + valorHE75 + valorHE100 + valorHAN

            # FERIAS
            ferias = salario * gozo
            holerite.insereItem("ferias", { "codigo": 5, "descricao": "Férias", "referencia": numDias, "proventos": ferias, "descontos": 0 })
            
            # BONUS FERIAS
            umTercoFerias = ferias / 3
            holerite.insereItem("umTercoFerias", { "codigo": 6, "descricao": "1/3 Férias", "referencia": numDias, "proventos": umTercoFerias, "descontos": 0 })
            
            # ABONO PECUNIARIO
            abonoPecuniario = salario * venda
            holerite.insereItem("abonoPecuniario", { "codigo": 7, "descricao": "Abono Pecuniário", "referencia": vendaDias, "proventos": abonoPecuniario, "descontos": 0 })

            # BONUS ABONO
            umTercoAbono = abonoPecuniario / 3
            holerite.insereItem("umTercoAbono", { "codigo": 8, "descricao": "1/3 Abono Pecuniário", "referencia": vendaDias, "proventos": umTercoAbono, "descontos": 0 })

            # INSS
            baseCalculoINSS = ferias + abonoPecuniario
            inss = INSS.calcular(baseCalculoINSS)
            inssRef = INSS.calcularRef(baseCalculoINSS)
            holerite.insereItem("inss", { "codigo": 101, "descricao": "INSS", "referencia": inssRef, "proventos": 0, "descontos": inss })

            # IRRF
            baseCalculoIRRF = ferias + abonoPecuniario - inss
            irrf = IRRF.calcular(baseCalculoIRRF, numDependentes)
            irrfRef = IRRF.calcularRef(baseCalculoIRRF, numDependentes)
            holerite.insereItem("irrf", { "codigo": 102, "descricao": "IRRF", "referencia": irrfRef, "proventos": 0, "descontos": irrf })

            if(adiantamento == "sim"):
                numMeses = int(input("Número de meses trabalhados: "))
                salarioProporcional = salario * numMeses / 12
                decimoTerceiro = salarioProporcional / 2
                holerite.insereItem("decimoTerceiro", { "codigo": 4, "descricao": "1ª Parcela 13º (Adiantamento)", "referencia": numMeses, "proventos": decimoTerceiro, "descontos": 0 })
           
            holerite.imprime()

            repetirStr = input("Deseja calcular novamente? (sim/nao) ")
            if(repetirStr == "nao"):
                repetir = False