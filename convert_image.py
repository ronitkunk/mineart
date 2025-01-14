from PIL import Image
import colour_map

def create_commands(n=40, image_path="data/dog.jpg", starting_coordinates=(0, 0), y=-60):
    image = Image.open(image_path)
    image = image.convert("RGB")
    width, height = image.size

    output_file=open("commands.txt", "w")

    if width < height:
        image = image.resize((n, (height*n)//width))
    else:
        image = image.resize(((width*n)//height, n))

    width, height = image.size

    for i in range(height):
        for j in range(width):
            r, g, b = image.getpixel((j, i))
            minecraft_r, minecraft_g, minecraft_b = colour_map.get_nearest_minecraft_colour(r, g, b)
            output_file.write(f"setblock {starting_coordinates[0]+j} {y} {starting_coordinates[1]+i} {colour_map.minecraft_colour_map.get((minecraft_r, minecraft_g, minecraft_b))}\n")
            print(f"creating commands, {((i+1)*100)//height}% completed", end="\r")

    output_file.close()

if __name__ == "__main__":
    create_commands()