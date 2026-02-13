################################## Day 56: 69 Days of Python #####################################
# Intro to OpenCV - Reading Images & Videos

import cv2

def read_image(image_path:str):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: could not load image.")
        return
    
    cv2.imshow("Image preview",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    read_image("sample.jpeg")