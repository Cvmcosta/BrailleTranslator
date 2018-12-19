import cv2
import numpy as np
import math

th2=cv2.imread('preprocessing/roi.jpg')
r,c,w=th2.shape
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (c+2000,25))
horizontal = cv2.dilate(th2, horizontalStructure, (-1, -1))
cv2.imwrite("horizontal/horizontal2.jpg", horizontal)


img = cv2.imread('horizontal/horizontal2.jpg')


edges = cv2.Canny(img,200,400,apertureSize = 3)
cv2.imwrite('horizontal/edges.jpg',edges)



m=[]

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength,maxLineGap)
for x in range(0, len(lines)):
        for x1,y1,x2,y2 in lines[x]:
                m.append(((x1,y1),(x2,y2)))



sorted_m=sorted(m, key=lambda x: x[0][1])

    


sorted_m.insert(0,((0,0),(c,0)))
#drawing line
for i in range (0,len(sorted_m)):
    cv2.line(th2,sorted_m[i][0],sorted_m[i][1],(0,0,255),3)
    
        
cv2.imwrite('horizontal/hough_lines.png',th2)


s=cv2.imread('horizontal/hough_lines.png')
p=[]
for i in range (0,len(sorted_m)):
    if i!=len(sorted_m)-1:
        p.append(th2[sorted_m[i][0][1]:sorted_m[i+1][0][1],sorted_m[i][0][0]:sorted_m[i][1][0]])
    else:
        p.append(th2[sorted_m[len(lines)-2][0][1]:r, sorted_m[len(lines)][0][0]:sorted_m[len(lines)][1][0]])

pix=[]


for x in range(len(p)):
    def contains_white(img):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, threshold = cv2.threshold(gray_image,100,255,cv2.THRESH_BINARY)
        h,w,l=img.shape
        for i in range(h):
            for j in range(w):
                if threshold[i][j]==255:
                    return True
            



    result= contains_white(p[x])
    if result== True:
        pix.append(p[x])

    

for i in range(len(pix)-1):
    cv2.imwrite('horizontal/part' +str(i)+'.jpg',pix[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
