def check_vowels():
    # Código a implementar utilizando input.
    nombre = input("")
    print("Contiene a: " + str("a" in nombre.lower()))
    print("Contiene e: " + str("e" in nombre.lower()))
    print("Contiene i: " + str("i" in nombre.lower()))
    print("Contiene o: " + str("o" in nombre.lower()))
    print("Contiene u: " + str("u" in nombre.lower()))

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
