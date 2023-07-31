import cv2
import os


def create_video_from_image_sequence(image_folder, output_video_path, frame_rate=60):
    if not os.path.exists(image_folder) or not os.path.isdir(image_folder):
        raise ValueError("Invalid image folder path. Please provide a valid directory path.")

    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))])
    if not image_files:
        raise ValueError("No valid image files found in the specified folder.")

    # Get the dimensions of the first image to set video size
    first_image_path = os.path.join(image_folder, image_files[0])
    first_image = cv2.imread(first_image_path)
    height, width, _ = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    video_writer.release()
    print("Video successfully created!")


if __name__ == "__main__":
    try:
        image_sequence_folder = "./t"  # path to images folder
        output_video_path = "output_video.avi"
        create_video_from_image_sequence(image_sequence_folder, output_video_path)
    except Exception as e:
        print(f"Error: {e}")
