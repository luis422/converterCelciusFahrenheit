opcao = "c"
while opcao == "c" or opcao == "f":
    opcao = str(input("Vai converter o valor para fahrenheit ou celsius? [f/c]: "))
    if opcao == "c":
        valor = float(input("Digite o valor em fahrenheit: "))
        a = input(f"{valor}ºF são {5*(valor-32)/9}ºC\n[Enter para sair, c para converter novamente]: ")
    elif opcao == "f":
        valor = float(input("Digite o valor em celsius: "))
        b = input(f"{valor}ºC são {valor*9/5+32}ºF\n[Enter para sair, c para converter novamente]: ")