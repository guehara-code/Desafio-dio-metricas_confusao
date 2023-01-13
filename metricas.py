# Calculo de metricas a partir de matriz de confusao

#A partir da matriz de confusao temos os seguintes valores...

VN = 50     # Negativos Verdadeiros
FN = 5      # Negativos Falsos

FP = 10     # Positivos Falsos
VP = 100    # Positivos Verdaeiros

# Sensibilidade

S = VP/(VP + FN)
print("Sensibilide = " + str(S))

# Especificidade

E = VN/(FP + VN)
print("Especificidade = " + str(E))

# Acurácia

A = (VP + VN)/(VN + FN + FP + VP)
print("Acurácia = " + str(A))

# Precisao

P = VP/(VP + FP)
print("Precisão = " + str(P))

# F-score

F = 2 * (P*S)/(P + S)
print("F-Score = " + str(F))