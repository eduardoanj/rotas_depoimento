import MySQLdb

class UsuarioDepoimento:
    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__depoimento = ''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id    
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome    

    @property
    def depoimento(self):
        return self.__depoimento

    @depoimento.setter
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
    cursor.execute("SELECT * FROM depoimento") 
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
    cursor.execute("DELETE FROM depoimento WHERE id = {}".format(id))
    conexao.commit()
    conexao.close()        

#### salvar depoimento para o publico ###          

def salvar_depoimentopub(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO depoimentopublico (id, nome, depoimento) "
    +"SELECT id, nome, depoimento FROM depoimento WHERE id = {}".format(id))
    conexao.commit()
    conexao.close()    

def listar_depoimentos_usuariopub_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM depoimentopublico") 
    lista_depoimentos= []
    for p in cursor.fetchall():
        depoimento = UsuarioDepoimento()
        depoimento.id = p[0]
        depoimento.nome = p[1]
        depoimento.depoimento = p[2]        
        lista_depoimentos.append(depoimento)

    conexao.close()
    return lista_depoimentos 