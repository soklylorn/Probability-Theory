from random import randint

def simulate(n): 
    Attacker = 0
    Defender=0
    Draw=0
    for _ in range(n):
        attack_sol=0
        def_sol=0
        A = sorted([randint(1,6) for _ in range(3)], reverse=True)
        D = sorted([randint(1,6) for _ in range(2)], reverse=True)
        for i in range(len(D)):
            if A[i]>D[i]:
                attack_sol+=1
            elif A[i]<D[i]:
                def_sol+=1
            else:
                def_sol+=1
        if attack_sol>def_sol:
            Attacker+=1
        elif attack_sol<def_sol:
            Defender+=1
        else:
            Draw+=1

    return f"{Attacker/n:.5f}   {Draw/n:.5f}   {Defender/n:.5f}"


def probability():
    
    attacker=[sorted([i1, i2, i3],reverse=True) for i1 in range(1,7) for i2 in range(1,7)for i3 in range(1,7)]
    defender=[sorted([i1, i2],reverse=True) for i1 in range(1,7) for i2 in range(1,7)]
    
    Attacker = 0
    Defender=0
    Draw=0
    for a in attacker:
        for d in defender:
            attack_sol=0
            def_sol=0
            for i in range(len(d)):
                if a[i]>d[i]:
                    attack_sol+=1
                elif a[i]<d[i]:
                    def_sol+=1
                else:
                    def_sol+=1
            if attack_sol>def_sol:
                Attacker+=1
            elif attack_sol<def_sol:
                Defender+=1
            else:
                Draw+=1
    return f"{Attacker/6**5:.5f}   {Draw/6**5:.5f}   {Defender/6**5:.5f}"

def main():
    print("                     Attacker  Draw      Defender")
    print("1000 experiments     "   +  simulate(1000))
    print("1000000 experiments  "+simulate(1000000))
    print("Probability          "         +probability())
          
if __name__ == "__main__":
    main()
