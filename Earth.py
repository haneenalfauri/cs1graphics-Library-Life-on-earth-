from cs1graphics import *
from time import sleep
import playsound

w=500
Haneen = Canvas(w, w, 'black', 'Life on Earth')


title=Text('Life on Earth',35)
title.setFontColor('white')
title.move(250,240)
Haneen.add(title)
sleep(10)
Haneen.remove(title)
title=Text('It is believed that an asteroid impact event ',15)
title.setFontColor('white')
title.move(250,225)
title2=Text('is the main reason behind dinosaurs extinction ',15)
title2.setFontColor('white')
title2.move(250,250)
Haneen.add(title)
Haneen.add(title2)

sleep(11)

Haneen.remove(title)
Haneen.remove(title2)

title=Text('65 million years ago',20)
title.setFontColor('white')
title.move(250,250)
Haneen.add(title)
sleep(6)
Haneen.remove(title)

#Draw Earth
paper=Layer()
Earth = Circle(w/10, Point(250,250))
Earth.setFillColor('lightblue')
paper.add(Earth)

# Draw scattered starts in the space
s1=Square(7,Point(0,0))
s1.setFillColor('white')
s1.setBorderColor('yellow')
s1.setBorderWidth(1.70)
s1.rotate(45)

Star_group0=Layer()
s2=s1.clone()
s2.move(100,100) 
Star_group0.add(s2)

s3=s1.clone()
s3.move(50,150) 
Star_group0.add(s3)

s4=s1.clone()
s4.move(25,100) 
Star_group0.add(s4)

s5=s1.clone()
s5.move(50,10) 
Star_group0.add(s5)
paper.add(Star_group0)

Star_group1=Layer()
Star_group1=Star_group0.clone()
Star_group1.move(350,-30)
paper.add(Star_group1)

Star_group2=Layer()
Star_group2=Star_group0.clone()
Star_group2.move(150,40)
paper.add(Star_group2)

Star_group3=Layer()
Star_group3=Star_group0.clone()
Star_group3.move(340,200)
paper.add(Star_group3)

Star_group4=Layer()
Star_group4=Star_group0.clone()
Star_group4.move(40,250)
paper.add(Star_group4)

Star_group5=Layer()
Star_group5=Star_group0.clone()
Star_group5.move(180,325)
paper.add(Star_group5)

# Draw two Continents on Earth
land0=ClosedSpline(Point(10,0), Point(30,20), Point(50,50),Point(110,0), Point(50,30), Point(90,0))
land0.setFillColor( 'green' )
land0.setBorderWidth(1)
land0.move(280,230)
land0.rotate(160)
paper.add(land0)

land = ClosedSpline(Point(23,0), Point(0,40), Point(90,50),Point(110,0), Point(90,0), Point(50,30),  Point(34,30))
land.setFillColor( 'green' )
land.setBorderWidth(1)
land.move(195,250)
land.rotate(-10)
paper.add(land)

din=Circle(0.05,Point(240,240))
paper.add(din)
Haneen.add(paper)
paper.adjustReference(240,240)

playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Backwards Souls.mp3', True)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Backwards Souls.mp3', True)
paper.scale(1.1)
sleep(1.3)
paper.scale(1.2)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Backwards Souls.mp3', True)
paper.scale(1.3)
sleep(1.3)
paper.scale(1.4)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Backwards Souls.mp3', True)
paper.scale(1.5)
sleep(1.3)
paper.scale(1.6)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Backwards Souls.mp3', True)
paper.scale(1.7)
sleep(1.3)
paper.scale(1.8)
# green background rectangle with trees
green_Background=Rectangle(500,500,Point(250,250))
green_Background.setFillColor('lightgreen')
green_Background.setBorderColor('transparent')
Haneen.add(green_Background)
blue_Background=Rectangle(500,500,Point(250,0))
blue_Background.setFillColor('lightblue')
blue_Background.setBorderColor('transparent')
Haneen.add(blue_Background)


# Draw trees with different depths
tree_layer=Layer()
tree = Polygon(Point(50,80), Point(30,140), Point(70,140))
tree.setFillColor('darkGreen')
tree.scale(2)
tree.move(200,40)
tree_rect=Rectangle(25,100,Point(250,250))
tree_rect.setFillColor('brown')
tree_layer.add(tree_rect)
tree_layer.add(tree)

