#
# Enunciado: Crea una función que sea capaz de detectar y retornar todos los
# handles de un texto usando solamente Expresiones Regulares.
# Debes crear una expresión regular para cada caso:
# - Handle usuario: Los que comienzan por "@"
# - Handle hashtag: Los que comienzan por "#"
# - Handle web: Los que comienzan por "www.", "http://", "https://"
#   y finalizan con un dominio (.com, .es...)
#

import re


def identify_text(text):
    user_pattern = re.compile(r"^@")
    hashtag_pattern = re.compile(r"^#")
    website_pattern = re.compile("((https?://(www\\.)?)|www\\.)[\\w#+\\=]{2,256}\\.[a-zA-Z]{2,7}[\\w\\/?=&.+-]*",
                                 re.IGNORECASE)
    if user_pattern.match(text):
        return "Username"
    elif hashtag_pattern.match(text):
        return "Hashtag"
    elif website_pattern.match(text):
        return "Website"


print(identify_text("www.fg.com"))
