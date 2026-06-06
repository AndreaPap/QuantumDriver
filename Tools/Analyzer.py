import matplotlib.pyplot as Plt
import math

V = float( input( 'Tensione: ' ) )
R = float( input( 'Resistenza: ' ) )
L = float( input( 'Induttanza: ' ) )

N = 10000

Tau = L / R

I = []  # delta corrente partendo da 0
E = []  # somma dei quanti di energia in un secondo
MaxI = 0
MaxE = 0

for Cur in range( 1, N ):
    TmpI = ( V / R ) * ( Cur / N )
    TmpE = L * ( TmpI ** 2 ) / ( - 2 * Tau * math.log( 1 - ( TmpI / ( V / R ) ) ) )

    if( TmpE > MaxE ):
        MaxI = TmpI
        MaxE = TmpE

    I.append( TmpI )
    E.append( TmpE )

T = - Tau * math.log( 1 - ( MaxI / ( V / R ) ) )

print( f'E: {MaxE} J\nI: {MaxI} A\nT: {T} s')
Plt.plot( I, E )
Plt.show()
