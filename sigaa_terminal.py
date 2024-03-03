def calcular_media(notas):
    soma = sum(notas)
    return soma / len(notas)

def verificar_aprovacao(media):
    if media >= 6:
        return "aprovado por média"
    elif media < 2:
        return "reprovado por média"
    else:
        return "prova final necessária"

def verificar_prova_final(media):
    if media >= 4:
        return "aprovado"
    else:
        return "reprovado"

def solicitar_notas():
    notas = []
    for i in range(6):
        while True:
            try:
                nota = float(input(f"Informe a nota da {i+1}ª unidade (0 a 10): "))
                if nota < 0 or nota > 10:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, insira apenas notas de 0 a 10.")
        notas.append(nota)
    return notas

def main():
    while True:
        try:
            notas = solicitar_notas()

            media = calcular_media(notas)

            if media >= 6 or media < 2:
                resultado = f"Média do aluno: {media:.2f}\n{verificar_aprovacao(media)}"
            
            else:
                prova_final = float(input("Informe a nota da prova final do aluno (0 a 10): "))
                media_final = (media + prova_final) / 2
                resultado = f"Média do aluno: {media_final:.2f}\n{verificar_prova_final(media_final)}"

            print(resultado)

            repetir = input("Deseja repetir a operação? (S/N): ").strip().upper()
            if repetir != 'S':
                break
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
 
