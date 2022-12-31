import time
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y, l, b, flip_x=False, flip_y=False):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (l, b))
        self.image = pygame.transform.flip(self.image, flip_x, flip_y)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class Orb(pygame.sprite.Sprite):
    def __init__(self, image, x, y, l, b):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (l, b))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

pygame.init()
pygame.mixer.init()
wl, wb = 1000, 600
window = pygame.display.set_mode((wl, wb))

pygame.display.set_caption("Orbs")  # You can set a custom name

icon = pygame.image.load("images\\orb_2.png")  # Enter file location with name
pygame.display.set_icon(icon)

# FPS
FPS = 60

bg = pygame.image.load("images\\bg.png")
bg = pygame.transform.scale(bg, (wl, wb + 50))

music = pygame.mixer.music.load('sound\\mixkit-driving-ambition-32.wav') # NOQA

hit = pygame.mixer.Sound('sound\\mixkit-metal-hammer-hit-833.wav') # NOQA

explode = pygame.mixer.Sound('sound\\mixkit-bomb-explosion-in-battle-2800.wav') # NOQA

pygame.mixer.music.play(-1)

def start_screen():
    pygame.init()
    y = (wb/2) - 180
    z = y
    idk = 1
    y_b = -50

    idk_g = 0.5
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
        window.fill((128, 73, 58))
        window.blit(bg, (0, y_b))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        font = pygame.font.Font('images\\Monocraft-nerd-fonts-patched.ttf', 300)
        font_idk = pygame.font.Font(None, 50)
        coffeee = font.render("Orbs", True, (255, 255, 255))
        press = font_idk.render("Press 'Space' to start.", True, (255, 255, 255))

        window.blit(coffeee, ((wl/2) - (coffeee.get_width())/2, y))

        window.blit(press, ((wl/2) - (press.get_width())/2, z + 400))

        y += idk

        if y - z > 50:
            idk *= -1

        if y == z - 2:
            idk *= -1

        y_b += idk_g

        if y_b >= 0:
            idk_g *= -1

        if y_b < -50:
            idk_g *= -1

        user_input = pygame.key.get_pressed()

        if user_input[pygame.K_SPACE]:
            main()
            break

        pygame.display.update()
        pygame.time.delay(10)
    pygame.quit()


def main():

    player_group = pygame.sprite.Group()
    player_1 = Player("images\\Space_ship_1.png", 150, 300, 72*3, 42*3, False, False)
    player_2 = Player("images\\Space_ship_2.png", wl - 150, 300, 72*3, 42*3, True, False)

    player_group.add(player_1, player_2)

    orbs = pygame.sprite.Group()

    orb_1 = Orb("images\\orb_1.png", player_1.rect.centerx, player_1.rect.centery, 64, 64)
    orb_2 = Orb("images\\orb_2.png", player_2.rect.centerx, player_2.rect.centery, 64, 64)

    orbs.add(orb_1, orb_2)

    y = -50

    idk = 0.5

    speed = 4.3

    attack_1 = False

    attack_2 = False

    score_1, score_2 = 0, 0

    running = True
    clock = pygame.time.Clock()
    last_time = time.time()
    while running:
        # delta time setup
        dt = time.time() - last_time
        dt *= FPS
        last_time = time.time()
        clock.tick(FPS)
        # window color
        window.fill((128, 128, 128))
        window.blit(bg, (0, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                splash_screen()
                running = False

        font = pygame.font.Font(None, 100)
        score_tag = font.render(F"P1: {score_1}", True, (0, 96, 202))
        window.blit(score_tag, (200, 10))

        score2_tag = font.render(F"P2: {score_2}", True, (196, 18, 0))
        window.blit(score2_tag, (610, 10))

        pygame.draw.line(window, (255, 255, 255), (500, 0), (500, wb), 3)

        y += idk

        if y >= 0:
            idk *= -1

        if y < -50:
            idk *= -1

        keys = pygame.key.get_pressed()

        orb_1.rect.centery = player_1.rect.centery
        orb_2.rect.centery = player_2.rect.centery

        if keys[pygame.K_w] and player_1.rect.centery >= 0 + player_1.image.get_height()/2 and attack_1 is False:
            player_1.rect.centery -= speed * dt

        if keys[pygame.K_s] and player_1.rect.centery <= wb - player_1.image.get_height()/2 and attack_1 is False:
            player_1.rect.centery += speed * dt

        if keys[pygame.K_UP] and player_2.rect.centery >= 0 + player_2.image.get_height()/2 and attack_2 is False:
            player_2.rect.centery -= speed * dt

        if keys[pygame.K_DOWN] and player_2.rect.centery <= wb - player_2.image.get_height()/2 and attack_2 is False:
            player_2.rect.centery += speed * dt

        if keys[pygame.K_LSHIFT]:
            attack_1 = True

        if keys[pygame.K_RSHIFT]:
            attack_2 = True

        if attack_1 is True:
            orb_1.rect.centerx += speed * dt * 2
            if orb_1.rect.colliderect(player_2.rect):
                score_1 += 1
                hit.play()
                orb_1.rect.centerx = player_1.rect.centerx
                attack_1 = False

            if orb_1.rect.centerx >= wl:
                orb_1.rect.centerx = player_1.rect.centerx
                attack_1 = False

        if attack_2 is True:
            orb_2.rect.centerx -= speed * 2 * dt
            if orb_2.rect.colliderect(player_1.rect):
                score_2 += 1
                hit.play()
                orb_2.rect.centerx = player_2.rect.centerx
                attack_2 = False

            if orb_1.rect.centerx <= 0:
                orb_2.rect.centerx = player_2.rect.centerx
                attack_2 = False

        if orb_1.rect.colliderect(orb_2):
            explode.play()
            score_2 -= 1
            score_1 -= 1
            orb_2.rect.centerx = player_2.rect.centerx
            orb_1.rect.centerx = player_1.rect.centerx
            attack_2, attack_1 = False, False

        orb_1.update()
        orb_2.update()
        orbs.draw(window)
        player_1.update()
        player_2.update()
        player_group.draw(window)
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

    while running:
        # delta time setup
        dt = time.time() - last_time
        dt *= fps
        last_time = time.time()
        clock.tick(fps)
        window.fill((20, 32, 53))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        font = pygame.font.Font('images\\CoffeeHealing-1GrKe.ttf', 50)
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
