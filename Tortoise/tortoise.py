import turtle
import urllib.request
from PIL import Image


def download_grass_pic(image_name):
    """ Downloads grass image from photobucket
        and saves as @image_name"""
    url = "http://i171.photobucket.com/albums/u288/ilybbygrlx3/grass.gif"
    urllib.request.urlretrieve(url, image_name)


def resize_image(image_name, size):
    """ Resizes image @image_name
        to given @size """
    img = Image.open(image_name)
    img = img.resize((size, size), Image.ANTIALIAS)
    img.save(image_name)


def draw_square(square_turtle, edge_size):
    # Initiate drawing sequence
    for i in range(4):
        square_turtle.forward(edge_size)
        square_turtle.left(90)


def draw_circle(circle_turtle, size):
    circle_turtle.circle(size)


def draw_circle_with_squares(cws_turtle, edge_size, degrees):
    steps = int(360/degrees)
    for i in range(steps):
        draw_square(cws_turtle, edge_size)
        cws_turtle.left(degrees)


def draw_triangle(triangle_turtle, edge_size):
    for i in range(3):
        triangle_turtle.forward(100)
        triangle_turtle.left(120)

if __name__ == "__main__":
    # Initialize Brad the Turtle
    # Actually it should be a tortoise since it moves on the ground
    # But let's follow the "Turtle" convention for library's name sake
    size = 600
    background_name = "background.gif"
    window = turtle.Screen()
    window.setup(size, size)

    download_grass_pic(background_name)
    resize_image(background_name, size)
    window.bgpic(background_name)

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("brown")
    brad.shapesize(1.2, 1.2, 5)
    brad.speed(0.5)
    draw_square(brad, 200)

    angie = turtle.Turtle()
    angie.color("blue")
    draw_circle(angie, 100)

    donna = turtle.Turtle()
    donna.color("yellow")
    draw_circle_with_squares(donna, edge_size = 100, degrees = 10)

    jackie = turtle.Turtle()
    jackie.color("black")
    draw_triangle(jackie, 100)

    window.exitonclick()

