from .irrf import IRRF
from .inss import INSS
from .dsr import DSR
from .horasextras import HorasExtras 
from .adicionalnoturno import AdicionalNoturno
from .pensao import Pensao
from .insalubridade import Insalubridade
from .periculosidade import Periculosidade
from common.holerite import Holerite

class FechamentoMensal:

    VALOR_DESC_DEPENDENTE = 189.59

    @staticmethod
    def run():
        VALOR_DESC_DEPENDENTE = FechamentoMensal.VALOR_DESC_DEPENDENTE

        repetir = True
        while(repetir):
            """
            ENTRADAS 
            """
            """
            salario = float(input("Salário Bruto: ").replace(",", ".")) 
            numDependentes = int(input("Número de Dependentes: "))
            cargaSemanal = int(input("Carga Horária Semanal: "))
            horasExtras50 = float(input("Quantidade de HE (50%): ").replace(",", "."))
            horasExtras75 = float(input("Quantidade de HE (75%): ").replace(",", "."))
            horasExtras100 = float(input("Quantidade de HE (100%): ").replace(",", "."))
            horasAdcNoturno = float(input("Quantidade de Horas Adicional Noturno: ").replace(",", "."))
            insalubridade = float(input("Adicional Insalubridade: ").replace(",", "."))
            periculosidade = float(input("Adicional Periculosidade: ").replace(",", "."))
            pensaoAlimenticia = float(input("Pensão Alimentícia: ").replace(",", "."))
            numDiasUteis = int(input("Dias úteis no Mês: "))
            numDiasNaoUteis = int(input("Dias de descanso no Mês: "))
            listaFaltas = input("Faltas (dd/MM/yyyy;dd/MM/yyyy): ").split(";")
            listaFeriados = input("Feriados (dd/MM/yyyy;dd/MM/yyyy): ").split(";")
            """
            
            salario = 4111.50
            numDependentes = 0
            cargaSemanal = 44
            horasExtras50 = 0
            horasExtras75 = 11.87
            horasExtras100 = 0
            horasAdcNoturno = 0
            insalubridade = 104.50
            periculosidade = 0
            pensaoAlimenticia = 0
            numDiasUteis = 24
            numDiasNaoUteis = 6
            listaFaltas = "13/04/2020".split(";")
            listaFeriados = "".split(";")
            

            """
            MAIN 
            """
            holerite = Holerite()
            holerite.insereItem("salarioMensal", { "codigo": 1, "descricao": "Salario Mensal", "referencia": 30, "proventos": salario, "descontos": 0 })

            insaRef = Insalubridade.calcularRef(insalubridade)
            holerite.insereItem("insalubridade", { "codigo": 6, "descricao": "Adicional Insalubridade", "referencia": insaRef, "proventos": insalubridade, "descontos": 0 })
            
            periRef = Periculosidade.calcularRef(periculosidade)
            holerite.insereItem("periculosidade", { "codigo": 7, "descricao": "Adicional Periculosidade", "referencia": periRef, "proventos": periculosidade, "descontos": 0 })

            baseCalculoHE = salario + insalubridade + periculosidade
            valorHE50 = HorasExtras.calculaHE50(baseCalculoHE, cargaSemanal, horasExtras50)
            holerite.insereItem("horasExtras50", { "codigo": 2, "descricao": "Horas Extras 50%", "referencia": horasExtras50, "proventos": valorHE50, "descontos": 0 })

            valorHE75 = HorasExtras.calculaHE75(baseCalculoHE, cargaSemanal, horasExtras75)
            holerite.insereItem("horasExtras75", { "codigo": 3, "descricao": "Horas Extras 75%", "referencia": horasExtras75, "proventos": valorHE75, "descontos": 0 })

            valorHE100 = HorasExtras.calculaHE100(baseCalculoHE, cargaSemanal, horasExtras100)
            holerite.insereItem("horasExtras100", { "codigo": 4, "descricao": "Horas Extras 100%", "referencia": horasExtras100, "proventos": valorHE100, "descontos": 0 })

            valorHAN = AdicionalNoturno.calcular(baseCalculoHE, cargaSemanal, horasAdcNoturno)
            holerite.insereItem("horasAdcNoturno", { "codigo": 5, "descricao": "Horas Adicional Noturno", "referencia": horasAdcNoturno, "proventos": valorHAN, "descontos": 0 })

            valorHE = valorHE50 + valorHE75 + valorHE100
            quantHE = horasExtras50 + horasExtras75 + horasExtras100
            dsrProv = DSR.calcularProventos(valorHE, numDiasUteis, numDiasNaoUteis)
            dsrProvRef = quantHE
            holerite.insereItem("dsrProv", { "codigo": 8, "descricao": "DSR Horas Extras", "referencia": dsrProvRef, "proventos": dsrProv, "descontos": 0 })

            baseCalculoDSR = salario + valorHE + valorHAN + insalubridade + periculosidade + dsrProv
            dsrDesc = DSR.calcularDescontos(salario, listaFaltas, listaFeriados)
            dsrDescRef = DSR.calcularDescontosRef(listaFaltas, listaFeriados)
            holerite.insereItem("dsrDesc", { "codigo": 9, "descricao": "DSR Faltas", "referencia": dsrDescRef, "proventos": 0, "descontos": dsrDesc })

            pensaoRef = Pensao.calcularRef(pensaoAlimenticia)
            holerite.insereItem("pensao", { "codigo": 10, "descricao": "Pensão Alimentícia", "referencia": pensaoRef, "proventos": 0, "descontos": pensaoAlimenticia })
            
            baseCalculoINSS = salario + valorHE + valorHAN + insalubridade + periculosidade + dsrProv - dsrDesc
            inss = INSS.calcular(baseCalculoINSS)
            inssRef = INSS.calcularRef(baseCalculoINSS)
            holerite.insereItem("inss", { "codigo": 11, "descricao": "INSS", "referencia": inssRef, "proventos": 0, "descontos": inss })

            baseCalculoIRRF = salario - inss - (numDependentes * VALOR_DESC_DEPENDENTE)
            irrf = IRRF.calcular(baseCalculoIRRF, numDependentes)
            irrfRef = IRRF.calcularRef(baseCalculoIRRF)
            holerite.insereItem("irrf", { "codigo": 12, "descricao": "IRRF", "referencia": irrfRef, "proventos": 0, "descontos": irrf })

            holerite.imprime()

            repetirStr = input("Deseja calcular novamente? (sim/nao) ")
            if(repetirStr == "nao"):
                repetir = False