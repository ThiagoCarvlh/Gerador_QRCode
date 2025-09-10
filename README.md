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
