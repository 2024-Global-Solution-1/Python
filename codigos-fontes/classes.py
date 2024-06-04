class novaOng():
    def __init__(self, nm, sigla, dtFund, missVis, end, email,redes, web = "Não tem"):
        self.nome = nm
        self.sigla = sigla
        self.dataFundacao = dtFund
        self.missaoEvisao = missVis
        self.endereco = end
        self.email = email
        self.redesSociais = redes
        self.webSite = web



class User():
    def __init__(self,user, nm, tele, idade, end, email, senha):
        self.username = user
        self.nome = nm
        self.telefone = tele
        self.idade = idade
        self.endereco = end
        self.email = email
        self.senha = senha