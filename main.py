class Main:
    
        import acc_cal
        import config
        import position
        import velocity
        import plotting
        import acc_cal
        k=acc_cal.Acc2
        a=acc_cal.Acc
        p=position.Pos
        v=velocity.Vel
        pl=plotting.Plot
        o=config.Init

        p.pos1()

# initial acceleration calculations

        k.a1=a.acceleration("Sun") # acceleration of the Sun
        k.a2=a.acceleration("Earth") # acceleration of the Earth
        k.a3=a.acceleration("Venus") # acceleration of the Venus
        k.a4=a.acceleration("Mars")  # acceleration of the Mars
        k.a5=a.acceleration("Jupiter")  # acceleration of the Jupiter
        k.a6=a.acceleration("Saturn")  # acceleration of the Saturn
        k.a7=a.acceleration("Uranus")  # acceleration of the Uranus
        k.a8=a.acceleration("Neptune")  # acceleration of the Neptune
        k.a9=a.acceleration("Pluto")  # acceleration of the Pluto

        for step in range(o.num_steps):
            p.pos2(step)
        
            k.a1=a.acceleration("Sun")
            k.a2=a.acceleration("Earth")
            k.a3=a.acceleration("Venus")
            k.a4=a.acceleration("Mars")
            k.a5=a.acceleration("Jupiter")
            k.a6=a.acceleration("Saturn")
            k.a7=a.acceleration("Uranus")
            k.a8=a.acceleration("Neptune")
            k.a9=a.acceleration("Pluto")

            v.velo()

            p.pos3(step)
    
        pl.plt()

    