Haneen.add(tree_layer)
tree_layer.move(-50,-50)
tree_layer2=tree_layer.clone()
Haneen.add(tree_layer2)
tree_layer.move(-90,5)
tree_layer3=tree_layer.clone()
Haneen.add(tree_layer3)
tree_layer3.move(-100,10)
tree_layer4=tree_layer.clone()
Haneen.add(tree_layer4)
tree_layer4.move(321,10)
tree_layer5=tree_layer.clone()
Haneen.add(tree_layer5)
tree_layer5.move(120,10)
tree_layer6=tree_layer.clone()
Haneen.add(tree_layer6)
tree_layer6.move(220,0)
tree_layer7=tree_layer.clone()
Haneen.add(tree_layer7)
tree_layer7.move(250,10)
#draw grass
grass = Path(Point(10,70), Point(23,50), Point(30,60),Point(40,30), Point(50,70), Point(60,50),Point(70,70))
grass.setBorderColor('darkGreen')
grass.setBorderWidth(1.4)
grass.scale(0.7)
grass.move(10,240)
grass2=grass.clone()
grass2.move(30,90)
grass3=grass.clone()
grass2.move(80,60)
grass3=grass.clone()
grass3.move(100,90)
grass4=grass.clone()
grass4.move(380,30)
grass5=grass.clone()
grass5.move(280,50)
grass6=grass.clone()
grass6.move(320,150)
Haneen.add(grass)
Haneen.add(grass2)
Haneen.add(grass3)
Haneen.add(grass4)
Haneen.add(grass5)
Haneen.add(grass6)

# Draw Dinosaur Body
Dinasor=Layer()

Dinasor_body=ClosedSpline(Point(23,30), Point(22,23), Point(33,19),Point(45,15), Point(53,17), Point(60,23),Point(73,52), Point(85,75), Point(105,83),
                          Point(125,90),Point(135,103), Point(150,108), Point(98,120),Point(110,122),Point(105,122),Point(90,123), Point(55,125),
                          Point(43,98),Point(45,72),Point(46,60), Point(45,45), Point(43,40),Point(35,40),Point(25,41), Point(20,43), Point(25,38),
                          Point(35,35),Point(43,35), Point(46,34), Point(47,32),Point(45,38),Point(40,27), Point(33,28))


Dinasor_body.setFillColor( 'darkgreen' )
Dinasor_body.setBorderWidth(1)
Dinasor.add(Dinasor_body)


Dinasor_eye1=Circle(5,Point(43,15))
Dinasor_eye1.setFillColor('white')
Dinasor.add(Dinasor_eye1)

Dinasor_eye2=Dinasor_eye1.clone()
Dinasor_eye2.move(4,0)
Dinasor.add(Dinasor_eye2)

Dinasor_eyeball=Circle(1,Point(46,15))
Dinasor_eyeball.setFillColor('black')
Dinasor.add(Dinasor_eyeball)

Dinasor_Back1=Polygon(Point(75,65), Point(70,90), Point(82,73))
Dinasor_Back1.setFillColor( 'green' )
Dinasor_Back1.setBorderWidth(1)
Dinasor.add(Dinasor_Back1)

Dinasor_Back2=Polygon(Point(95,75), Point(90,100), Point(102,83))
Dinasor_Back2.setFillColor( 'green' )
Dinasor_Back2.setBorderWidth(1)
Dinasor.add(Dinasor_Back2)

Dinasor_Back3=Polygon(Point(115,88), Point(110,112), Point(122,92))
Dinasor_Back3.setFillColor( 'green' )
Dinasor_Back3.setBorderWidth(1)
Dinasor.add(Dinasor_Back3)

Dinasor_teeth=Layer()

Dinasor_teeth1=Polygon(Point(23,38), Point(26,32), Point(28,36))
Dinasor_teeth1.setFillColor( 'white' )
Dinasor_teeth1.setBorderWidth(0.1)
Dinasor_teeth.add(Dinasor_teeth1)

Dinasor_teeth2=Dinasor_teeth1.clone()
Dinasor_teeth2.move(4,0)
Dinasor_teeth.add(Dinasor_teeth2)

Dinasor_teeth3=Dinasor_teeth1.clone()
Dinasor_teeth3.move(8,0)
Dinasor_teeth.add(Dinasor_teeth3)

Dinasor_teeth4=Dinasor_teeth1.clone()
Dinasor_teeth4.move(11,0)
Dinasor_teeth.add(Dinasor_teeth4)
Dinasor.add(Dinasor_teeth)

Upper_Dinasor_teeth=Dinasor_teeth.clone()
Upper_Dinasor_teeth.move(0,-6)
Dinasor.add(Upper_Dinasor_teeth)

