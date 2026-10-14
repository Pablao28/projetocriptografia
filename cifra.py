def cifrar_texto(texto: str, chave: int) -> str:
    """
    Cifra o texto substituindo cada caractere com base num deslocamento na Tabela ASCII.
    Trata letras maiúsculas, minúsculas e mantém caracteres especiais intactos.
    """
    texto_cifrado = ""
    
    for caractere in texto:
        # Tratamento para letras minúsculas (ASCII 97 a 122)
        if 'a' <= caractere <= 'z':
            ascii_original = ord(caractere)
            novo_ascii = 97 + ((ascii_original - 97 + chave) % 26)
            texto_cifrado += chr(novo_ascii)
            
        # Tratamento para letras maiúsculas (ASCII 65 a 90)
        elif 'A' <= caractere <= 'Z':
            ascii_original = ord(caractere)
            novo_ascii = 65 + ((ascii_original - 65 + chave) % 26)
            texto_cifrado += chr(novo_ascii)
            
        # Mantém espaços, números e pontuações sem alterar
        else:
            texto_cifrado += caractere
            
    return texto_cifrado


def decifrar_texto(texto_cifrado: str, chave: int) -> str:
    """
    Decifra o texto aplicando o deslocamento inverso.
    """
    return cifrar_texto(texto_cifrado, -chave)