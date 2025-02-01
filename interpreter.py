def texto_para_brainfuck(texto):
    bf_code = ""
    valor_atual = 0
    for char in texto:
        valor_char = ord(char)  # Pega o valor ASCII do caractere
        diferenca = valor_char - valor_atual
        if diferenca > 0:
            bf_code += '+' * diferenca
        elif diferenca < 0:
            bf_code += '-' * (-diferenca)
        bf_code += '.'  # Imprime o caractere
        valor_atual = valor_char
    return bf_code

texto = input("Digite o texto: ")
codigo_bf = texto_para_brainfuck(texto)
print("Código Brainfuck gerado:")
print(codigo_bf)