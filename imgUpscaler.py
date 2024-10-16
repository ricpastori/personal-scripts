import os, argparse
from PIL import Image

def upscale_image(input_folder, scale_factor=2):
    # Create the output folder if it doesn't exist
    output_folder='Upscaled-images'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Build the full input file path
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image (supported formats: jpg, png, etc.)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Open the image
            img = Image.open(input_path)

            # Get original image dimensions
            width, height = img.size

            # Calculate new dimensions based on the scale factor
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)

            # Resize the image using LANCZOS filter (high-quality filter for upscaling)
            upscaled_img = img.resize((new_width, new_height), Image.LANCZOS)

            # Build the full output file path
            output_path = os.path.join(output_folder, filename)

            # Save the upscaled image
            upscaled_img.save(output_path)

            print(f"Upscaled image: {filename}, new size: {new_width}x{new_height}")

# Parse command arguments
parser = argparse.ArgumentParser()
parser.add_argument('--directory',type=str, help='Path to the input files')
parser.add_argument('--scale', type=int, help="Scale factor to enlarge images")
args = parser.parse_args()


# Run the image upscaling process
if not args.directory:
    if args.scale:
        upscale_image(os.getcwd(), args.scale)
    else:
        upscale_image(os.getcwd())
else:
    if args.scale:
        upscale_image(args.directory, args.scale)
    else:
        upscale_image(args.directory)
