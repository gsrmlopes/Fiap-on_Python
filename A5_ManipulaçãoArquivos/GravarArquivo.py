with open("./A5_ManipulaçãoArquivos/teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.\n")

with open("./A5_ManipulaçãoArquivos/teste.txt", "a") as arquivo:
    arquivo.write("Continuação do texto.")

with open("./A5_ManipulaçãoArquivos/teste.txt", "r") as arquivo:
    conteudo=arquivo.readlines()
print("Tipo de dado da variável",type(conteudo))
print("Conteúdo do arquivo:",conteudo)