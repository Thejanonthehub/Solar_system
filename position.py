class Pos:
    def pos1():
        import numpy as np
        import config
        o=config.Init()
    # this class is dedicated for position calculations
        # storing the initial position of planets
        o.positions2[0]=o.r2 # Earth
        o.positions1[0]=o.r1 # Sun
        o.positions3[0]=o.r3 # Venus
        o.positions4[0]=o.r4 # Mars 
        o.positions5[0]=o.r5 # Jupiter
        o.positions6[0]=o.r6 # Saturn
        o.positions7[0]=o.r7 # Uranus
        o.positions8[0]=o.r8 # Neptune
        o.positions9[0]=o.r9 # Pluto

    def pos2(s):
        import config
        import acc_cal
        m=acc_cal.Acc2
        c=config.Init
        if s==0:
            # verlet algorithm for position calculation at t=0
            c.r2 = c.r2 + c.v2*c.dt + (0.5*m.a2*c.dt**2) # new position of the Earth
            c.r1 = c.r1 + c.v1*c.dt + (0.5*m.a1*c.dt**2) # new position of the Sun
            c.r3 = c.r3 + c.v3*c.dt + (0.5*m.a3*c.dt**2) # new position of the Venus
            c.r4 = c.r4 + c.v4*c.dt + (0.5*m.a4*c.dt**2) # new position of the Mars
            c.r5 = c.r5 + c.v5*c.dt + (0.5*m.a5*c.dt**2) # new position of the Jupiter
            c.r6 = c.r6 + c.v6*c.dt + (0.5*m.a6*c.dt**2) # new position of the Saturn
            c.r7 = c.r7 + c.v7*c.dt + (0.5*m.a7*c.dt**2) # new position of the Uranus
            c.r8 = c.r8 + c.v8*c.dt + (0.5*m.a8*c.dt**2) # new position of the Neptune
            c.r9 = c.r9 + c.v9*c.dt + (0.5*m.a9*c.dt**2) # new position of the Pluto

        else:
            # verlet algorithm for position calculations at t>0
            c.r2 = 2*c.r2 - c.positions2[s-1] + m.a2*c.dt**2 # new position of the Earth 
            c.r1 = 2*c.r1 - c.positions1[s-1] + m.a1*c.dt**2 # new position of the Sun
            c.r3 = 2*c.r3 - c.positions3[s-1] + m.a3*c.dt**2 # new position of the Venus
            c.r4 = 2*c.r4 - c.positions4[s-1] + m.a4*c.dt**2 # new position of the Mars
            c.r5 = 2*c.r5 - c.positions5[s-1] + m.a5*c.dt**2 # new position of the Jupiter
            c.r6 = 2*c.r6 - c.positions6[s-1] + m.a6*c.dt**2 # new position of the Saturn
            c.r7 = 2*c.r7 - c.positions7[s-1] + m.a7*c.dt**2 # new position of the Uranus
            c.r8 = 2*c.r8 - c.positions8[s-1] + m.a8*c.dt**2 # new position of the Neptune
            c.r9 = 2*c.r9 - c.positions9[s-1] + m.a9*c.dt**2 # new position of the Pluto

    def pos3(s):
        import config
        o=config.Init
        # Store positions for visualization
        o.positions2[s+1]=o.r2 # Earth
        o.positions1[s+1]=o.r1 # Sun
        o.positions3[s+1]=o.r3 # Venus
        o.positions4[s+1]=o.r4 # Mars
        o.positions5[s+1]=o.r5 # Jupiter
        o.positions6[s+1]=o.r6 # Saturn
        o.positions7[s+1]=o.r7 # Uranus
        o.positions8[s+1]=o.r8 # Neptune
        o.positions9[s+1]=o.r9 # Pluto
    
    