Hand1=Rectangle(30,5,Point(40,75))
Hand1.rotate(-30)
Hand1.setFillColor( 'darkgreen' )
Dinasor.add(Hand1)
Hand2=Hand1.clone()
Hand2.move(0,10)
Hand2.rotate(-30)
Hand2.setDepth(60)
Dinasor.add(Hand2)

Dinasor_Leg1=Rectangle(45,9,Point(40,110))
Dinasor_Leg1.adjustReference(22.5,-3.5)
Dinasor_Leg1.rotate(-60)
Dinasor_Leg1.setFillColor( 'darkgreen' )
Dinasor.add(Dinasor_Leg1)

Dinasor_Leg2=Rectangle(45,9,Point(65,115))
Dinasor_Leg2.adjustReference(22.5,-3.5)
Dinasor_Leg2.rotate(-60)
Dinasor_Leg2.setFillColor( 'darkgreen' )
Dinasor_Leg2.setDepth(60)
Dinasor.add(Dinasor_Leg2)


#Draw croocodile
Haneen1=Layer()
Aligator_body=ClosedSpline(Point(12,42), Point(15,44), Point(24,44),Point(32,43), Point(39,40), Point(43,46),Point(45,40), Point(47,44), Point(84,45),
                          Point(96,53),Point(120,57), Point(105,55), Point(95,62),Point(80,62),Point(54,61),Point(42,51), Point(24,55),
                          Point(12,53),Point(10,50),Point(14,45), Point(10,44))


Aligator_body.setFillColor( 'darkgreen' )
Aligator_body.setBorderWidth(1)
Aligator_body.scale(1.5)
Haneen1.add(Aligator_body)


Aligator_eye1=Circle(5,Point(43,40))
Aligator_eye1.setFillColor('white')
Haneen1.add(Aligator_eye1)

Aligator_eye2=Aligator_eye1.clone()
Aligator_eye2.move(4,0)
Haneen1.add(Aligator_eye2)

Aligator_eyeball=Circle(1,Point(46,40))
Aligator_eyeball.setFillColor('black')
Haneen1.add(Aligator_eyeball)

Aligator_Back1=Polygon(Point(75,65), Point(70,90), Point(82,73))
Aligator_Back1.setFillColor( 'brown' )
Aligator_Back1.setBorderWidth(1)
Aligator_Back1.move(40,-25)
Aligator_Back1.setDepth(40)
Haneen1.add(Aligator_Back1)

Aligator_Back2=Polygon(Point(95,75), Point(90,100), Point(102,83))
Aligator_Back2.setFillColor( 'brown' )
Aligator_Back2.setBorderWidth(1)
Aligator_Back2.move(5,-34)
Haneen1.add(Aligator_Back2)

Aligator_Back3=Polygon(Point(115,88), Point(110,112), Point(122,92))
Aligator_Back3.setFillColor( 'brown' )
Aligator_Back3.move(-30,-48)
Aligator_Back3.setBorderWidth(1)
Haneen1.add(Aligator_Back3)

Aligator_teeth=Layer()

Aligator_teeth1=Polygon(Point(23,38), Point(26,32), Point(28,36))
Aligator_teeth1.setFillColor( 'white' )
Aligator_teeth1.setBorderWidth(0.1)
Aligator_teeth.add(Aligator_teeth1)

Aligator_teeth2=Aligator_teeth1.clone()
Aligator_teeth2.move(4,0)
Aligator_teeth.add(Aligator_teeth2)

Aligator_teeth3=Aligator_teeth1.clone()
Aligator_teeth3.move(8,0)
Aligator_teeth.add(Aligator_teeth3)

Aligator_teeth4=Aligator_teeth1.clone()
Aligator_teeth4.move(11,0)
Aligator_teeth.add(Aligator_teeth4)
Haneen1.add(Aligator_teeth)

Upper_Aligator_teeth=Aligator_teeth.clone()
Upper_Aligator_teeth.move(0,-6)
Haneen1.add(Upper_Aligator_teeth)

Aligator_teeth.move(-12,15)
Upper_Aligator_teeth.move(-13,16)
Aligator_teeth.scale(1.1)
Upper_Aligator_teeth.scale(1.1)


Aligator_Hand1=Rectangle(20,8,Point(70,70))
Aligator_Hand1.setFillColor( 'darkgreen' )
Aligator_Hand1.adjustReference(10,-4)
Haneen1.add(Aligator_Hand1)

