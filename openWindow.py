import pygame
import webbrowser
import independentWork


pygame.init()
def startGame(service):
    is_running = True

    class Button():
        def __init__(self,x,y,image,scale):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)

        def draw(self):
            mousePos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mousePos):
                if pygame.mouse.get_pressed()[0] == 1:
                    independentWork.organisePrivates(service)
            #blit draws object to screen at coords taken by argument2
            screen.blit(self.image, (self.rect.x, self.rect.y))

    class webButton(Button):
        def draw(self):
            mousePos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mousePos):
                if pygame.mouse.get_pressed()[0] == 1:
                    webbrowser.open("https://calendar.google.com/calendar/u/0/r")
                    
            #blit draws object to screen at coords taken by argument2
            screen.blit(self.image, (self.rect.x, self.rect.y))
    
    class powerButton(Button):
        def draw(self):
            mousePos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mousePos):
                if pygame.mouse.get_pressed()[0] == 1:
                    webbrowser.open("https://www.youtube.com/watch?v=dI_XEPoN3MA&ab_channel=Razbuten")
                    
            #blit draws object to screen at coords taken by argument2
            screen.blit(self.image, (self.rect.x, self.rect.y))

    screenWidth = 1280
    screenHeight =720

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Sort Calendar")

    icon = pygame.image.load("icon.png")
    buttonImage = pygame.image.load("button.png")
    powerImage = pygame.image.load("powerOff.webp")

    pygame.display.set_icon(icon)

    
    #Creates instance of a button
    buttons = [
        Button(527,280,buttonImage,0.3),
        webButton(300,280,icon,.1),
        powerButton(100, 500, powerImage, 0.5)
    ]
    is_running = True
    while is_running:

        screen.fill((202,228,241))

        for i in buttons:
            i.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        pygame.display.update()