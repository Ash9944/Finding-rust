import cv2
import numpy as np

#Read the Rust Photograph
img = cv2.imread(r'C:\Users\HP\imageprocessing\resources\rust-1-e1488346306943-1288x724.jpg', 1)

#Set different boundaries for different shades of rust
boundaries1 = [ ([58, 57, 101], [76, 95, 162]) ]
boundaries2 = [ ([26, 61, 111], [81, 144, 202]) ]
boundaries3 = [ ([44, 102, 167], [115, 169, 210]) ]

#Highlight out the shades of rust
for (lower1, upper1) in boundaries1:
    lower1 = np.array(lower1, dtype = "uint8")
    upper1 = np.array(upper1, dtype = "uint8")
    mask = cv2.inRange(img, lower1, upper1)
    output1 = cv2.bitwise_and(img, img, mask = mask)

for (lower2, upper2) in boundaries2:
    lower2 = np.array(lower2, dtype = "uint8")
    upper2 = np.array(upper2, dtype = "uint8")
    mask = cv2.inRange(img, lower2, upper2)
    output2 = cv2.bitwise_and(img, img, mask = mask)

for (lower3, upper3) in boundaries3:
    lower3 = np.array(lower3, dtype = "uint8")
    upper3 = np.array(upper3, dtype = "uint8")
    mask = cv2.inRange(img, lower3, upper3)
    output3 = cv2.bitwise_and(img, img, mask = mask)

#Combine the 3 different masks with the different shades into 1 image file
final = cv2.bitwise_or(output1, output2, output3)
cv2.imshow("Rusted patterns", final)
cv2.waitKey(0)