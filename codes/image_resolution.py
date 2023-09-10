from PIL import Image
  
# Open the image by specifying the image path.
image_path = "./test_img/image_name.jpg"
image_file = Image.open(image_path)
  
# the default
image_file.save("./test_img/image_name1.jpg", quality=500)
  
# Changing the image resolution using quality parameter
