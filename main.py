import qrcode
import os

def main():
    print("=== GERADOR QR CODE ===")
    
    url = input("Cole o link aqui: ")
    
    # adiciona https se não tiver
    if not url.startswith('http'):
        url = 'https://' + url
    
    print(f"Gerando QR para: {url}")
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # salva com nome baseado no timestamp
    import time
    filename = f"qrcode_{int(time.time())}.png"
    img.save(filename)
    
    print(f"Salvo como {filename}")
    
    # abre a imagem automaticamente
    try:
        os.startfile(filename)  # windows
    except:
        pass

main()