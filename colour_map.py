minecraft_colour_map = {
    (194,300,200):"minecraft:white_concrete",
    (117,117,107):"minecraft:light_gray_concrete",
    (50,54,58):"minecraft:gray_concrete",
    (7,8,14):"minecraft:black_concrete",
    (90,56,30):"minecraft:brown_concrete",
    (133,30,30):"minecraft:red_concrete",
    (210,91,1):"minecraft:orange_concrete",
    (226,160,20):"minecraft:yellow_concrete",
    (89,159,23):"minecraft:lime_concrete",
    (68,86,35):"minecraft:green_concrete",
    (21,112,128):"minecraft:cyan_concrete",
    (33,128,186):"minecraft:light_blue_concrete",
    (42,44,134):"minecraft:blue_concrete",
    (92,29,145):"minecraft:purple_concrete",
    (159,46,149):"minecraft:magenta_concrete",
    (200,94,133):"minecraft:pink_concrete"
}

minecraft_colours = minecraft_colour_map.keys()

def get_nearest_minecraft_colour(r,g,b):
    nearest_minecraft_colour = (0,0,0)
    min_two_norm = 195076 # (255-0)^3 + 1
    for minecraft_colour in minecraft_colours:
        two_norm = (minecraft_colour[0] - r)**2 + (minecraft_colour[1] - g)**2 + (minecraft_colour[2] - b)**2
        if two_norm < min_two_norm:
            min_two_norm = two_norm
            nearest_minecraft_colour = minecraft_colour
    return nearest_minecraft_colour