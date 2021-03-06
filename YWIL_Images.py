from PIL import ImageTk, Image

url_route = 'Resources/'
url_prefix = url_route + 'Step_'

color_images = []

for n in range(8):
    image_url = url_prefix + str(n) + '_50.jpg'
    color_images.append(ImageTk.PhotoImage(Image.open(image_url)))

alpha_images = []

for n in range(8):
    image_url = url_prefix + str(n) + '_50_alpha.png'
    alpha_images.append(ImageTk.PhotoImage(Image.open(image_url)))

validation_names = ['yes', 'no', 'aux']

progress_images = {}

for validation_name in validation_names:
    image_url = url_prefix + validation_name + '_60.png'
    progress_images[validation_name] = ImageTk.PhotoImage(Image.open(image_url))

assembly_images = []

for n in range(8):
    image_url = url_prefix + str(n) + '.jpg'
    assembly_images.append(ImageTk.PhotoImage(Image.open(image_url)))

validation_images = {}

for validation_name in validation_names:
    image_url = url_prefix + validation_name + '.png'
    validation_images[validation_name] = ImageTk.PhotoImage(Image.open(image_url))

assembly_name = 'AssemblyCompleted'

completed_image = url_route + assembly_name + '.png'
completed_mask = url_route + assembly_name + '_mask.png'