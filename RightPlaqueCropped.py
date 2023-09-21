from PIL import Image
import os

def crop_image(input_path, output_path, left, top, right, bottom):
    try:
        # Open the input image
        image = Image.open(input_path)

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Save the cropped image
        cropped_image.save(output_path)

        print(f"Image cropped and saved to {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")

def crop_all_images_in_folder(input_folder, output_folder, left, top, right, bottom):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all .jpg files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith("_2.jpg"):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            crop_image(input_image_path, output_image_path, left, top, right, bottom)

if __name__ == "__main__":
    input_folder = "/data/circ_ukb/RightPlaque"  # Replace with the path to your input folder
    output_folder = "/data/circ_ukb/RightPlaqueCropped"  # Replace with the path to your output folder

    # Specify the crop coordinates (left, top, right, bottom)
    crop_left = 275
    crop_top = 100
    crop_right = 750
    crop_bottom = 600

    crop_all_images_in_folder(input_folder, output_folder, crop_left, crop_top, crop_right, crop_bottom)
