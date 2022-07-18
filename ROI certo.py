import cv2

   
camera = cv2.VideoCapture(0)
  
background = None
   
   
while True:
  _, frame = camera.read()
  imagemInvertida = cv2.flip(frame, -1)
  roi = imagemInvertida[160:320, 160:320]
  
  
  
  if background is None:
    background = roi
    continue
  
  
  
  cv2.rectangle(imagemInvertida, (160,320), (320,160), (0,0,255), 1)
       
  cv2.imshow('Minha Camera', imagemInvertida)
  cv2.imshow('ROI', roi)
    
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

camera.release()
cv2.destroyAllWindows()