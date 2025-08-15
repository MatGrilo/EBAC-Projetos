#!/usr/bin/env python3
import math

def ler_numero(prompt="Digite um número: "):
    while True:
        entrada = input(prompt).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido. Tente novamente (ex.: 12,5 ou 12.5).")

def normalizar_operacao(op_raw: str):
    op = op_raw.strip().lower()
    if op in {"+", "soma", "somar", "adicao", "adição"}: return ("+", "binaria")
    if op in {"-", "subtrair", "diminuir", "menos"}:     return ("-", "binaria")
    if op in {"*", "x", "multiplicar", "vezes"}:         return ("*", "binaria")
    if op in {"/", "dividir", "divisao", "divisão"}:     return ("/", "binaria")
    if op in {"^", "**", "potencia", "potência", "pow", "x^y"}: return ("^", "binaria")
    if op in {"%", "porc", "porcent", "porcentagem", "percentual", "pct"}: return ("%", "binaria")
    if op in {"!", "fatorial", "fat"}:                   return ("!", "unaria")
    if op in {"sqrt", "raiz", "raiz quadrada"}:          return ("sqrt", "unaria")
    if op in {"log", "ln", "logn"}:                      return ("log", "unaria")
    if op in {"limpar", "c", "clear", "reset"}:          return ("limpar", "controle")
    if op in {"sair", "q", "exit"}:                      return ("sair", "controle")
    if op in {"ajuda", "help", "?"}:                     return ("ajuda", "controle")
    return (None, None)

def aplicar_binaria(atual: float, op: str, b: float):
    if op == "+": return atual + b, None
    if op == "-": return atual - b, None
    if op == "*": return atual * b, None
    if op == "/":
        if b == 0: return atual, "Erro: divisão por zero."
        return atual / b, None
    if op == "%": return atual * (b / 100.0), None
    if op == "^":
        if atual < 0 and not float(b).is_integer():
            return atual, "Erro: com base negativa, o expoente deve ser inteiro (reais)."
        try:
            return atual ** b, None
        except ZeroDivisionError:
            return atual, "Erro: 0 elevado a expoente negativo é indefinido."
        except OverflowError:
            return atual, "Erro: resultado muito grande (overflow)."
        except ValueError as e:
            return atual, f"Erro: {e}"
    return atual, "Operação binária desconhecida."

def aplicar_unaria(atual: float, op: str):
    if op == "!":
        if atual < 0 or not float(atual).is_integer():
            return atual, "Erro: fatorial requer inteiro ≥ 0."
        return float(math.factorial(int(atual))), None
    if op == "sqrt":
        if atual < 0: return atual, "Erro: raiz quadrada de número negativo."
        return math.sqrt(atual), None
    if op == "log":
        if atual <= 0: return atual, "Erro: log definido apenas para positivos."
        return math.log(atual), None
    return atual, "Operação unária desconhecida."

def mostrar_menu():
    print("\nOperações disponíveis:")
    print("  +  soma (binária)          |   %    porcentagem: atual * (p/100)")
    print("  -  diminuir (binária)      |   !    fatorial (do valor atual)")
    print("  *  multiplicar (binária)   |   sqrt raiz quadrada (do atual)")
    print("  /  dividir (binária)       |   log  log natural (ln) do atual")
    print("  ^  potência x^y (binária)")
    print("Comandos: limpar, sair, ajuda\n")

def main():
    print("=== Calculadora Interativa ===")
    mostrar_menu()
    valor_atual = None
    while True:
        if valor_atual is None:
            valor_atual = ler_numero("Digite o primeiro número: ")
        print(f"\nValor atual: {valor_atual:g}")
        op_raw = input("Escolha uma operação (ou 'limpar' / 'sair' / 'ajuda'): ")
        op, tipo = normalizar_operacao(op_raw)
        if op is None:
            print("Operação/comando não reconhecido. Digite 'ajuda' para ver as opções.")
            continue
        if tipo == "controle":
            if op == "limpar":
                valor_atual = None
                print("→ Calculadora reiniciada.")
            elif op == "sair":
                print("Até mais!")
                return
            elif op == "ajuda":
                mostrar_menu()
            continue
        if tipo == "binaria":
            b = ler_numero("Digite o próximo número: ")
            novo, erro = aplicar_binaria(valor_atual, op, b)
        else:
            novo, erro = aplicar_unaria(valor_atual, op)
        if erro:
            print(erro)
        else:
            valor_atual = novo
            print(f"= {valor_atual:g}")

if __name__ == "__main__":
    main()
12