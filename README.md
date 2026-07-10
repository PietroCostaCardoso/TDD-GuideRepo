# Guia de TDD
* [Versão em Português](#versão-em-português)
* [English Version](#english-version)
---

## Versão em Português

### O Ciclo Red, Green, Refactor (TDD)

O ciclo **Red, Green, Refactor** é a base do TDD (*Test-Driven Development* ou Desenvolvimento Guiado por Testes). Funciona como um guia em três passos simples para criar códigos com menos erros e de alta qualidade:

**Resumo Visual:** 
1. **Red** = Cria um teste que falha.
2. **Green** = Faz o código funcionar o mais rápido possível.
3. **Refactor** = Limpa e melhora o código sem quebrar nada.


---

### Ferramentas

#### Type Hints & Mypy 
Aprendi a dar "dicas de tipo" para o Python. O Mypy funciona como um corretor ortográfico que avisa se estamos a passar o tipo de dado errado (como um texto onde deveria ser um número) antes do programa rodar.

#### Asserts 
Aprendi a criar travas de segurança no meio do código para garantir que condições absurdas parem o programa imediatamente se algo der muito errado.

#### Doctest 
Aprendi a unir documentação e testes no mesmo lugar, escrevendo exemplos práticos de uso diretamente nas caixas de texto (*docstrings*) das funções.

#### Unittest 
Aprendi a criar uma estrutura de testes organizada e automatizada usando classes e métodos para validar cenários e comportamentos complexos do sistema.

#### Coverage 
Aprendi a usar um "fiscal de testes" num arquivo único para medir a percentagem do código que realmente foi testada, garantindo que nenhum `if` ou `else` fique desprotegido.

---

### O Que Eu Espero Mostrar Para Todos

Com este projeto, o objetivo é demonstrar que testar não é apenas clicar no sistema para ver se ele funciona, mas sim criar uma **rede de proteção automatizada**.

Quero mostrar para todos que, ao dominar estas ferramentas de forma isolada e organizada, o programador encontra *bugs* antes mesmo que o utilizador final perceba que eles existem. A qualidade de código é um processo contínuo que começa logo na primeira linha escrita.

---

### A Importância Estratégica do TDD

Para fechar, todas as ferramentas unem-se sob uma única metodologia: o **TDD**. O TDD não é uma ferramenta que se instala, mas sim uma filosofia de trabalho baseada no ciclo contínuo.

A importância de aplicar o TDD no dia a dia resume-se em:

* **Design de Código Melhor:** Como escreve o teste primeiro, é obrigado a pensar em como o seu código vai ser usado antes mesmo de o escrever. Isso gera funções menores, mais simples e focadas.
* **Segurança para Mudar:** Em sistemas reais, alterar código antigo dá medo de quebrar outra parte do software. Com o TDD, ganha uma bateria de testes que cobre tudo. Se mudar algo e quebrar outra coisa, o teste avisa na hora.
* **Economia de Tempo e Dinheiro:** Encontrar um *bug* enquanto está a programar custa segundos. Encontrar um *bug* quando o sistema já está nas mãos do cliente pode custar caro e prejudicar a reputação da empresa. O TDD garante que o software nasça robusto.

[⬆️ Voltar ao índice](#-índice--table-of-contents) | [Ir para Versão em Inglês](#english-version)

---

## English Version

### The Red, Green, Refactor Cycle (TDD)

The **Red, Green, Refactor** cycle is the foundation of TDD (*Test-Driven Development*). It works as a simple three-step guide to writing high-quality code with fewer bugs:

**Visual Summary:** 
1. **Red** = Write a test that fails.
2. **Green** = Make the code work as quickly as possible.
3. **Refactor** = Clean up and improve the code without breaking anything.

---

### Tools

#### Type Hints & Mypy 
I learned how to add "type hints" to Python. Mypy works like a spell checker that warns you if you are passing the wrong data type (like text where a number should be) before the program even runs.

#### Asserts 
I learned how to create safety nets within the code to ensure that absurd conditions stop the program immediately if something goes terribly wrong.

#### Doctest 
I learned how to combine documentation and testing in the same place by writing practical usage examples directly inside the functions' *docstrings*.

#### Unittest 
I learned how to create an organized and automated testing structure using classes and methods to validate complex scenarios and system behaviors.

#### Coverage 
I learned how to use a "test inspector" on a single file to measure the percentage of the code that was actually tested, ensuring that no `if` or `else` statement is left unprotected.

---

### What I Hope to Show Everyone

The goal of this project is to demonstrate that testing is not just about clicking through the system to see if it works, but rather about creating an **automated safety net**.

I want to show everyone that by mastering these tools in an isolated and organized way, a programmer can find bugs even before the end-user notices they exist. Code quality is a continuous process that begins with the very first line written.

---

### The Strategic Importance of TDD

To wrap up, all these tools come together under a single methodology: **TDD**. TDD is not a tool you install, but a philosophy of work based on a continuous cycle.

The importance of applying TDD daily can be summarized as:

* **Better Code Design:** Since you write the test first, you are forced to think about how your code will be used before you even write it. This leads to smaller, simpler, and more focused functions.
* **Confidence to Change:** In real-world systems, modifying legacy code brings the fear of breaking another part of the software. With TDD, you get a test suite that covers everything. If you change something and break something else, the test alerts you immediately.
* **Saving Time and Money:** Finding a bug while you are coding takes seconds. Finding a bug when the system is already in the hands of the client can be costly and damage the company's reputation. TDD ensures that the software is robust from birth.

[⬆️ Back to top](#-índice--table-of-contents) | [ Go to Portuguese Version](#versão-em-português)

## 👤 Autor

Desenvolvido com dedicação por **Pietro Costa Cardoso**.  
Se este projeto te ajudou, considere dar uma ⭐ no repositório!

Link original:

Pietro Costa Cardoso. Todos os direitos reservados sob a Licença MIT.