# 🧠 Desafios de Python com TDD – Projeto Casa 🚀

Seja bem-vindo, **Casa**!  
Aqui começa sua jornada no mundo da programação com **Python** e **TDD (Test Driven Development)**! 😄🐍

Neste projeto, você vai encarar **9 desafios práticos**, do nível mais fácil ao mais desafiador.  
E o melhor: **vamos testar o código desde o início**, como um verdadeiro programador profissional.

---

## 💡 Como funciona

Cada desafio está dividido em arquivos:

- 📄 `a primeira função` → É onde você implementa sua lógica
- 🧪 `test...` → Onde você escreve (ou roda) os testes automatizados com `pytest`

---

## 🧪 O que é TDD?

> **TDD** significa *Test Driven Development*, ou seja:  
> **Escrevemos os testes antes do código!** 💥

Fluxo básico:

1. ✍️ Escreve o teste (vai falhar!)
2. 👨‍💻 Escreve o código necessário para fazer o teste passar
3. 🔧 Refatora se quiser… com segurança 😎

---

## 🛠️ Como rodar os testes

Antes de tudo, instale o `pytest`:

```bash
pip install pytest
```

Depois, para rodar todos os testes:
```bash
pytest
```

Ou para rodar apenas um exercício:
```bash
pytest ex_03.py
```
---

📚 Lista de Exercícios
| Nº | Desafio                 | Tema                    |
| -- | ----------------------- | ----------------------- |
| 1  | Soma de dois números    | entrada e saída         |
| 2  | Par ou Ímpar            | condicionais            |
| 3  | Contador até 10         | laços `for`             |
| 4  | Tabuada                 | laços + multiplicação   |
| 5  | Lista de nomes em ordem | listas e `.sort()`      |
| 6  | Palíndromos             | strings + slicing       |
| 7  | Jogo de adivinhação     | laços + `random`        |
| 8  | Calculadora com funções | funções + operadores    |
| 9  | Validador de CPF        | lógica + validação real |

---

😎 Dicas para aproveitar melhor
Leia as docstrings nas funções — são seus guias no código.

Use os testes como missões: seu objetivo é fazer todos eles passarem.

Faça commits pequenos e organizados, com mensagens como:

"feat: exercício 5 completo"

"test: valida palíndromo"

"refactor: função de CPF otimizada"

---

Com carinho,
Lucas Eduardo ✨
