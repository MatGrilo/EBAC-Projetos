# EBAC-Projetos
Projetos feitos durante o curso 
## Visão rápida do código (Calculadora em Python)

**O que é:** calculadora de terminal que mantém um **valor atual** e permite **encadear operações**.

### Fluxo (em 5 passos)
1) Lê o **primeiro número**.  
2) Usuário escolhe **operação**.  
3) Se **binária** (`+ - * / % ^`), pede o **próximo número**.  
4) Se **unária** (`! sqrt log`), aplica direto no valor atual.  
5) Mostra o resultado e repete; `limpar` reinicia, `sair` encerra.

### Funções (1-liners)
- `main()` — loop principal de interação.  
- `ler_numero()` — leitura com validação (aceita `,` ou `.`).  
- `normalizar_operacao()` — mapeia entrada → `(código, tipo)` com **sinônimos** (`somar/+`, `dividir//`, `potência/^, **, pow` etc.).  
- `aplicar_binaria()` — executa `+ - * / % ^` e trata erros.  
- `aplicar_unaria()` — executa `! sqrt log` e valida domínio.  
- `mostrar_menu()` — imprime ajuda.

### Operações
- **Binárias:** `+` soma, `-` subtração, `*` multiplicação, `/` divisão,  
  `%` porcentagem → `valor_atual * (p/100)`, `^` potência `x^y`.  
- **Unárias:** `!` fatorial (inteiro ≥ 0), `sqrt` raiz (≥ 0), `log` ln (> 0).  
- **Comandos:** `limpar`, `ajuda`, `sair`.

### Regras rápidas
- Entrada inválida → repete pergunta.  
- Divisão por zero → bloqueada.  
- **Potência com base negativa:** exige **expoente inteiro** (resultado real).  
- **Fatorial:** só **inteiro ≥ 0** (aceita `5.0`).  
- `sqrt` só `≥ 0`; `log` só `> 0`.





## Como executar o arquivo `.sh`

Pré-requisitos: Ubuntu/Linux com **bash** e **Python 3** instalado.

1. Dê permissão de execução (uma vez):
   ```bash
   chmod 744 calculadora.sh
