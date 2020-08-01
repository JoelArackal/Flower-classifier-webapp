from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
import os

def imgp(img):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_DIR = os.path.join(BASE_DIR,'media/profile_pics')
    image = os.path.join(MEDIA_DIR,str(img))
    image1 = plt.imread(image)
    print(image1.shape)

#imgp('14351620_f1024.jpg')  
# 
from tensorflow.keras.optimizers import RMSprop

class classification():
    model = tf.keras.models.Sequential([
    #First Convolution
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # The second convolution
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The third convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fourth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fifth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(20, activation='softmax')
        ])
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # from tensorflow.keras.optimizers import RMSprop

    model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['accuracy'])
    checkpoint_path = os.path.join(BASE_DIR,'media/training_miniproj/cp.cpkt')
    #checkpoint_dir = os.path.dirname(checkpoint_path)

    model.load_weights(checkpoint_path)

    def pred(self,img):
        MEDIA_DIR = os.path.join(self.BASE_DIR,'media')
        imagep = os.path.join(MEDIA_DIR,str(img))
        
        

        from tensorflow.keras.preprocessing import image

        # img = image.load_img('images/train/5/image_05170.jpg', target_size=(300, 300))
        img1 = image.load_img(str(imagep), target_size=(300, 300))
        x = image.img_to_array(img1)
        x = np.expand_dims(x, axis=0)

        images = np.vstack([x])
        classes = self.model.predict(images, batch_size=10)
        c = list(classes[0])
        flowers = ['sunflower','cape flower','bird of paradise','bishop of llandaff','frangipani','blanket flower','pink-yellow dahlia','pincushion flower','love in the mist','anthurium','artichoke','balloon flower','buttercup','common tulip','daffodil','daisy','marigold','rose','wild rose','toad lily']
        flowers.sort()
        result = flowers[c.index(1)]
        print(result)
        return result

mod= classification()
        
