from __future__ import print_function,division
import math as m

# Nome:Cinthia Midory Uehara Tengan
# NUSP:8012071
# Disciplina: MAP0214 - Cálculo Numérico com Aplicações em Física
# Professor: Professor Dr. André Salles de Carvalho
# Data: 06/12/2017

#---------------------------A EQUAÇÃO DE KEPLER--------------------------------
def main():
    
    # Informações iniciais do Exercício-Programa
    a=149.6e6;        # a: Semi-eixo maior da órbita terrestre (Km).
    G=6.67408e-11;    # G: Constante gravitacional (m3kg-1s-2).
    M=1.99e30;        # M: Massa do sol (kg).
    t0=[];            # t0: Período (dias) do periélio terrestre.
    e=0.06;           # e: Excentricidade da elipse terrestre.
    eps=1e-4;         # eps: Condição de parada do método de Newton.
    
    # Preenchendo os valores do periélio
    j=0;              # j: contador        
    P=0;              # P: Período para cada mês (dias).
    while(j<=12):
        if j > 0:
            P = ((2*m.pi)/(30*j));
            t0.append(P)
        else:
            t0.append(j)
        j = j + 1;
    
    # Calculando a constante representada pela anomalia média
    Nt=[];          # Nt: lista que receberá valores da anomalia média (rad).   
    for i in range(len(t0)):
        cte=m.sqrt(G*M/m.pow(a,3))*t0[i];
        Nt.append(cte)
        
    # Calculando os valores da anomalia excêntrica a partir da Eq. de Kepler
    E = [];         # E: lista que receberá valores da anomalia excêntrica (rad).
    for k in Nt:
        value = Kepler(k,e,eps);
        E.append(value)
    
    """Calculando a distância da órbita da Terra em relação ao sol, a diferença
    entre o calculado e o medido em sites de periélio e mostrando os resultados
    no prompt"""
    r = [];         # r: Lista que receberá os valores das distâncias calculadas (km)
    for i in range(len(E)):
        res = a*(1 - e*m.cos(E[i]))
        r.append(res)
        print('Período (dias): ',t0[i]);
        print('Anomalia excêntrica (rad): ',E[i]);
        print('Distância (km): ',r[i]);
        if i <= 11:
            p_2017 = 147100998; # p_2017: periélio referente a jan/2017.
            dif = r[i] - p_2017;
            print ('Diferença (km): ',dif, '\n')
        else:
            p_2018 = 147097233; # p_2018: periélio referente a jan/2018.
            dif = r[i] - p_2018;
            print('Diferença (km): ',dif, '\n')
            
#-----------------FUNÇÃO QUE CALCULA A EQUAÇÃO DE KEPLER-----------------------            

def Kepler(Nt,e,eps):
    E = Nt;        # E: Valor inicial da anomalia excêntrica (rad)
    Ep = E - (E - e*m.sin(E) - Nt)/(1 - e*m.cos(E)); # Ep: valor para cada iteração de Newton
    while (abs(Ep - E) > eps):
        E = Ep;
        Ep =  E - (E - e*m.sin(E) - Nt)/(1 - e*m.cos(E));
    E = Ep;        # valor que o método de Newton encontrou para a função.
    return E
    
main()        