Aligator_Hand2=Rectangle(20,8,Point(65,70))
Aligator_Hand2.setFillColor( 'darkgreen' )
Aligator_Hand2.setDepth(60)
Aligator_Hand2.adjustReference(10,-4)
Haneen1.add(Aligator_Hand2)

Aligator_Hand1.rotate(-40)
Aligator_Hand2.rotate(-70)

Aligator_Leg1=Rectangle(12,25,Point(110,75))
Aligator_Leg1.adjustReference(6,-12.5)
Aligator_Leg1.setFillColor( 'darkgreen' )
Aligator_Leg1.rotate(-60)
Haneen1.add(Aligator_Leg1)

Aligator_Leg2=Rectangle(12,25,Point(110,75))
Aligator_Leg2.adjustReference(6,-12.5)
Aligator_Leg2.setFillColor( 'darkgreen' )
Aligator_Leg2.setDepth(60)
Aligator_Leg2.rotate(-50)
Haneen1.add(Aligator_Leg2)






# Prepare canvas to host the dinasor layer
Haneen.setAutoRefresh(False)
Dinasor.scale(1.3)
Haneen.add(Dinasor)
Haneen.add(Haneen1)
Dinasor.move(400,200)
Haneen1.move(240,300)
Haneen.setAutoRefresh(True)
x=20
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Dragon Roaring.mp3', True)
#Dinasor walk
for i in range(x):
    
    Dinasor_Leg1.rotate(40)
    Dinasor_Leg2.rotate(-40)
    Dinasor.move(-10,0)
    Aligator_Hand1.rotate(40)
    Aligator_Hand2.rotate(40)
    Aligator_Leg2.rotate(50)
    Aligator_Leg1.rotate(50)
    Haneen1.move(-10,0)
    playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Dinosaur Footstep.mp3', True)
    Dinasor_Leg1.rotate(-40)
    Dinasor_Leg2.rotate(40)
    Dinasor.move(-10,0)
    Aligator_Hand1.rotate(-40)
    Aligator_Hand2.rotate(-40)
    Aligator_Leg1.rotate(-50)
    Aligator_Leg2.rotate(-50)
    Haneen1.move(-10,0)
    playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Dinosaur Footstep.mp3', True)
    
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Dragon Roaring.mp3', True)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/Dragon Roaring.mp3', True)


# Draw the Asteroids and add a tail of fire to them

Asteroid=Layer()
yellow_fire=Asteroid1=ClosedSpline(Point(55,53), Point(59,32), Point(68,0),Point(72,30), Point(83,5), Point(79,36),Point(75,49))

yellow_fire.scale(2)
yellow_fire.setBorderWidth(0.5)
yellow_fire.setFillColor( 'yellow' )
red_fire=Asteroid1=ClosedSpline(Point(45,53), Point(49,32), Point(58,0),Point(62,30), Point(73,5), Point(69,36),Point(65,49))
red_fire.setFillColor( 'red' )
red_fire.scale(3)
red_fire.setBorderWidth(0.5)

red_fire.move(200,200)
yellow_fire.move(200,200)



Asteroid1=ClosedSpline(Point(43,60), Point(45,53), Point(48,46),Point(52,42), Point(55,42), Point(62,36),Point(65,41), Point(64,45), Point(65,53),
                          Point(62,55),Point(58,58), Point(53,59), Point(49,61))
crater=Spline(Point(51,50), Point(53,54), Point(49,58))
crater.move(220,200)
crater.scale(2.1)
crater.rotate(90)
crater.setBorderWidth(1.5)
crater2=crater.clone()
crater2.move(20,-20)

Asteroid1.setFillColor( 'gray' )
Asteroid1.setBorderWidth(1)
Asteroid1.scale(3)
Asteroid1.move(200,200)


Asteroid.add(red_fire)
Asteroid.add(yellow_fire)
Asteroid.add(Asteroid1)
Asteroid.add(crater)
Asteroid.add(crater2)

Asteroid_layer2=Asteroid.clone()
Asteroid_layer2.scale(0.6)


Asteroid.rotate(20)
Asteroid_layer2.rotate(20)
Asteroid.move(200,-200)
Asteroid_layer2.move(100,-200)
Haneen.add(Asteroid)
Haneen.add(Asteroid_layer2)

red_background=Rectangle(600,600,Point(250,250))
red_background.setFillColor('red')




# prepare Astroid Hit 

playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/ast1.mp3', True)
Asteroid.scale(1.2)
Asteroid_layer2.scale(1.2)
Asteroid.move(-50,1)
Asteroid_layer2.move(-50,1)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/ast2.mp3', True)
Asteroid.scale(1.5)
Asteroid_layer2.scale(1.5)
Asteroid.move(-75,1)
Asteroid_layer2.move(-75,1)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/ast3.mp3', True)
Asteroid.scale(1.8)
Asteroid_layer2.scale(1.8)
Asteroid.move(-130,1)
Asteroid_layer2.move(-130,1)

Haneen.add(red_background)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/ast4.mp3', True)
sleep(2)
# Clear the screen for the next scene
Haneen.remove(green_Background)
Haneen.remove(blue_Background)
Haneen.remove(tree_layer)
Haneen.remove(tree_layer2)
Haneen.remove(tree_layer3)
Haneen.remove(tree_layer4)
Haneen.remove(tree_layer5)
Haneen.remove(tree_layer6)
Haneen.remove(tree_layer7)
Haneen.remove(grass)
Haneen.remove(grass2)
Haneen.remove(grass3)
Haneen.remove(grass4)
Haneen.remove(grass5)
Haneen.remove(grass6)
Haneen.remove(Dinasor)
Haneen.remove(Asteroid)
Haneen.remove(Asteroid_layer2)
Haneen.remove(red_background)
Haneen.remove(Haneen1)
paper.remove(din)
red_fire.scale(2)
yellow_fire.scale(2)

fire_layer=Layer()
fire_layer.add(red_fire)
fire_layer.add(yellow_fire)
fire_layer2=fire_layer.clone()
fire_layer3=fire_layer.clone()
fire_layer4=fire_layer.clone()

fire_layer2.move(10,0)
fire_layer3.move(20,0)
fire_layer4.move(30,0)
Haneen.add(fire_layer2)
Haneen.add(fire_layer3)
Haneen.add(fire_layer4)
Haneen.add(fire_layer)

# Zoom out on earth and show all other fire 
paper.scale(0.9)
fire_layer.scale(0.9)
fire_layer2.scale(0.9)
fire_layer3.scale(0.9)
fire_layer4.scale(0.9)


# add fire to earth 
sleep(2)
paper.scale(0.4)
fire_layer.scale(0.4)
fire_layer.move(50,100)
fire_layer2.scale(0.4)
fire_layer2.move(55,40)
fire_layer3.scale(0.4)
fire_layer3.move(60,50)
fire_layer4.scale(0.4)
fire_layer4.move(50,45)


sleep(2)
Haneen.remove(fire_layer3)
Haneen.remove(fire_layer4)

paper.scale(0.37)
fire_layer.move(15,-57)
fire_layer2.move(30,-20)


Haneen.remove(fire_layer2)
Haneen.remove(fire_layer)
Haneen.remove(paper)




title=Text('Present 2020',20)
title.setFontColor('white')
title.move(250,250)

sleep(4)
Haneen.add(title)
sleep(4)
Haneen.remove(title)


# prepare the setup for the city scence (add buildings, cars, background)
Buildings=Layer()
building1= Rectangle(80,150,Point(100,150))
building1.setFillColor('gray')
Windows=Layer()
window1=Square(17,Point(73,95))
window1.setFillColor('black')
window1.setBorderColor('yellow')
window2=window1.clone()
window2.move(25,0)
window3=window1.clone()
window3.move(50,0)
Windows.add(window1)
Windows.add(window2)
Windows.add(window3)
Windows_layer2=Windows.clone()
Windows_layer3=Windows.clone()
Windows_layer4=Windows.clone()
Windows_layer5=Windows.clone()
door= Rectangle(23,50,Point(98,200))
door.setFillColor('brown')
Buildings.add(building1)
Windows_layer2.move(0,28)
Windows_layer3.move(0,58)
Windows_layer4.move(0,88)
Windows_layer5.move(0,118)
Buildings.add(Windows_layer2)
Buildings.add(Windows_layer3)
Buildings.add(Windows_layer4)
Buildings.add(Windows_layer5)
Buildings.add(Windows)
Buildings.add(door)

