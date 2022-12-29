import pygame
import time
import random


class Coffee(pygame.sprite.Sprite):
    def __init__(self, cx, cy):
        super().__init__()
        self.image = pygame.image.load("Images\\coffee.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = [cx, cy]

class Player(pygame.sprite.Sprite):
    def __init__(self, cx, cy):
        super().__init__()
        self.image = pygame.image.load("Images\\cup.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 5, self.image.get_height() * 5))
        self.rect = self.image.get_rect()
        self.rect.center = [cx, cy]

pygame.init()
pygame.mixer.init()
wl, wb = 870, 600
window = pygame.display.set_mode((wl, wb))

pygame.display.set_caption("Coffe(No, its not a typo.) ~ UpBeat25_YT")

icon = pygame.image.load("Images\\coffee.png")
pygame.display.set_icon(icon)

music = pygame.mixer.music.load('Sound\\mixkit-raising-me-higher-34.wav') # NOQA

collect = pygame.mixer.Sound('Sound\\mixkit-player-jumping-in-a-video-game-2043.wav') # NOQA

pygame.mixer.music.play(-1)

def start_screen():
    pygame.init()
    y = (wb/2) - 180
    z = y
    idk = 1
    running = True
    clock = pygame.time.Clock()
    last_time = time.time()
    fps = 60

    random_x = random.randrange(0, wl - 20)
    random_y = random.randrange(10, 570)
    coffee = Coffee(random_x, random_y)
    coffe = pygame.sprite.Group()
    for i in range(20):
        coffee = Coffee(random_x, random_y)
        coffe.add(coffee)
        random_x = random.randrange(0, wl - 20)
        random_y = random.randrange(10, 570)

    while running:
        # delta time setup
        dt = time.time() - last_time
        dt *= fps
        last_time = time.time()
        clock.tick(fps)
        window.fill((128, 73, 58))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        coffee.update()
        coffe.draw(window)

        font = pygame.font.Font('Images\\CoffeeHealing-1GrKe.ttf', 300)
        font_idk = pygame.font.Font(None, 50)
        coffeee = font.render("Coffe", True, (255, 255, 255))
        press = font_idk.render("Press 'Space' to start.", True, (255, 255, 255))

        window.blit(coffeee, ((wl/2) - (coffeee.get_width())/2, y))

        window.blit(press, ((wl/2) - (press.get_width())/2, z + 400))

        y += idk

        if y - z > 50:
            idk *= -1

        if y == z - 2:
            idk *= -1

        user_input = pygame.key.get_pressed()

        if user_input[pygame.K_SPACE]:
            main()
            break

        pygame.display.update()
        pygame.time.delay(10)
    pygame.quit()

def main():
    pygame.init()
    x, y = wl / 2, 500
    player = Player(x, y)

    p_group = pygame.sprite.Group()
    p_group.add(player)

    score = 0

    random_x = random.randrange(0, wl - 20)
    random_y = random.randrange(-570, -50)
    coffee = Coffee(random_x, random_y)
    coffe = pygame.sprite.Group()
    for i in range(10):
        coffee = Coffee(random_x, random_y)
        coffe.add(coffee)
        random_x = random.randrange(0, wl - 20)
        random_y = random.randrange(-570, -50)

    running = True
    clock = pygame.time.Clock()
    last_time = time.time()
    fps = 60
    while running:
        # delta time setup
        dt = time.time() - last_time
        dt *= fps
        last_time = time.time()
        clock.tick(fps)
        # window color
        window.fill((128, 73, 58))
        speed = 5 * dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                splash_screen()
                break

        font = pygame.font.Font('Images\\CoffeeHealing-1GrKe.ttf', 50)
        coffeee = font.render(F": {score}", True, (255, 255, 255))

        window.blit(coffeee, (100, 20))

        # main game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.rect.centerx -= speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.rect.centerx += speed

        for drops in coffe:
            drops.rect.centery += 3
            if drops.rect.centery > wb:
                coffe.remove(drops)

            if player.rect.colliderect(drops.rect):
                coffe.remove(drops)
                collect.play()
                score += 1


        if len(coffe) < 10:
            for i in range(10):
                coffee = Coffee(random_x, random_y)
                coffe.add(coffee)
                random_x = random.randrange(0, wl - 20)
                random_y = random.randrange(-570, -50)

        window.blit(player.image, (20, 20))

        player.update()
        p_group.draw(window)
        coffee.update()
        coffe.draw(window)
        pygame.display.update()
        pygame.time.delay(10)
    pygame.quit()


def splash_screen():
    y = (wb/2) - 180
    z = y
    idk = 1
    running = True
    clock = pygame.time.Clock()
    last_time = time.time()
    fps = 60

    random_x = random.randrange(0, wl - 20)
    random_y = random.randrange(10, 570)
    coffee = Coffee(random_x, random_y)
    coffe = pygame.sprite.Group()
    for i in range(20):
        coffee = Coffee(random_x, random_y)
        coffe.add(coffee)
        random_x = random.randrange(0, wl - 20)
        random_y = random.randrange(10, 570)

    while running:
        # delta time setup
        dt = time.time() - last_time
        dt *= fps
        last_time = time.time()
        clock.tick(fps)
        window.fill((128, 73, 58))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        coffee.update()
        coffe.draw(window)

        font = pygame.font.Font('Images\\CoffeeHealing-1GrKe.ttf', 50)
        coffeee = font.render("Made by UpBeat25-YT", True, (255, 255, 255))

        window.blit(coffeee, ((wl/2) - (coffeee.get_width())/2, y))

        y += idk

        if y - z > 50:
            idk *= -1

        if y == z - 2:
            idk *= -1

        pygame.display.update()
        pygame.time.delay(10)
    pygame.quit()

if __name__ == '__main__':
    start_screen()
