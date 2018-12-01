import numpy as np
import cv2
import os


def div_imgs(filename1,filename2):
    img1 = cv2.imread(filename1, 0)  
    img2 = cv2.imread(filename2, 0)

    
    rows, cols = img1.shape
    img3 = np.zeros([rows,cols], dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            val = img1[i,j]/img2[i,j]
            if(val>255):
                    val = 255
            else:
                if(val<0):
                    val = 0
                
            img3[i,j] = val
    name, extension = os.path.splitext(filename1)
    
    newname = "{name}-Div{ext}".format(name=name, ext=extension)
    cv2.imwrite(newname, img3)
    img  = cv2.imread(newname,0)
    cv2.imshow(newname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":