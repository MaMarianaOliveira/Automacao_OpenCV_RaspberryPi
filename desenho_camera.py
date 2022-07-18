import cv2

camera = cv2.VideoCapture(0)

while True:
    _,frame = camera.read()
    
    imagemInvertida = cv2.flip(frame,1)
    
    frameComLinha = cv2.line(imagemInvertida,(0,0),(640,480),(0,255,0),5)
    
    frameComRetangulo = cv2.rectangle(imagemInvertida,(10,240),(280,460),(255,0,0),3)
    
    cv2.imshow('Minha Camera', frameComLinha)
    
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
    