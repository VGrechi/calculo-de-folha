class Holerite:

    holerite = {}
    totalProventos = 0
    totalDescontos = 0

    def insereItem(self, item, valor):
        self.holerite.update({ item: valor})
        self.totalProventos += valor.get("proventos")
        self.totalDescontos += valor.get("descontos")

    def imprime(self):
        print("")
        print("--------------------------------------------------------------------------------------")
        print("| {:50}  {:>30} |".format("Trabalhador: 0001 - Julia Figueiredo", "DEMONSTRATIVO DE PAGAMENTO"))
        print("--------------------------------------------------------------------------------------")
        print("| {:<10} | {:<30} | {:<10} | {:<10} | {:<10} |".format("Código", "Descrição", "Referência", "Proventos", "Descontos"))
        print("--------------------------------------------------------------------------------------")
        for key in self.holerite.keys():
            registro = self.holerite.get(key)
            if registro.get("referencia") == 0: 
                continue
            print("| {:<10} | {:<30} | {:<10} | {:<10} | {:<10} |".format(registro.get("codigo"), registro.get("descricao"), registro.get("referencia"), registro.get("proventos"), registro.get("descontos")))
        print("--------------------------------------------------------------------------------------")
        print("| {:<28} {:>10} | {:<29} {:>10} |".format("TOTAL PROVENTOS", round(self.totalProventos, 2), "TOTAL DESCONTOS", round(self.totalDescontos, 2)))
        print("{:41} | {:<29} {:>10} |".format("", "LÌQUIDO A RECEBER", round(self.totalProventos - self.totalDescontos, 2)))
        print("--------------------------------------------------------------------------------------")