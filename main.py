import env
import sensors
import pygame
import math

# environment = env.buildEnvironment((600, 1200))
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     pygame.display.update()

environment = env.buildEnvironment((600, 1200))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(200,environment.originalMap, uncertainty=(0.5, 0.1))
environment.map.fill((0, 0, 0))
environment.infomap = environment.map.copy()

running = True

while running:
    sensorOn=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorOn = True
        elif not pygame.mouse.get_focused():
            sensorOn = False
    if sensorOn:
        position = pygame.mouse.get_pos()
        laser.position=position
        sensor_data = laser.sense_obstacles()
        environment.dataStorage(sensor_data)
        environment.show_sensor_data()
    environment.map.blit(environment.infomap, (0, 0))
    pygame.display.update()
