# https://chat.openai.com/share/2dedcf53-d4b9-4779-8981-26cd45b0581e

# HOW TO USE
# When downloading a photo, temporarily add it to the /assets/Scaled photo, then run the script
# This will only scale the images in the Scaled photo
# Do not run twice, or the photo will be scaled down again
# Then, move from the folder to the desired location
# I could have had it where it renames all photos with a "_scaled" on the end (commented out below)
# But then I would have had to change the images in every single post file to reflect this
# Plus, then when going through the images to chamge, it would still have to loop through every single image file
# Just skipping over the ones already scaled
# Which would be slow
# This way it's more efficient, and only goes through the exact photos it needs to

import os
from PIL import Image

os.system('cls')

def scale_images_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith("_scaled.jpg") or filename.endswith("_scaled.JPG") or filename.endswith("_scaled.png"):
                continue
            elif filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".png"):
                filepath = os.path.join(root, filename)
                try:
                    img = Image.open(filepath)
                    
                    # Check for EXIF orientation and rotate if necessary
                    exif = img._getexif()
                    if exif:
                        orientation = exif.get(0x0112)
                        if orientation == 3:
                            img = img.rotate(180, expand=True)
                        elif orientation == 6:
                            img = img.rotate(270, expand=True)
                        elif orientation == 8:
                            img = img.rotate(90, expand=True)
                    
                    # Resize the image
                    width, height = img.size
                    new_width = int(width * 0.25)
                    new_height = int(height * 0.25)
                    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
                    # filepath = filepath[0:-4] + "_scaled.jpg"
                    resized_img.save(filepath)
                    print(f"{filename} scaled successfully")
                except Exception as e:
                    print(f"Error scaling {filename}: {e}")

# Replace 'path_to_your_directory' with the path to the directory containing your JPG images
directory_path = r'C:\Users\mets1\Documents\website\assets\Scaled'
# directory_path = r'C:\Users\mets1\Documents\GitHub\pscally1005.github.io\assets\Scaled'
scale_images_in_directory(directory_path)
