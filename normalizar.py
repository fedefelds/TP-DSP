import numpy as np

def normalizar(senal_a_normalizar):
    valor_max=np.max(senal_a_normalizar)
    senal_normalizada=senal_a_normalizar/valor_max
    return senal_normalizada


