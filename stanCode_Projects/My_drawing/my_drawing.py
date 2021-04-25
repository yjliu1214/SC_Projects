"""
File: My Drawing
Name: Serena
----------------------
This file draws Big Ben with campy module.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    This file draws London landmarks.
    """
    window = GWindow(width=600, height=750, title='my drawing')

    ground = GRect(570, 85, x=15, y=650)
    ground.color = 'darkseagreen'
    ground.filled = True
    ground.fill_color = 'darkseagreen'
    window.add(ground)

    sky = GRect(570, 635, x=15, y=15)
    sky.color = 'lavender'
    sky.filled = True
    sky.fill_color = 'lavender'
    window.add(sky)

    tower1 = GRect(130, 275, x=110, y=425)
    tower1.color = 'wheat'
    tower1.filled = True
    tower1.fill_color = 'wheat'
    window.add(tower1)

    tower2 = GRect(150, 25, x=100, y=400)
    tower2.color = 'wheat'
    tower2.filled = True
    tower2.fill_color = 'wheat'
    window.add(tower2)

    tower3 = GRect(130, 110, x=110, y=291)
    tower3.color = 'wheat'
    tower3.filled = True
    tower3.fill_color = 'wheat'
    window.add(tower3)

    tower4 = GRect(150, 25, x=100, y=267)
    tower4.color = 'wheat'
    tower4.filled = True
    tower4.fill_color = 'wheat'
    window.add(tower4)

    tower5 = GRect(130, 25, x=110, y=243)
    tower5.color = 'wheat'
    tower5.filled = True
    tower5.fill_color = 'wheat'
    window.add(tower5)

    tower6 = GRect(70, 30, x=140, y=210)
    tower6.color = 'cornflowerblue'
    tower6.filled = True
    tower6.fill_color = 'cornflowerblue'
    window.add(tower6)

    tower7 = GRect(70, 25, x=140, y=185)
    tower7.color = 'wheat'
    tower7.filled = True
    tower7.fill_color = 'wheat'
    window.add(tower7)

    tower8 = GPolygon()
    tower8.add_vertex((140, 210))
    tower8.add_vertex((140, 240))
    tower8.add_vertex((110, 240))
    tower8.color = 'cornflowerblue'
    tower8.filled = True
    tower8.fill_color = 'cornflowerblue'
    window.add(tower8)

    tower9 = GPolygon()
    tower9.add_vertex((140, 185))
    tower9.add_vertex((210, 185))
    tower9.add_vertex((175, 70))
    tower9.color = 'cornflowerblue'
    tower9.filled = True
    tower9.fill_color = 'cornflowerblue'
    window.add(tower9)

    tower10 = GPolygon()
    tower10.add_vertex((210, 210))
    tower10.add_vertex((210, 240))
    tower10.add_vertex((240, 240))
    tower10.color = 'cornflowerblue'
    tower10.filled = True
    tower10.fill_color = 'cornflowerblue'
    window.add(tower10)

    clock1 = GRect(100, 90, x=125, y=300)
    clock1.color = 'tan'
    clock1.filled = True
    clock1.fill_color = 'tan'
    window.add(clock1)

    clock2 = GOval(80, 80, x=135, y=305)
    clock2.color = 'whitesmoke'
    clock2.filled = True
    clock2.fill_color = 'whitesmoke'
    window.add(clock2)

    clock3 = GOval(70, 70, x=140, y=310)
    clock3.color = 'white'
    clock3.filled = True
    clock3.fill_color = 'white'
    window.add(clock3)

    clock3 = GOval(6, 6, x=172, y=342)
    clock3.filled = True
    clock3.fill_color = 'dimgray'
    window.add(clock3)

    clock4 = GRect(4, 28, x=173, y=318)
    clock4.color = 'dimgray'
    clock4.filled = True
    clock4.fill_color = 'dimgray'
    window.add(clock4)

    building1 = GRect(250, 140, x=241, y=560)
    building1.color = 'wheat'
    building1.filled = True
    building1.fill_color = 'wheat'
    window.add(building1)

    building2 = GRect(210, 180, x=301, y=520)
    building2.color = 'wheat'
    building2.filled = True
    building2.fill_color = 'wheat'
    window.add(building2)

    building3 = GRect(160, 50, x=326, y=470)
    building3.color = 'cornflowerblue'
    building3.filled = True
    building3.fill_color = 'cornflowerblue'
    window.add(building3)

    building4 = GPolygon()
    building4.add_vertex((301, 520))
    building4.add_vertex((326, 520))
    building4.add_vertex((326, 470))
    building4.color = 'cornflowerblue'
    building4.filled = True
    building4.fill_color = 'cornflowerblue'
    window.add(building4)

    building5 = GPolygon()
    building5.add_vertex((486, 520))
    building5.add_vertex((511, 520))
    building5.add_vertex((486, 470))
    building5.color = 'cornflowerblue'
    building5.filled = True
    building5.fill_color = 'cornflowerblue'
    window.add(building5)

    window1 = GRect(12, 225, x=132.5, y=450)
    window1.color = 'tan'
    window1.filled = True
    window1.fill_color = 'tan'
    window.add(window1)

    window2 = GRect(12, 225, x=157.5, y=450)
    window2.color = 'tan'
    window2.filled = True
    window2.fill_color = 'tan'
    window.add(window2)

    window3 = GRect(12, 225, x=182.5, y=450)
    window3.color = 'tan'
    window3.filled = True
    window3.fill_color = 'tan'
    window.add(window3)

    window4 = GRect(12, 225, x=207.5, y=450)
    window4.color = 'tan'
    window4.filled = True
    window4.fill_color = 'tan'
    window.add(window4)

    window5 = GRect(45, 90, x=320, y=550)
    window5.color = 'tan'
    window5.filled = True
    window5.fill_color = 'tan'
    window.add(window5)

    window6 = GRect(45, 90, x=383, y=550)
    window6.color = 'tan'
    window6.filled = True
    window6.fill_color = 'tan'
    window.add(window6)

    window7 = GRect(45, 90, x=445, y=550)
    window7.color = 'tan'
    window7.filled = True
    window7.fill_color = 'tan'
    window.add(window7)

    name = GLabel('L O N D O N', 290, 110)
    name.font = 'Nelvetica-50-bold'
    name.color = 'white'
    window.add(name)


if __name__ == '__main__':
    main()
