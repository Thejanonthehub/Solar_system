class Init:

#Initial Conditions
    import numpy as np
    dt = 500000
    num_steps=365
    G = 6.67430e-11 # gravitational constant

    m1 = 1.989e30  # mass of the Sun
    m2 = 5.972e24  # mass of the Earth
    m3 = 4.87e24 # mass of the Venus
    m4 = 0.642e24 # mass of the Mars
    m5 = 1898e24 # mass of the Jupiter
    m6 = 568e24 # mass of the Saturn
    m7 = 86.8e24 # mass of the Uranus
    m8 = 102e24 # mass of the Neptune
    m9 = 0.0130e24 # mass of the Pluto

    r1 = np.array([0.0, 0.0,0.0])  # initial position of the Sun
    r2 = np.array([149.6e9, 0.0,0.0])  # initial position of the Earth
    r3 = np.array([108.2e9,0.0,0.0]) # initial position of the venus
    r4 = np.array([228.0e9,0.0,0.0]) # initial position of the Mars 
    r5 = np.array([778.5e9,0.0,0.0]) # initial position of the Jupiter
    r6 = np.array([1432.0e9,0.0,0.0]) # initial position of the Saturn
    r7 = np.array([2867.0e9,0.0,0.0]) # initial position of the Uranus
    r8 = np.array([4515.0e9,0.0,0.0]) # initial position of the Neptune
    r9 = np.array([5906.4e9,0.0,0.0]) # initial position of the Pluto

    v2 = np.array([0.0,29800.0,0.0])  # initial velocity of the Earth
    v1 = np.array([0.0,0.0,0.0]) # initial velocity of the Sun
    v3 = np.array([0.0,35000.0,0.0]) # initial velocity of the Venus
    v4 = np.array([0.0,24100.0,0.0]) # initial velocity of the Mars
    v5 = np.array([0.0,13100.0,0.0]) # initial velocity of the Jupiter
    v6 = np.array([0.0,9700.0,0.0]) # initial velocity of the Saturn
    v7 = np.array([0.0,6800.0,0.0]) # initial velocity of the Uranus
    v8 = np.array([0.0,5400.0,0.0]) # initial velocity of the Neptune
    v9 = np.array([0.0,4700.0,0.0]) # initial velocity of the Pluto

    positions2 = np.zeros((num_steps+1, 3))
    positions1 = np.zeros((num_steps+1,3))
    positions3 = np.zeros((num_steps+1,3))
    positions4 = np.zeros((num_steps+1,3))
    positions5 = np.zeros((num_steps+1,3))
    positions6 = np.zeros((num_steps+1,3))
    positions7 = np.zeros((num_steps+1,3))
    positions8 = np.zeros((num_steps+1,3))
    positions9 = np.zeros((num_steps+1,3))


