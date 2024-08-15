stage.set_background("space")
earth = codesters.Sprite("earth")
earth.set_size(0.4)
spaceship = codesters.Sprite("SpaceShip_f07")
spaceship.set_size(0.5)

score = 0
lives = 5
earth_lives = 5
score_board = codesters.Display(score, 200, 200)
lives_board = codesters.Display(lives, -200, 200)
earth_lives_board = codesters.Display(earth_lives, -200, -200)


def teleport(x_pos, y_pos):
    if x_pos > 270:
        spaceship.go_to(-260, y_pos)
    if y_pos > 270:
        spaceship.go_to(x_pos, -260)
    if x_pos < -270:
        spaceship.go_to(260, y_pos)
    if y_pos < -270:
        spaceship.go_to(x_pos, 260)

def shoot():
    x_ship = spaceship.get_x()
    y_ship = spaceship.get_y()
    dir_ship = spaceship.get_direction()
    
    laser = codesters.Sprite("Laser_3b5", x_ship, y_ship)
    laser.set_speed(10)
    
    laser.rotate_about(dir_ship, x_ship, y_ship)
    laser.move_forward(1000)
stage.event_key("space", shoot)

def move_forward():
    x_pos = spaceship.get_x()
    y_pos = spaceship.get_y()
    spaceship.move_forward(25)
    teleport(x_pos, y_pos)

def move_back():
    x_pos = spaceship.get_x()
    y_pos = spaceship.get_y()
    spaceship.move_back(25)
    teleport(x_pos, y_pos)

def turn_right():
    spaceship.turn_right(70)
    
def turn_left():
    spaceship.turn_left(70)

stage.event_key("up", move_forward)
stage.event_key("down", move_back)
stage.event_key("left", turn_left)
stage.event_key("right", turn_right)

respawn_list = [-270, 270]


def asteroids_spawn():
    asteroid = codesters.Sprite("asteroid", random.choice(respawn_list), random.choice(respawn_list))
    asteroid.event_collision(asteroids_collision)
    asteroid.set_speed(1)
    asteroid.set_size(0.9)
    asteroid.glide_to(earth.get_x(), earth.get_y())
    
def asteroids_collision(sprite, hit_sprite):
    global lives, earth_lives, score
    name = hit_sprite.get_image_name()
    
    if name == "Spaceship_f07":
        stage.remove_sprite(sprite)
        lives -= 1
        lives_board.update(lives)
        if lives <= 0:
            text = codesters.Text("You Lose", 0, 0, "red")
            stage.remove_all_events()
    if name == "earth":
        stage.remove_sprite(sprite)
        earth_lives -= 1
        earth_lives_board.update(earth_lives)
        if earth_lives <= 0:
            text = codesters.Text("You Lose", 0, 0, "red")
            stage.remove_all_events()
    if name == "Laser_3b5":
        sprite.set_size(sprite.get_size() - 0.1)
        if sprite.get_size() < 0.1:
            stage.remove_sprite(sprite)
            score += 1
            score_board.update(score)
            if score == 10:
                text = codesters.Text("You Win!!!", 0, 0, "green")
                stage.remove_all_events()

stage.event_interval(asteroids_spawn, 3)

