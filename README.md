# Gerador de QR Code

Scriptezinho em Python pra gerar QR code de links. Nada muito complexo.

## Como usar

1. Instala a lib:
```bash
pip install qrcode[pil]
```

2. Roda o script:
```bash
python main.py
```

3. Cola o link quando pedir
4. Escolhe o nome do arquivo (ou deixa em branco)
5. Pronto, vai gerar o QR e abrir automaticamente

## O que faz

- Pega qualquer link e vira QR code
- Se você não colocar https:// ele adiciona sozinho
- Funciona no Windows, Mac e Linux
- Você pode mudar as cores se quiser
- Abre a imagem depois de gerar

## Requisitos

- Python 3.6+
- qrcode library

## Exemplo

Você cola `google.com` e ele gera um QR pro `https://google.com`

Simples assim.

---

Feito rapidinho pra facilitar a vida. Se quiser melhorar algo, fique à vontade.

🐧 Como Rodar no Linux

Se você usa Linux, pode encontrar um erro de permissão ao tentar instalar as bibliotecas, devido à forma como o sistema gerencia as versões do Python. A melhor solução é usar um ambiente virtual para instalar as dependências de forma segura, sem afetar o resto do sistema.

## Siga estes passos:

    Instale o gerenciador de ambientes virtuais (se necessário):
    Bash

sudo apt install python3-venv

## Crie o ambiente virtual na pasta do projeto:
Bash

python3 -m venv venv

## Ative o ambiente virtual:
Bash

source venv/bin/activate

Você saberá que o ambiente está ativo quando (venv) aparecer no início da linha de comando.

## Instale as dependências do projeto dentro do ambiente virtual:
Bash

pip install qrcode[pil]

## Execute o script:
Bash

    python main.py

Pronto! Agora o script vai rodar sem problemas.
