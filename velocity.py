class Vel:

    def velo():
        import acc_cal
        import config
        m=acc_cal.Acc2
        i=config.Init
        i.v2 = i.v2 + m.a2 * i.dt
        i.v1 = i.v1 + m.a1 * i.dt
        i.v3 = i.v3 + m.a3 * i.dt
        i.v4 = i.v4 + m.a4 * i.dt
        i.v5 = i.v5 + m.a5 * i.dt
        i.v6 = i.v6 + m.a6 * i.dt
        i.v7 = i.v7 + m.a7 * i.dt
        i.v8 = i.v8 + m.a8 * i.dt
        i.v9 = i.v9 + m.a9 * i.dt   