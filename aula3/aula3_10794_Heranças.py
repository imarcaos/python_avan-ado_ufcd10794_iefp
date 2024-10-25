class Pessoa:
    #contrutor
    def __init__(self,nome,idade,sexo, nacionalidade, localidade):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.nacionalidade = nacionalidade
        self.localidade = localidade
    #Definição dos métodos
    def get_nome(self):
        return {self.nome}
    def get_sexo(self):
        return f"Eu sou do sexo {self.sexo}"
    def get_idade(self):
        return f"Eu tenho {self.idade} anos"
    def altera_idade(self,idade):
        self.idade = idade
        print(f"Eu passei a ter esta idade {self.idade}")
    def altera_nome(self,nome):
        self.nome = nome
        print(f"Eu agora chamo-me {self.nome}")

#Definição da classe
class Estudante(Pessoa):
    #COnstrutor
    def __init__(self,nome,idade,sexo, nacionalidade, localidade, nr_aluno,nome_curso, turma, estabelecimento):
        super().__init__(nome,idade, sexo, nacionalidade, localidade)
        #definição dos atributos específicos do objeto tipo estudante
        self.nr_aluno = nr_aluno
        self.nome_curso = nome_curso
        self.turma = turma
        self.estabelecimento = estabelecimento
    # Definição métodos
    def show_aluno(self):
        print(f"""Eu sou o aluno {self.nome}, 
              e tenho estas características como estudante:""")
        print(f""" Nr de aluno: {self.nr_aluno}
              Turma: {self.turma } 
              Nome do curso: {self.nome_curso} 
              Escola: {self.estabelecimento} 
            """)
    def altera_nome(self, nome):
        self.nome = nome
        print(f"Eu sou estudante e por isso tive de mudar de nome: {self.nome}")

class Atleta(Estudante):
    #Construtor
    def __init__(self, nome, idade, sexo, nacionalidade, localidade, nr_aluno,nome_curso, turma, estabelecimento, modalidade):
        super().__init__(nome,idade, sexo, nacionalidade, localidade, nr_aluno,nome_curso, turma, estabelecimento)
        self.modalidade = modalidade   

#instanciação de objetos
# p1=Pessoa('Fátima',45,'feminino','portuguesa','Lisboa')
# print(p1.get_nome(),p1.get_idade())
# p1.altera_nome('Fátima Sousa')

# estudante1 = Estudante('Rafael',34,'Masculino','Espanhola','Madrid',1234,'Python','A',\
#                        'Escola Tecnológica de Madrid')
# estudante1.show_aluno()
# estudante1.altera_nome('Rafael Silva')
# estudante1.show_aluno()
atleta1 = Atleta('Duarte',20,'Masculino','Espanhola','Madrid',1234,'Python',\
                'A','Escola Tecnológica de Madrid','Vela')
print(atleta1.modalidade)
atleta1.get_nome()





