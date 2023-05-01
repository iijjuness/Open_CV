import cv2

# read two images
img1 = cv2.imread('lec9_field.bmp')
img2 = cv2.imread('lec9_airplane.bmp')

# set alpha value
alpha = 1

# create an empty list to store output images
output_images = []

# loop through a range of values for alpha
for i in range(1):
    # calculate beta value
    beta = 1 - alpha

    # apply addWeighted
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)

    # append output to list
    output_images.append(output)

    # increment alpha value
    alpha += 0.05

# display the output images
for i, output in enumerate(output_images):
    cv2.imwrite(f'{i}.bmp', output)
    cv2.imshow(f'Output {i}', output)
    cv2.waitKey()

cv2.destroyAllWindows()
