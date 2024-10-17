class Usuario:
    def __init__(self, id, nome, senha, status):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.status = status

u1 = Usuario(1, "renan", '123', "admin")
u2 = Usuario(2, "cleiton", '321', "user")
lista = [u1, u2]

def verifc_senha(usuario, sen):
    ident = 0
    for i in lista:
        if i.nome == usuario and i.senha == sen:
            ident = 1
            break
    return ident

def verifc_admin(usuario):
    ident_1 = 0
    for i in lista:
        if i.nome == usuario and i.status == 'admin':
            ident_1 = 1
            break
    return ident_1
            
    

