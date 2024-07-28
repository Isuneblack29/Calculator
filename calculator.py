#soma_total = 
#subtracao_2 = 
#subtracao_3 =
#subtracao_4 =
#multiplicacao_2 =
#multiplicacao_3 =
#multiplicacao_4 =
#divisao_2 = 
#divisao_3 = 
#divisao_4 = 



print(' CALCULADORA COM IF')
print('[1] = SOMA')
print('[2] = SUBTRAÇÃO')
print('[3] = MULTIPLICAÇÃO')
print('[4] = DIVISÃO')
op = input('Digite a opção: ')




if '1' in op:
    print('VOCÊ SELECIONOU SOMA')
    print('[2] DOIS NÚMEROS')
    print('[3] TRÊS NÚMEROS')
    print('[4] QUATRO NÚMEROS')
    soma = input('Digite a opção:')
    if '2' in soma:
        print('VOCÊ SELECIONOU DOIS NÚMEROS')
        s1 = float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        s2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        print(f'O RESULTADO DA SOMA FOI = {s1+s2}')
    elif '3' in soma:
        print('VOCÊ SELECIONOU TRÊS NÚMEROS')
        s1 = float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        s2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        s3 = float(input('DIGITE O TERCEIRO NÚMERO: '))
        print(f'O RESULTADO DA SOMA FOI = {s1+s2+s3}')
    elif '4' in soma:
        print('VOCÊ SELECIONOU QUATRO NÚMEROS')
        s1 = float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        s2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        s3 = float(input('DIGITE O TERCEIRO NÚMERO: '))
        s4 = float(input('DIGITE O QUARTO NÚMERO'))
        print(f'O RESULTADO DA SOMA FOI = {s1+s2+s3+s4}')
    else:
        print('Você deixou o campo vazio')


elif '2' in op:
    print('VOCÊ SELECIONOU SUBTRAÇÃO')
    print('[2] DOIS NÚMEROS')
    print('[3] TRÊS NÚMEROS')
    print('[4] QUATRO NÚMEROS')
    subtracao = input('Digite a opção:')
    if '2' in subtracao:
        print('VOCÊ SELECIONOU DOIS NÚMEROS')
        sub1 = float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        sub2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        print(f'O RESULTADO DA SUBTRAÇÃO FOI = {sub1-sub2}')
    elif '3' in subtracao:
        print('VOCÊ SELECIONOU TRÊS NÚMEROS')
        sub1 = float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        sub2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        sub3 = float(input('DIGITE O TERCEIRO NÚMERO: '))
        print(f'O RESULTADO DA SUBTRAÇÃO FOI = {sub1-sub2-sub3}')
    elif '4' in subtracao:
        print('VOCÊ SELECIONOU QUATRO NÚMEROS')
        sub1 = float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        sub2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        sub3 = float(input('DIGITE O TERCEIRO NÚMERO: '))
        sub4 = float(input('DIGITE O QUARTO NÚMERO: '))
        print(f'O RESULTADO DA SUBTRAÇÃO FOI = {sub1-sub2-sub3-sub4}')
    else:
        print('Você deixou o campo vazio')



elif '3' in op:
    print('VOCÊ SELECIONOU MULTIPLICAÇÃO')
    print('[2] DOIS NÚMEROS')
    print('[3] TRÊS NÚMEROS')
    print('[4] QUATRO NÚMEROS')
    multiplicacao = input('Digite a opção:')
    if '2' in multiplicacao:
        print('VOCÊ SELECIONOU DOIS NÚMEROS')
        mult1= float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        mult2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        print(f'O RESULTADO DA MULTIPLICAÇÃO FOI = {mult1*mult2}')
    elif '3'  in multiplicacao:
        print('VOCÊ SELECIONOU TRÊS NÚMEROS')
        mult1= float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        mult2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        mult3 = float(input('DIGITE O TERCEIRO NÚMERO: '))
        print(f'O RESULTADO DA MULTIPLICAÇÃO FOI = {mult1*mult2*mult3}')
    elif '4' in multiplicacao:
        print('VOCÊ SELECIONOU QUATRO NÚMEROS')
        mult1= float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        mult2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        mult3 = float(input('DIGITE O TERCEIRO NÚMERO: '))
        mult4 = float(input('DIGITE O QUARTO NÚMERO: '))
        print(f'O RESULTADO DA MULTIPLICAÇÃO FOI = {mult1*mult2*mult3*mult4}')
    else:
        print('Você deixou o campo vazio')




elif '4' in op:
    print('VOCÊ SELECIONOU DIVISÃO')
    print('[2] DOIS NÚMEROS')
    print('[3] TRÊS NÚMEROS')
    print('[4] QUATRO NÚMEROS')
    divisao = input('Digite a opção:')
    if '2' in divisao:
        print('VOCÊ SELECIONOU DOIS NÚMEROS')
        div1 = float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        div2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        print(f'O RESULTADO DA DIVISÂO FOI = {div1/div2}')
    elif '3' in divisao:
        print('VOCÊ SELECIONOU TRÊS NÚMEROS')
        div1 = float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        div2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        div3 = float(input('DIGITE O TERCEIRO NÚMERO: '))
        print(f'O RESULTADO DA DIVISÂO FOI = {div1/div2/div3}')
    elif '4' in divisao:
        print('VOCÊ SELECIONOU QUATRO NÚMEROS')
        print('VOCÊ SELECIONOU TRÊS NÚMEROS')
        div1 = float(input('DIGITE O PRIMEIRO NÚMERO: ')) 
        div2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
        div3 = float(input('DIGITE O TERCEIRO NÚMERO: '))
        div4 = float(input('DIGITE O QUARTO NÚMERO: '))
        print(f'O RESULTADO DA DIVISÂO FOI = {div1/div2/div3/div4}')
    else:
        print('Você deixou o campo vazio')
else:
    print('Você deixou o campo vazio')