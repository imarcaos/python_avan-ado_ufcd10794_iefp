Exercícios e trabalhos da UFCD 10794 - Programação Avançada comPython
# Programação Avançada com PythonPython


## Formação do IEFP da Ação: 23328 - UFCD 10794 - Programador de Informática 


Lista de exercícios, tarefas e trabalhos que tivemos de fazer durante as aulas
Os códigos estão divididos por Aulas ex.: Aula1, Aula2, ...
Sempre que houver enunciados, estarão juntamente com o código.

### Aula 1 - 2024-09-19
- continuação do trabalho da ufcd anterior

### Aula 2 - 2024-09-27
- Apresentação da ufcd e conteúdo programático
- Tratamento idiomático de dados
- PEP (Python Enhancement Proposal)
- Formatação de string f-string, %, format(...)

### Aula 3 - 2024-10-01
- Revisão aula anterior:
    - falsy e truthy
- o in em um dicionário só lê a chave (1,2,3,...)
    - {1: "one", 2: "two", 3: "three",...}

- Aula de hoje:
- Classe e Objetos
- Herança - superclasse (mãe) subclasse(filho)

### Aula 4 - 2024-10-02
- Vídeo explicando sobre heranças: Pai, Mãe, filhos ....
    - vídeo 1 -  https://www.youtube.com/watch?v=ttMX3Ns_0oY
    - vídeo 2 - https://www.youtube.com/watch?v=3JANS2yxizs

- MRO (Method Resolution Order) - método que escolhe o primeiro da ordem da herança.
    - ex: filho (pai, mae) -> o pai esta primeiro, herda do método dele

### Aula 5 - 2024-10-08
- classes publica e privadas
    - protegido leva um '_' underscore antes da variável, métodos, ex.: _nome
    - privado leva dois'__' underscores antes das variável, métodos, ex.: __nif

### Aula 6 - 2024-10-09
- classes privadas e protegidas
- decoradores @staticmethod
- trabalho 2 para entregar até o dia 14
    - Nome: Informações Automóveis
    - sobre classes, construtores e métodos

### Aula 7 - 2024-10-11
- 1 hora para resolução do exercício 2 (já terminei na aula passada, aproveito para outro estudo)
- variável global e local
    - o global antes da variável indica que ela é global, ex: global variavel_global2
    - Quando usamos o termo global em uma variável dentro de outra função conseguimos modificá-lo
- Âmbito em funções *arg e **kwargs
    - unpacking operators (* e **)
    - 2 asteriscos "**" pode ser utilizado em dicionários
- Decoradores '@'
    - ex.: temos 2 funções e metemos o decorador imediatamente antes da função2 com o @função1, ele irá chamar primeiro a função 1 antes de executar a função 2.

- Serialialization e deserialization pág.94
    - Cria um serialização de informação que podem funcionar em outras linguagens, exemplo o Json
    - Pickle, ex. pickle.dump(objx, ficheiro) e pickle.load(file)
    - pip install jsonpickle
- Teste, registo e depuração pág.110
    - Try, Except
- Metaprogramação, programação dinâmica
    - Metaclasse
