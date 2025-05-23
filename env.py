import math
import pygame

class buildEnvironment:
    def __init__(self, MapDimensions):
        self.pointcloud = []
        self.externalMap=pygame.image.load("map.png")
        self.maph, self.mpw = MapDimensions
        self.MapWindowName = "RRT Path Planning"
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mpw, self.maph))
        self.map.blit(self.externalMap, (0, 0))

        # Colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)  
        self.green = (0, 255, 0)    
        self.blue = (0, 0, 255) 
        self.yellow = (255, 255, 0) 
        self.purple = (128, 0, 128)
        self.grey = (128, 128, 128)

    def AS2pos(self, distance, angle, robotPosition):
        x = distance * math.cos(angle) + robotPosition[0]
        y = distance * math.sin(angle) + robotPosition[1]
        return (int(x), int(y))
    
    def dataStorage(self, data):
        print(len(self.pointcloud))
        for element in data:
            point = self.AS2pos(element[0], element[1], element[2])
            if point not in self.pointcloud:
                self.pointcloud.append(point)

    def show_sensor_data(self):
        self.infomap=self.map.copy()
        for point in self.pointcloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))


