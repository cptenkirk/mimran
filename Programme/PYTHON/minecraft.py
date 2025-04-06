from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
application.vsync = True
application.development_mode = False
window.fullscreen = False
player = FirstPersonController()
Sky()
DirectionalLight(parent=scene, y=2,z=3,shadows=True)
def add_box(position):
    Button(
        
        parent = scene,
        model = 'cube',
        origin_y = 0.5,
        color = color.brown,
        position = position
     )
for x in range(50):
 for y in range(50):  
  add_box((x,0,y))   
app.run()


