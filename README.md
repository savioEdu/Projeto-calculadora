# Projeto calculadora em Python
## Sobre o projeto

Atividade pratica do curso Analista de Dados da EBAC

Desenvolver uma calculadora capaz de fazer contas aritméticas entre dois números de forma simples e intuitiva.

Além do desenvolvimento da calculadora ser em Python será usado um Script Shell para facilitar a execução.  

# Criação e funcionalidade da calculadora

O programa ira pedir inicialmente seu nome, logo após pedira 2 numero em que será realizada uma serie de operações básicas como:

* Soma
* Subtração
* Multiplicação
* Divisão

A calculadora contem um menu interativo que permanece em execução até que o usuário escolha encerrar o programa.

Caso o usuario digite letras ou contas incorretas o sistema retorna e exibira uma mensagem 


```python
[erro]
```

Ate o momento o programa não realiza divisão por zero não contem históricos de operação ou tratamento de porcentagem.

## Módulos usados e estrutura do projeto

```text
├── calculadora.py
├── calculadora.sh
├── comandos.txt
└── README.md
```

* Python 3
* Shell Script (Bash)
* Linux (Ubunto)
* GitHub

  ## Como executar

1. Abra o terminal.
2. Navegue até a pasta do projeto.
3. Conceda permissão de execução ao arquivo:

```bash
chmod 744 calculadora.sh
```

4. Execute o programa:

```bash
./calculadora.sh
```
