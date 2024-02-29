def invert_colors(image_path):
    """Inverte as cores da imagem."""
    from PIL import Image
    image = Image.open(image_path)
    inverted_image = Image.eval(image, lambda x: 255 - x)
    return inverted_image