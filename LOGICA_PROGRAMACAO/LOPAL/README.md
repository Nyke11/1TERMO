# 🧠 Lógica de Programação com Python: Guia de Aula

Este documento é o seu manual para entender como "conversar" com o computador e estruturar algoritmos de forma inteligente e organizada. 💻✨

---

## 1. 📥 Interação com o Usuário
Todo programa precisa receber informações e mostrar resultados.

* **`print()` 📢:** A voz do programa. Exibe mensagens na tela.
* **`input()` ⌨️:** O ouvido do programa. Lê o que o usuário digita.
* **`int()` 🔢:** Um conversor. Transforma o texto do input em um número inteiro para que possamos fazer contas.

### 📝 Exemplo Prático:
```python
# Recebendo dados
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Em que ano você nasceu? "))

# Calculando e exibindo
idade = 2024 - ano_nascimento
print(f"Olá {nome}! Você tem {idade} anos. 🎉")

2. 🛣️ Tomada de Decisão (Estruturas Condicionais)
É assim que o programa escolhe caminhos diferentes baseado em regras.

if (se) 🟢: A primeira condição a ser testada.

elif (senão se) 🟡: Uma alternativa caso o primeiro if seja falso.

else (senão) 🔴: O caminho final, caso nenhuma das opções anteriores funcione.

3. 🔄 Repetição e Automação (Loops)
Para que fazer manualmente se o computador pode repetir para você?

while (enquanto) ⏳: Repete o código enquanto uma condição for verdadeira. Cuidado para não criar um loop infinito!

for (para) 🔁: Perfeito para repetir algo um número específico de vezes ou percorrer uma lista de itens.

4. ✨ Clean Code (Código Limpo)
Escrever código que funciona é o básico. Escrever código que outras pessoas entendem é o diferencial! 🤝

Boas Práticas:
Nomes Claros 📛: Use preco_produto em vez de apenas p.

Mantenha Simples 💡: Se a lógica está muito complicada, tente dividi-la.

Atenção à Indentação 📐: Em Python, o espaço no início da linha define quem manda em quem. É fundamental!

🔗 O Ciclo da Programação
Entrada 📥: Coleta de dados com input.

Lógica ⚙️: Decisões com if e repetições com for/while.

Saída 📤: Resultado final com print.