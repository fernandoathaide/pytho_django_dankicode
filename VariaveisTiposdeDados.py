"""
    AULA 02 NÚMEROS
        Tipos de números embutidos
        int - inteiros [-3,-2,-1,0,1,2,3]"
        Float [-3.2, -2.1, -1.0, 0.0, 1.0, 2.1, 3.2]
        Complex [1+2j, 1-2j] Conjunto de números complexos Usados nas áreas de engenharia e física
        Bool [True, False] - Booleano"
        Decimal [Decimal('0.1')] - Decimal
        Fraction [Fraction(1,3)] - Fração
        math.inf - Infinito
        math.nan - Not a Number
        math.pi - Pi
        math.e - Constante de Euler
        math.tau - Tau
        math.inf - Infinito

    AULA 03 VARIÁVEIS
        Variáveis são usadas para armazenar valores
        x = 5 # x é uma variável do tipo int
        y = "Hello, World!" # y é uma variável do tipo string
        print(x) # Imprime o valor de x
        print(y) # Imprime o valor de y
        Variáveis não precisam ser declaradas com qualquer tipo e podem até mudar de tipo após terem sido definidas
        x = 4 # x é do tipo int
        x = "Sally" # x é do tipo str

        Pytho é case-sensitive altura, Altura e ALTURA são três variáveis diferentes
        h,j,l = 1,2,3 # Atribuição múltipla
            print(h) # Imprime o valor de h => 1
            print(j) # Imprime o valor de j => 2
            print(l) # Imprime o valor de l => 3

        Variáveis Globais
            Variáveis globais podem ser usadas por qualquer função.
            Variáveis locais são criadas quando a função é chamada e excluídas quando a função é concluída.

                x = "awesome" # Variável global
                def myfunc():
                    x = "fantastic" # Variável local
                    print("Python is " + x)
                myfunc()
                print("Python is " + x)

"""