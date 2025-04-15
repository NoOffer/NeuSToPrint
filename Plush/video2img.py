import cv2
from PIL import Image
from rembg import remove

def remove_background(image):
    # Processing the image 
    input = image.convert('RGBA')
      
    # Removing the background from the given Image 
    output = remove(input).convert('RGB')
    output.save(f'ran_no_bg/IMG{str(i).zfill(3)}.jpeg')
 
def extract_frames(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)
 
    frames = []
    success, frame = video.read()
     
    # Iterate over each frame in the video
    while success:
        # Append the current frame to the list
        frames.append(frame)
         
        # Read the next frame
        success, frame = video.read()
 
    # Release the video capture object
    video.release()
 
    return frames
 
# Usage
video_path = 'ran.mp4'
all_frames = extract_frames(video_path)

for i, frame in enumerate(all_frames):
    if i % 1 == 0:
        im = Image.fromarray(frame)
        r, g, b = im.split()
        im_rgb = Image.merge('RGB', (b, g, r))
        remove_background(im_rgb)
        # im_rgb.save(f'ran/IMG{str(i).zfill(3)}.jpeg')