Buildings2=Buildings.clone()
Buildings2.move(250,0)
Buildings3=Buildings.clone()
Buildings3.move(350,-50)
Buildings3.setDepth(70)
Buildings4=Buildings.clone()
Buildings4.move(50,-60)
Buildings4.setDepth(70)
Buildings5=Buildings.clone()
Buildings5.move(130,10)
Buildings5.setDepth(70)
Haneen.add(Buildings3)
Haneen.add(Buildings4)
Haneen.add(Buildings5)
Haneen.add(Buildings)
Haneen.add(Buildings2)
#add sky
blue=Rectangle(500,250,Point(250,0))
blue.setFillColor('lightblue')
blue.setDepth(80)
Haneen.add(blue)
#add grass
Green=Rectangle(500,250,Point(250,250))
Green.setFillColor('darkgreen')
Green.setDepth(80)
Haneen.add(Green)
#Add street
street=Rectangle(500,250,Point(250,500))
street.setFillColor('gray')
street.setDepth(70)
Haneen.add(street)
#Draw street markers
marker=Rectangle(80,20,Point(400,450))
marker.setFillColor('transparent')
marker.setBorderColor('white')
marker.setBorderWidth(3)
marker2=marker.clone()
marker2.move(-160,0)
marker3=marker.clone()
marker3.move(-320,0)
Haneen.add(marker)
Haneen.add(marker2)
Haneen.add(marker3)
#Draw Car 1
Car_body= Rectangle(200,50,Point(300,450))
Car_body.setBorderWidth(2)
Car_body.setFillColor('Red')
Car=Layer()
Car.add(Car_body)
car_windows=Polygon(Point(235,425),Point(275,380),Point(330,380),Point(370,425))
car_windows.setFillColor('lightblue')
Car.add(car_windows)
tire1=Circle(25,Point(375,475))
tire1.setFillColor('black')
tire1.setBorderColor('gray')
tire2=tire1.clone()
tire2.move(-145,0)
Car.add(tire1)
Car.add(tire2)
Haneen.add(Car)
Car.move(200,-30)


#Draw Car 2
Car_body2= Rectangle(200,50,Point(300,450))
Car_body2.setBorderWidth(2)
Car_body2.setFillColor('blue')
Car2=Layer()
Car2.add(Car_body2)
car_windows2=Polygon(Point(235,425),Point(275,380),Point(330,380),Point(370,425))
car_windows2.setFillColor('lightblue')
Car2.add(car_windows2)
tire11=Circle(25,Point(375,475))
tire11.setFillColor('black')
tire11.setBorderColor('gray')
tire21=tire11.clone()
tire21.move(-145,0)
Car2.add(tire11)
Car2.add(tire21)
Haneen.add(Car2)
Car2.move(100,-30)

#Draw Car 3
Car_body3= Rectangle(200,50,Point(300,450))
Car_body3.setBorderWidth(2)
Car_body3.setFillColor('yellow')
Car3=Layer()
Car3.add(Car_body3)
car_windows3=Polygon(Point(235,425),Point(275,380),Point(330,380),Point(370,425))
car_windows3.setFillColor('lightblue')
Car3.add(car_windows3)
tire12=Circle(25,Point(375,475))
tire12.setFillColor('black')
tire12.setBorderColor('gray')
tire22=tire11.clone()
tire22.move(-145,0)
Car3.add(tire12)
Car3.add(tire22)
Haneen.add(Car3)
Car3.move(-100,-30)


# Car1 Movement 
Car.move(-50,0)
Car2.move(-50,0)
Car3.move(-50,0)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/traffic1.mp3', True)
Car.move(-50,0)
Car2.move(-40,0)
Car3.move(-50,0)
sleep(2)
Car.move(-50,0)
Car2.move(-50,0)
Car3.move(-30,0)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/traffic2.mp3', True)
Car.move(-50,0)
Car2.move(-50,0)
Car3.move(-40,0)
sleep(2)
Car.move(-50,0)
Car2.move(-50,0)
Car3.move(-30,0)
playsound.playsound('C:/Users/Haneen/Desktop/Fall 2020/OOP Python/Programming Assigninment 1/needed files/traffic2.mp3', True)
Car.move(-50,0)
Car2.move(-50,0)
Car3.move(-20,0)

# Clear the scene for last caption
Haneen.remove(Buildings3)
Haneen.remove(Buildings)
Haneen.remove(Buildings2)
Haneen.remove(Buildings4)
Haneen.remove(Buildings5)
Haneen.remove(blue)
Haneen.remove(Green)
Haneen.remove(street)
Haneen.remove(Car)
Haneen.remove(Car2)
Haneen.remove(Car3)
Haneen.remove(marker)
Haneen.remove(marker2)
Haneen.remove(marker3)


# The end title
title=Text('The End.',20)
title.setFontColor('white')
title.move(250,250)

sleep(4)
Haneen.add(title)
