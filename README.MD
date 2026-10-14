# 🎮 Jogo da Velha Interativo no Terminal (Python)

Um Jogo da Velha (Tic-Tac-Toe) fluido e 100% jogável diretamente no terminal, construído em Python. 
Diferente dos jogos de terminal comuns que exigem digitar coordenadas e apertar `Enter`, este projeto utiliza **Programação Orientada a Eventos (Event-Driven)** para capturar as setas do teclado em tempo real.

## ✨ Funcionalidades

- **Controle em Tempo Real:** Navegue pelo tabuleiro usando as setas do teclado (sem precisar do input padrão).
- **Interface Limpa (CLI):** O terminal é atualizado dinamicamente criando a ilusão de uma tela estática.
- **Sistema Anti-Bugs:** Implementação de limpeza de buffer de hardware (`termios.tcflush`) para evitar conflitos entre as teclas pressionadas e os menus do jogo.
- **Lógica Completa:** Deteção automática de vitórias (linhas, colunas, diagonais) e empates.
- **Loop de Gameplay:** Opção de jogar novamente sem precisar reiniciar o script.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **[pynput](https://pypi.org/project/pynput/):** Biblioteca principal para monitorar e escutar os eventos do teclado (Threads).
- **termios / sys / os:** Bibliotecas nativas do Python para manipulação do ambiente Linux/Unix.

## ⚠️ Pré-requisitos e Compatibilidade

> **Nota para utilizadores de Windows:** Este projeto utiliza a biblioteca `termios` e comandos como `clear`, que são exclusivos para sistemas **Unix (Linux e macOS)**. Para rodar no Windows, pequenas adaptações no código seriam necessárias.

Você precisará instalar a biblioteca `pynput` antes de rodar o jogo:

```bash
pip install pynput