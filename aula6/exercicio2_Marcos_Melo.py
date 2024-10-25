'''
Aula 6 - 2024-10-09
@author: Marcos Melo
Exercício 2 - Classes
'''

# Classe Automóveis
class Auto:
    # Atributo estatico e protegido
    _fraseAuto = "MarCAr possui os Melhores Automoveis para si!"

    # Construtor
    def __init__(self, marca, modelo, ano, matricula):
        # instanciando os atributos as variáveis
        self.marca = marca 
        self.modelo = modelo
        self.__logo = 'sim' # atributo privado
        self.ano = ano
        self.matricula = matricula

    # Métodos de retorno
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo
    
    def getLogo(self):
        return self.__logo

    def getAno(self):
        return self.ano
    
    def getMatricula(self):
        return self.matricula

    # Métodos para inserir valores
    def setAge(self, age):
        self.age = age

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setLogo(self, logo):
        self.__logo = logo

    def setAno(self, ano):
        self.ano = ano
    
    def setMatricula(self, matricula):
        self.matricula = matricula

    # Imprime todas as informações do Automóvel
    def printInfo(self):
        print("\n######### INFO AUTOMOVEL #########")
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nLogo: {self.__logo}\nAno: {self.ano}\nMatricula: {self.matricula}")

    # Metodo estático que retorna o valor do atributo estático
    @staticmethod
    def bestAutoFrase():
        return Auto._fraseAuto
    

# Classe Tipo Automovel
class AutoType(Auto):
    # Construtor
    def __init__(self, marca, modelo, ano, matricula, combustivel):
        super().__init__(marca, modelo, ano, matricula)
        self.combustivel = combustivel
        self.caixa_automatica = 'sim'

    # Métodos de retorno
    def getCombustivel(self):
        return self.combustivel

    def getCaixaAutomatica(self):
        return self.modelo
    
    # Métodos para inserir valores
    def setCombustivel(self, combustivel):
        self.combustivel = combustivel

    def setCaixaAutomatica(self, cx_auto):
        self.caixa_automatica = cx_auto

    # Imprime todas as informações adicionais do Automóvel
    def printInfo(self):
        super().printInfo()
        print(f"Combustivel: {self.combustivel}\nCaixa Automatica: {self.caixa_automatica}") 

# Método Main para organizar os testes
def main():
    # Instanciando os objetos
    auto1 = Auto("Volkswagem", "T-Rock", 2024, "88-AA-99" )
    auto1.printInfo()

    # Modificando e apresentando o atributo privado através do método interno da classe Super
    auto1.setLogo('nao')
    print("\nAlteracao do atributo privado logo 'nao' atraves um metodo publico")
    auto1.printInfo()

    auto2 = AutoType("Pegeout", "3008", 2024, "AA-00-AA", "Eletrico" )
    auto2.printInfo()

    ## Testes dos Métodos Estáticos
    print("\n---------------")
    # Chamando o método estático através da classe
    print("\nMetodo estatico por classe: ", Auto.bestAutoFrase())

    # Chamando o método estático por um objeto da classe
    objeto = Auto
    print("\nMetodo estatico por objeto: ", objeto.bestAutoFrase())    

    '''
    As duas formas a seguir, não são a melhor forma de acessar o atributo protegido,
    serve apenas a título de demonstração do exercício
    '''
    # Acessando o atributo da classe através da classe    
    print("\nAtributo estatico por classe: ", Auto._fraseAuto)

    # Acessando o atributo da classe por um objeto
    print("\nAtributo estatico por objeto: ", objeto._fraseAuto)

# executa a função main
main()