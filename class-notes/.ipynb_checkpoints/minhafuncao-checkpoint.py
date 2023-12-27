def faixaIdade(idade):
    if idade <= 12:
        return "Criança"
    elif idade <= 18:
        return "Adolescente"
    elif idade <= 80:
        return "Adulto"
    else:
        return "Idoso"
