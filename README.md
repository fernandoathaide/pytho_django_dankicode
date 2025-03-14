# Python e Django Frameworks
Python é uma linguagem interpretada de alto nível, tipada, dinâmica e OO. Django Framework é uma estrutura da web de código aberto escrito em python, arquitetura Model-Template-View (MTV). Dividido em: 01 - Classes de interface de banco de dados (MODEL), classes de processamento de solicitações (VIEW) e modelos para a apresentação final (modelo template). FrameWork Focado para o desenvolvimento WEB programado em Python utilizado pelo Pinterest, Instagram, Mozilla e Blender (Software de modelagem 3D para desenvolvimento de jogos).

# IDE ::

    Python colab da Google
    Visual Studio Code
    Python 3.9.21
        #❯ python --version
            Python 3.9.21
        #❯ python3 --version
            Python 3.10.12
        #❯ pip --version ou(pip3 --version)
            pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)

# Erros::

## Correção do Conflito entre VS Code e XAMPP no Linux
    A instalação simultânea do VS Code e do XAMPP no Linux estava causando um conflito no uso de bibliotecas. O VS Code tentava carregar as bibliotecas do XAMPP, resultando em erros ao abrir a IDE.
## Solução
    Para corrigir o problema, foi necessário renomear as bibliotecas conflitantes do XAMPP e atualizar o cache das bibliotecas do sistema. Os seguintes comandos foram executados:
        sudo mv /opt/lampp/lib/libfreetype.so.6.bkp /opt/lampp/lib/libfreetype.so.6
        sudo mv /opt/lampp/lib/libfreetype.so.bkp /opt/lampp/lib/libfreetype.so

        sudo mv /opt/lampp/lib/libexpat.so.1 /opt/lampp/lib/libexpat.so.1.bkp
        sudo mv /opt/lampp/lib/libexpat.so /opt/lampp/lib/libexpat.so.bkp

        sudo ldconfig //E atualizar as bibliotecas do sistema
    * Após esses ajustes, o VS Code passou a abrir normalmente, sem conflitos com as bibliotecas do XAMPP.