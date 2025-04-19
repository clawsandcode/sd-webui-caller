from PIL import Image

def display_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"Error opening image: {e}")