import matplotlib.pyplot as Plt
import math

V_In = float( input( 'Tensione in: ' ) )
V_Out = float( input( 'Tensione out: ' ) )
R = float( input( 'Resistenza: ' ) )
L = float( input( 'Induttanza: ' ) )

N = 10000

Tau = L / R

I = []  # delta corrente partendo da 0
E = []  # somma dei quanti di energia in un secondo
MaxI = 0
MaxE = 0
MaxOn = 0
MaxOff = 0

for Cur in range( 1, N ):
    TmpI = ( V_In / R ) * ( Cur / N )
    
    T_On = - Tau * math.log( 1 - ( TmpI / ( V_In / R ) ) ) # i( t ) = V_In / R * ( 1 - e^-( t / tau ) )
    T_Off = - Tau * math.log( ( V_In - V_Out ) / ( R * ( ( ( V_In - V_Out ) / R ) - TmpI ) ) ) # i( t ) = ( V_In - V_Out ) / R + ( I0 - ( V_In - V_Out ) / R ) ) e^-( t / tau )
    
    TmpE = 0.5 * L * ( TmpI ** 2 ) / ( T_On + T_Off )

    if( TmpE > MaxE ):
        MaxI = TmpI
        MaxE = TmpE
        MaxOn = T_On
        MaxOff = T_Off

    I.append( TmpI )
    E.append( TmpE )

#T = - Tau * math.log( 1 - ( MaxI / ( Vin / R ) ) )

print( f'E: {MaxE} J\nI: {MaxI} A\nT on: {MaxOn}\nT off: {MaxOff}\nT: {MaxOn + MaxOff}\nF: {1 / ( MaxOn + MaxOff )}')
Plt.plot( I, E )
Plt.show()
