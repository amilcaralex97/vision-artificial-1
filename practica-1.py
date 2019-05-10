import numpy as np
import cv2 

mano='./img/mano.jpg'
manos='./img/manos.jpeg'
ok='./img/ok.jpeg'

img = cv2.imread(mano)#r+g+b/3
gaussiana = cv2.GaussianBlur(img, (5,5), 0)
b,g,r=cv2.split(gaussiana)
be,ge,re=cv2.split(gaussiana)
bc,gc,rc=cv2.split(gaussiana)

""" Esta es el chido dido """
bc=np.array(bc)
gc=np.array(gc)
rc=np.array(rc)
"""----------------------------------------------------------------------------------------------------------  """


pb=bc+1/((bc+gc+rc+1)*255)

pr=rc+1/((bc+gc+rc+1)*255)

pg=gc+1/((bc+gc+rc+1)*255)


pb=np.where(pb>250,0,255*256)
pb=pb*1.5
pg=np.where(pg>250,0,255*256)
pg=pg*1.5
pr=np.where(pr>250,0,255*256)
pr=pr*1.5

""" Este tiene brillocro """
be=np.array(be)
be=(6/5)*be

ge=np.array(ge)
ge=(6/5)*ge

re=np.array(re)
re=(6/5)*re

be=np.where(be>240,0,255*256)
ge=np.where(ge>230,0,255*256)
re=np.where(re>250,0,255*256)
""" normalon 1 y 0s """
 
b=np.where(b>240,0,255*256)
g=np.where(g>230,0,255*256)
r=np.where(r>250,0,255*256)

escalar=cv2.merge((be,ge,re))
nueva= cv2.merge((b,g,r))
chida=cv2.merge((pb,pg,pr))


cv2.imshow("original",gaussiana)
cv2.imshow("brillo",escalar)
cv2.imshow("imgsinbrillo",nueva)
cv2.imshow("chida",chida)
cv2.waitKey(0)
cv2.destroyAllWindows()