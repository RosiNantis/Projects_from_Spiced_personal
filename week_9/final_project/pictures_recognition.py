import sys
import logging
import os
import cv2
from utils import write_image, key_action, init_cam
from tensorflow.keras.models import load_model
import time
import numpy as np
from tensorflow.keras.preprocessing import image # Keras own inbuild image class
from skimage.transform import resize

# Load model
model = load_model("model_mobilinet_v2.h5")

#load classes
mapping = {'plants' : 0,'coins' : 1,'faces' : 2,'cups' : 3,'glasses' : 4,'pens' : 5,'gestures' : 6,'cutlery' : 7,'plates' : 8, 
             'nail_polishes' : 9  ,'shoes' : 10 
             }


if __name__ == "__main__":

    # folder to write images to
    out_folder = sys.argv[1]

    # maybe you need this
    os.environ['KMP_DUPLICATE_LIB_OK']='True'

    logging.getLogger().setLevel(logging.INFO)
   
    # also try out this resolution: 640 x 360
    webcam = init_cam(640, 480)
    key = None

    try:
        # q key not pressed 
        while key != 'q':
            # Capture frame-by-frame
            ret, frame = webcam.read()
            # fliping the image 
            frame = cv2.flip(frame, 1)
   
            # draw a [224x224] rectangle into the frame, leave some space for the black border 
            offset = 2
            width = 224
            x = 160
            y = 120
            cv2.rectangle(img=frame, 
                          pt1=(x-offset,y-offset), 
                          pt2=(x+width+offset, y+width+offset), 
                          color=(0, 0, 0), 
                          thickness=2
            )     
            
            # get key event
            key = key_action()
            if key == 'space':
                # write the image without overlay
                # extract the [224x224] rectangle out of it
                img = frame[y:y+width, x:x+width, :]
                #write_image(out_folder, img) 
                #convert image to array, can also specify datatype
                #print(type(img))
                img = image.img_to_array(img,dtype='uint8')
                image_cam = img.reshape(1,224,224,3)
                ynew = model.predict(image_cam)
                # show the inputs and predicted outputs
                
                for idx, value in enumerate(ynew):
                    print(f'With {np.max(value)} probability the model predicts that it is a {list(mapping)[np.where(value == np.max(value))[0][0]]}.')#

            # disable ugly toolbar
            cv2.namedWindow('frame', flags=cv2.WINDOW_GUI_NORMAL)              
            
            # display the resulting frame
            cv2.imshow('frame', frame) 


 

            
    finally:
        # when everything done, release the capture
        logging.info('quit webcam')
        webcam.release()
        cv2.destroyAllWindows()
