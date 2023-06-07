class Acc:
    # acceleration calculation
    def acceleration (rc):
        import numpy as np 
        import config 
        obj1=config.Init()
        tot=0
        ac_f=0
        def acc1(m_1,m_2,r_min,r_max,):
            r=r_max-r_min
            r_mag = np.linalg.norm(r)
            G = obj1.G # gravitational constant
            F = (G * m_1 * m_2) / (r_mag ** 2)
            direction = r / r_mag
            F2 = -F * direction


            return F2

        dict1={"Sun":obj1.r1,"Venus":obj1.r3,"Earth":obj1.r2,"Mars":obj1.r4,"Jupiter":obj1.r5,"Saturn":obj1.r6,"Uranus":obj1.r7,"Neptune":obj1.r8,"Pluto":obj1.r9}
        dict2={"Sun":obj1.m1,"Venus":obj1.m3,"Earth":obj1.m2,"Mars":obj1.m4,"Jupiter":obj1.m5,"Saturn":obj1.m6,"Uranus":obj1.m7,"Neptune":obj1.m8,"Pluto":obj1.m9}
        pior=["Sun","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
        for g in pior:
            c=pior.index(rc)
            if pior.index(g)<c:
                r_c1=dict1[g]
                r_c2=dict1[rc]
                m_c1=dict2[g]
                m_c2=dict2[rc]
                ac_f=acc1(m_c1,m_c2,r_c1,r_c2)/m_c2
            elif pior.index(g)>c:
                r_c1=dict1[rc]
                r_c2=dict1[g]
                m_c1=dict2[g]
                m_c2=dict2[rc]
                ac_f=-(acc1(m_c1,m_c2,r_c1,r_c2))/m_c2
            tot+=ac_f
   
        return tot
    
class Acc2:
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    a9=0
    def ac2():
        Acc2.a1=Acc.acceleration("Sun") # acceleration of the Sun
        Acc2.a2=Acc.acceleration("Earth") # acceleration of the Earth
        Acc2.a3=Acc.acceleration("Venus") # acceleration of the Venus
        Acc2.a4=Acc.acceleration("Mars")  # acceleration of the Mars
        Acc2.a5=Acc.acceleration("Jupiter")  # acceleration of the Jupiter
        Acc2.a6=Acc.acceleration("Saturn")  # acceleration of the Saturn
        Acc2.a7=Acc.acceleration("Uranus")  # acceleration of the Uranus
        Acc2.a8=Acc.acceleration("Neptune")  # acceleration of the Neptune
        Acc2.a9=Acc.acceleration("Pluto")  # acceleration of the Pluto
