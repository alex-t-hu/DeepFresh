from PIL import Image, ImageDraw
import os

def show_bbox(image_path, label_path):
    # convert image path to label path

    # Open the image and create ImageDraw object for drawing
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    with open(label_path, 'r') as f:
        for line in f.readlines():
            # Split the line into five values
            label, x, y, w, h = line.split(' ')

            # Convert string into float
            x = float(x)
            y = float(y)
            w = float(w)
            h = float(h)

            # Convert center position, width, height into
            # top-left and bottom-right coordinates
            W, H = image.size
            x1 = (x - w/2) * W
            y1 = (y - h/2) * H
            x2 = (x + w/2) * W
            y2 = (y + h/2) * H

            # Draw the bounding box with red lines
            draw.rectangle((x1, y1, x2, y2),
                           outline=(255, 0, 0), # Red in RGB
                           width=5)             # Line width
    image.show()

path = 'C:\\Users\\Risha\\Downloads\\dataset\\yolotest'
show_bbox(os.path.join(path, 'freshtomato', 'freshtomato70.jpg'), os.path.join(path, 'freshtomatolabel', 'freshtomato70.txt'))