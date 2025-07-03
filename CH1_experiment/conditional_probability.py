import numpy as np


A = [2,4,6]
B = [1,2,3,4]
Pa = 1/2
Pb = 2/3
Pab = 1/3

def simulate_die_role(trials=10000):
    rollos = np.random.randint(1,7, size=trials)
    A1 = np.isin(rollos,A)
    B1 = np.isin(rollos,B)
    AB1 = A1 & B1

    P1_A1 = np.mean(A1)
    P1_B1 = np.mean(B1)
    P1_AB1 = np.mean(AB1)

    print("Independent Events")
    print(f"P1(A) = {P1_A1}, P1(B) = {P1_B1} ,P1(AB) = {P1_AB1}")
    print(f"P1(AB) = P1(A) * P1(B) = {P1_A1 * P1_B1}")
    print("Conclusion events are approxmiatly independent")

    
    A2 = np.isin(rollos,[2,4,6])
    B2 = np.isin(rollos,[1,3,5])
    AB2 = A2 & B2

    P2_A2 = np.mean(A2)
    P2_B2 = np.mean(B2)
    P2_AB2 = np.mean(AB2)

    print("Independent Events")
    print(f"P2(A) = {P2_A2}, P2(B) = {P2_B2} ,P2(AB) = {P2_AB2}")
    print(f"P2(AB) = P2(A) * P2(B) = {P2_A2 * P2_B2}")
    print("Conclusion events are approxmiatly not independent")

simulate_die_role()