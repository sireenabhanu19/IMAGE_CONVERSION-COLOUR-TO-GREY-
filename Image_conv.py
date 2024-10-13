from PIL import Image

# Provide the path to the image
image_path = 'c:/Users/siree/Downloads/IMG_20230527_113645.jpg'

# Open the image
img = Image.open(image_path)

# Convert the image to grayscale
gimg = img.convert('L')

# Display the grayscale image
gimg.show()

# If you want to convert it back to RGB (uncomment the following lines if needed)
# cimg = img.convert('RGB')
# cimg.show()
