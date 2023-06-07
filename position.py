class Pos:
    def pos1():
        import numpy as np
        import config
        o=config.Init()
    # this class is dedicated for position calculations
        
        o.positions2[0]=o.r2
        o.positions1[0]=o.r1
        o.positions3[0]=o.r3
        o.positions4[0]=o.r4
        o.positions5[0]=o.r5
        o.positions6[0]=o.r6
        o.positions7[0]=o.r7
        o.positions8[0]=o.r8
        o.positions9[0]=o.r9

    def pos2(s):
        import config
        import acc_cal
        m=acc_cal.Acc2
        c=config.Init
        if s==0:
            c.r2 = c.r2 + c.v2*c.dt + (0.5*m.a2*c.dt**2) # verlet algorithm for position calculation at t=0
            c.r1 = c.r1 + c.v1*c.dt + (0.5*m.a1*c.dt**2)
            c.r3 = c.r3 + c.v3*c.dt + (0.5*m.a3*c.dt**2)
            c.r4 = c.r4 + c.v4*c.dt + (0.5*m.a4*c.dt**2)
            c.r5 = c.r5 + c.v5*c.dt + (0.5*m.a5*c.dt**2)
            c.r6 = c.r6 + c.v6*c.dt + (0.5*m.a6*c.dt**2)
            c.r7 = c.r7 + c.v7*c.dt + (0.5*m.a7*c.dt**2)
            c.r8 = c.r8 + c.v8*c.dt + (0.5*m.a8*c.dt**2)
            c.r9 = c.r9 + c.v9*c.dt + (0.5*m.a9*c.dt**2)

        else:
            c.r2 = 2*c.r2 - c.positions2[s-1] + m.a2*c.dt**2 # verlet algorithm for position calculations at t>0
            c.r1 = 2*c.r1 - c.positions1[s-1] + m.a1*c.dt**2
            c.r3 = 2*c.r3 - c.positions3[s-1] + m.a3*c.dt**2
            c.r4 = 2*c.r4 - c.positions4[s-1] + m.a4*c.dt**2
            c.r5 = 2*c.r5 - c.positions5[s-1] + m.a5*c.dt**2
            c.r6 = 2*c.r6 - c.positions6[s-1] + m.a6*c.dt**2
            c.r7 = 2*c.r7 - c.positions7[s-1] + m.a7*c.dt**2
            c.r8 = 2*c.r8 - c.positions8[s-1] + m.a8*c.dt**2
            c.r9 = 2*c.r9 - c.positions9[s-1] + m.a9*c.dt**2

    def pos3(s):
        import config
        o=config.Init
        o.positions2[s+1]=o.r2 # Store positions for visualization
        o.positions1[s+1]=o.r1
        o.positions3[s+1]=o.r3
        o.positions4[s+1]=o.r4
        o.positions5[s+1]=o.r5
        o.positions6[s+1]=o.r6
        o.positions7[s+1]=o.r7
        o.positions8[s+1]=o.r8
        o.positions9[s+1]=o.r9
    
    