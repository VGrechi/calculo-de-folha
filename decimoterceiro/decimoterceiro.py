from common.irrf import IRRF
from common.inss import INSS
from common.horasextras import HorasExtras 
from common.adicionalnoturno import AdicionalNoturno
from common.holerite import Holerite

class DecimoTerceiro:

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
            numMeses = int(input("Número de meses trabalhados: "))
            adiantamento = float(input("Valor da 1ª Parcela (se já foi paga): ").replace(",", "."))

            # Main
            holerite = Holerite()
            proporcao = numMeses / 12

            valorHE50 = HorasExtras.calcularHE50(salario, cargaSemanal, (horasExtras50 / numMeses))
            valorHE75 = HorasExtras.calcularHE75(salario, cargaSemanal, (horasExtras75 / numMeses))
            valorHE100 = HorasExtras.calcularHE100(salario, cargaSemanal, (horasExtras100 / numMeses))
            valorHAN = AdicionalNoturno.calcular(salario, cargaSemanal, (horasExtras100 / numMeses))
            salario += insalubridade + periculosidade + valorHE50 + valorHE75 + valorHE100 + valorHAN

            if(adiantamento == 0):
                # PRIMEIRA PARCELA - ADIANTAMENTO
                salarioProporcional = salario * proporcao
                decimoTerceiro = salarioProporcional / 2
                holerite.insereItem("decimoTerceiro", { "codigo": 2, "descricao": "1ª Parcela 13º", "referencia": numMeses, "proventos": decimoTerceiro, "descontos": 0 })
            else:
                salarioProporcional = salario * proporcao
               
                # SEGUNDA PARCELA
                decimoTerceiro = salarioProporcional - adiantamento
                holerite.insereItem("decimoTerceiro", { "codigo": 3, "descricao": "2ª Parcela 13º", "referencia": numMeses, "proventos": decimoTerceiro, "descontos": 0 })

                # INSS
                baseCalculoINSS = salarioProporcional
                inss = INSS.calcular(baseCalculoINSS)
                inssRef = INSS.calcularRef(baseCalculoINSS)
                holerite.insereItem("inss", { "codigo": 101, "descricao": "INSS", "referencia": inssRef, "proventos": 0, "descontos": inss })

                # IRRF
                baseCalculoIRRF = salarioProporcional - inss
                irrf = IRRF.calcular(baseCalculoIRRF, numDependentes)
                irrfRef = IRRF.calcularRef(baseCalculoIRRF, numDependentes)
                holerite.insereItem("irrf", { "codigo": 102, "descricao": "IRRF", "referencia": irrfRef, "proventos": 0, "descontos": irrf })

            holerite.imprime()

            repetirStr = input("Deseja calcular novamente? (sim/nao) ")
            if(repetirStr == "nao"):
                repetir = False
