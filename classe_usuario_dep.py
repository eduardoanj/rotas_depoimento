import MySQLdb

class UsuarioDepoimento:
    def __init__(self):
        self.__id = 0
        self.__nome = nome
        self.__depoimento = depoimento

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id    
    
    @property
    def nome(self):
        return self.__nome

    @id.setter
    def nome(self, nome):
        self.__id = id    

    @property
    def depoimento(self):
        return self.__depoimento

    @id.setter
    def depoimento(self, depoimento):
        self.__depoimento = depoimento       


##### mudar o host ####### NÃO ESQUECER 
def salvar_depoimento_db(usuario:UsuarioDepoimento):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO depoimento (nome, depoimento) VALUES ('{}', '{}')"
    .format(usuario.nome, usuario.depoimento))
    conexao.commit()
    conexao.close()     

########## LISTA O PLANO DO USUARIO NA TABELA ASSOCIADOS ##########
def listar_depoimentos_usuario_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM depoimentos") 
    lista_depoimentos= []
    for p in cursor.fetchall():
        depoimento = UsuarioDepoimento()
        depoimento.id = p[0]
        depoimento.nome = p[1]
        depoimento.depoimento = p[2]        
        lista_depoimentos.append(depoimento)

    conexao.close()
    return lista_depoimentos 

########## DELETAR DEPOIMENTO DO DB ##########
def deletar_depoimento(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM PLANO_ITEN WHERE ID_ITEN = {}".format(id))
    conexao.commit()
    cursor.execute("DELETE FROM ITENS WHERE ID = {}".format(id))
    conexao.commit()
    conexao.close()        
           