from common.irrf import IRRF
from common.inss import INSS
from common.dsr import DSR
from common.horasextras import HorasExtras 
from common.adicionalnoturno import AdicionalNoturno
from common.pensao import Pensao
from common.insalubridade import Insalubridade
from common.periculosidade import Periculosidade
from common.holerite import Holerite

class FechamentoMensal:

    @staticmethod
    def run():

        repetir = True
        while(repetir):
            # Entradas
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
        
            # Main
            holerite = Holerite()

            # SALÁRIO
            holerite.insereItem("salarioMensal", { "codigo": 1, "descricao": "Salario Mensal", "referencia": 30, "proventos": salario, "descontos": 0 })

            # INSALUBRIDADE
            insaRef = Insalubridade.calcularRef(insalubridade)
            holerite.insereItem("insalubridade", { "codigo": 9, "descricao": "Adicional Insalubridade", "referencia": insaRef, "proventos": insalubridade, "descontos": 0 })
            
            # PERICULOSIDADE
            periRef = Periculosidade.calcularRef(periculosidade)
            holerite.insereItem("periculosidade", { "codigo": 10, "descricao": "Adicional Periculosidade", "referencia": periRef, "proventos": periculosidade, "descontos": 0 })

            # HORAS EXTRAS 50%
            baseCalculoHE = salario + insalubridade + periculosidade
            valorHE50 = HorasExtras.calcularHE50(baseCalculoHE, cargaSemanal, horasExtras50)
            holerite.insereItem("horasExtras50", { "codigo": 11, "descricao": "Horas Extras 50%", "referencia": horasExtras50, "proventos": valorHE50, "descontos": 0 })

            # HORAS EXTRAS 75%
            valorHE75 = HorasExtras.calcularHE75(baseCalculoHE, cargaSemanal, horasExtras75)
            holerite.insereItem("horasExtras75", { "codigo": 12, "descricao": "Horas Extras 75%", "referencia": horasExtras75, "proventos": valorHE75, "descontos": 0 })

            # HORAS EXTRAS 100%
            valorHE100 = HorasExtras.calcularHE100(baseCalculoHE, cargaSemanal, horasExtras100)
            holerite.insereItem("horasExtras100", { "codigo": 13, "descricao": "Horas Extras 100%", "referencia": horasExtras100, "proventos": valorHE100, "descontos": 0 })

            # ADICIONAL NOTURNO
            valorHAN = AdicionalNoturno.calcular(baseCalculoHE, cargaSemanal, horasAdcNoturno)
            holerite.insereItem("horasAdcNoturno", { "codigo": 14, "descricao": "Horas Adicional Noturno", "referencia": horasAdcNoturno, "proventos": valorHAN, "descontos": 0 })

            # DSR PROVENTOS
            valorHE = valorHE50 + valorHE75 + valorHE100
            quantHE = horasExtras50 + horasExtras75 + horasExtras100
            dsrProv = DSR.calcularProventos(valorHE, numDiasUteis, numDiasNaoUteis)
            dsrProvRef = quantHE
            holerite.insereItem("dsrProv", { "codigo": 15, "descricao": "DSR Horas Extras", "referencia": dsrProvRef, "proventos": dsrProv, "descontos": 0 })

            # DSR DESCONTOS
            baseCalculoDSR = salario + valorHE + valorHAN + insalubridade + periculosidade + dsrProv
            dsrDesc = DSR.calcularDescontos(salario, listaFaltas, listaFeriados)
            dsrDescRef = DSR.calcularDescontosRef(listaFaltas, listaFeriados)
            holerite.insereItem("dsrDesc", { "codigo": 103, "descricao": "DSR Faltas", "referencia": dsrDescRef, "proventos": 0, "descontos": dsrDesc })

            # PENSÂO ALIMENTÍCIA
            pensaoRef = Pensao.calcularRef(pensaoAlimenticia)
            holerite.insereItem("pensao", { "codigo": 104, "descricao": "Pensão Alimentícia", "referencia": pensaoRef, "proventos": 0, "descontos": pensaoAlimenticia })

            # INSS
            baseCalculoINSS = salario + valorHE + valorHAN + insalubridade + periculosidade + dsrProv - dsrDesc
            inss = INSS.calcular(baseCalculoINSS)
            inssRef = INSS.calcularRef(baseCalculoINSS)
            holerite.insereItem("inss", { "codigo": 101, "descricao": "INSS", "referencia": inssRef, "proventos": 0, "descontos": inss })

            # IRRF
            baseCalculoIRRF = salario - inss
            irrf = IRRF.calcular(baseCalculoIRRF, numDependentes)
            irrfRef = IRRF.calcularRef(baseCalculoIRRF, numDependentes)
            holerite.insereItem("irrf", { "codigo": 102, "descricao": "IRRF", "referencia": irrfRef, "proventos": 0, "descontos": irrf })

            holerite.imprime()

            repetirStr = input("Deseja calcular novamente? (sim/nao) ")
            if(repetirStr == "nao"):
                repetir = False