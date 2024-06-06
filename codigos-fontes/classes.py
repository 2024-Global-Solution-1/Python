class Dados():
    def __init__(self, nm, endereco, tele, em, sen):
        self.nome = nm
        self.endereco = endereco
        self.telefone = tele
        self.email = em
        self.senha = sen



class NovaOng(Dados):
    def __init__(self, sigla, dtFund, missVis,nome,ende,telefone,email,web,senha):
        super().__init__(nm = nome, endereco = ende, tele=telefone, em=email, sen=senha)
        self.sigla = sigla
        self.dataFundacao = dtFund
        self.missaoEvisao = missVis
        self.email = email
        self.web = web



class User(Dados):
    def __init__(self,user, idade, senha, nome, ende, telefone, email):
        super().__init__(nm = nome, endereco = ende, tele=telefone, em=email,sen=senha)
        self.username = user
        self.idade = idade


class Empresa(Dados):
    def __init__(self, nome, ende, telefone, email,senha, tipo, pessoaContato):
        super().__init__(nm = nome, endereco = ende, tele=telefone, em=email, sen=senha)
        self.tipo = tipo
        self.pessoaDeContato = pessoaContato
