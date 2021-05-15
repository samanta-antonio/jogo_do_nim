def computador_escolhe_jogada(n, m):
    computadorRemove = 1

    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove

        else:
            computadorRemove += 1
            
    return computadorRemove




def usuario_escolhe_jogada(n, m):
    jogadaValida = False


    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > n or jogadorRemove >m:
             print()
             print('Oops! Jogada inválida! Tente de novo.')
             print()
            
        else:
            jogadaValida = True

    return jogadorRemove


def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()

        partida()
        numeroRodada += 1

    print ('Placar: Você 0 x 3 Computador')



def partida ():
    n = int(input('Quantas peças? '))
    print()

    m = int(input('Limite de peças por jogada? '))
    print()

    turnoPC = False

    if n % (m+1) == 0:
        print('Você começa')
    else:
        print('Computador começa!')
        turnoPC = True


    while n > 0:
        if turnoPC:
            computadorRemove = computador_escolhe_jogada(n,m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print('O computador tirou uma peça')
            else:
                print('O computador tirou', computadorRemove, 'peças')

            turnoPC = False

        else:
            jogadorRemove = usuario_escolhe_jogada(n,m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print('Você retirou uma peça')
            else:
                print('Você tirou', jogadorRemove, 'peças.')
                
            turnoPC = True

            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            else:
                if n != 0:
                    print('Agora restam, ', n , 'peças no tabuleiro.')

    print('Fim do jogo! O computador ganhou!')



        

print('Bem-vindo ao jogo do NIM! Aposto que você irá perder! Escolha: ')
print()

print('1 - para jogar uma partida isolada ')
print()

tipoPartida = int(input('2 - para jogar um campeonato '))
print()

if tipoPartida == 2:
    print('Você escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoPartida == 1:
        print('Você escolheu uma partida isolada')
        print()
        partida()
    else:
        print('Digite um número válido')
        
        
    
        



    
