def niver():
  while True:
    try:
      ano = int(input("Digite sua data de nascimento entre 1922 e 2021: "))
      if 1922 <= ano <= 2021:
        return ano
      else:
        print(
            "Ano inválido, tente novamente digitando o ano dentro do intervalo!"
        )
    except ValueError:
      print("Ano inválido, tente novamente!")


nome = input("Digite seu nome completo: ")

nascimento = niver()

hoje = 2022
idade = hoje - nascimento

print("Olá", nome)
print("Sua idade é: ", idade)
