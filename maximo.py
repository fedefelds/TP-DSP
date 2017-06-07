# Para implementar el max([abs(m[0,0]-m[0,1]),abs(m[1,0]-m[1,1]),...,abs(m[a-1,0]-m[a-1,1])
# se puede usar un ciclo for:
#
# maximo= -infinito
# for i desde 0 hasta a-1
#   if abs([abs(m[i,0]-m[i,1]))>maximo
#       maximo=abs([abs(m[i,0]-m[i,1]))
# return maximo

def maximo(m):
    maximo=-1000000000000000000000
    for i in range(0,m.shape[0]):
        if abs(m[i,0]-m[i,1])>maximo:
            maximo=abs(m[i,0]-m[i,1])
    return maximo
