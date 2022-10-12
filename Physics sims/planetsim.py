from turtle import shape
import taichi as ti
ti.init(arch=ti.cpu)

# VARIABLER
nPlanteter = 100
delta_t = 3e-5

# Note to self, don't increase resolution
x_opplosning = 1200
y_opplosning = 800

# Taichi datastrukturer, doble arrayer
planeter = ti.Vector.field(2, dtype=ti.f32, shape=nPlanteter)
hastigheter = ti.Vector.field(2, dtype=ti.f32, shape=nPlanteter)
masser = ti.field(ti.f32, shape=nPlanteter)
kraftvektorer = ti.Vector.field(2, dtype=ti.f32, shape=nPlanteter)

@ti.kernel
def steg():
    beregn_kraftvektorer()
    flytt()
    
@ti.func
def beregn_kraftvektorer(): # 
    kraftvektorer.fill([0, 0])
    for p1, p2 in ti.ndrange(nPlanteter, nPlanteter):
        if (p1 != p2):
            avstand = (planeter[p2]-planeter[p1]).norm(1e-3)
            endring = masser[p1]*masser[p2]*(planeter[p2]-planeter[p1])/(avstand**3)
            kraftvektorer[p1] += endring

@ti.func
def flytt(): # 
    for p in planeter:
        hastigheter[p] += delta_t / masser[p] * kraftvektorer[p]
        planeter[p] += delta_t*hastigheter[p]
        
        if(planeter[p][0] < 0 or planeter[p][0] > 1):
            hastigheter[p][0] *= -1
        if(planeter[p][1] < 0 or planeter[p][1] > 1):
            hastigheter[p][1] *= -1

@ti.kernel
def init(): # Initsialiserer planet størrelser og hastigheter
    for p in planeter:
        planeter[p] = [ti.random()/3+0.35, ti.random()/3+0.35]
        hastigheter[p] = [200-ti.random()*20, 10-ti.random()*0]
        masser[p] = ti.random()*50
    planeter[0] = [0.4, 0.4]
    hastigheter[0] = [0, 0]
    masser[0] = 10000
    
    # planeter[0] = [0.4, 0.4]
    # hastigheter[0] = [10, 5]
    # masser[0] = 1000
    # planeter[1] = [0.4, 0.4]
    # hastigheter[1] = [50, 100]
    # masser[1] = 5000

init()
gui = ti.GUI("planeter", res=(x_opplosning, y_opplosning), fullscreen=False)
while gui.running:
    # Escape
    while gui.get_event(ti.GUI.PRESS, ti.GUI.MOTION):
        if gui.event.key == ti.GUI.ESCAPE:
            gui.running = False
        
    steg()
    
    # Endrer størrelse på sirklene
    pn = planeter.to_numpy()
    mn = masser.to_numpy()
    for i, p in enumerate(pn):
        rad = max(1, min(16, int(mn[i]/5)))
        gui.circle(p, radius=rad)
    gui.show()
