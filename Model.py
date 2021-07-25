import random
import fasttext
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model



class Classifier:
    def __init__(self):
        self.model_loaded = None
        self.loadModel()

    def loadModel(self):
        self.model_use = fasttext.load_model('C:/Users/USER/PycharmProjects/pythonProject/model_use.bin')
        self.model_loaded = tf.keras.models.load_model('C:/Users/USER/PycharmProjects/pythonProject/CNN')

        self.model_xcep = tf.keras.applications.xception.Xception(weights='imagenet', include_top=True)
        self.model_xcep = Model(inputs=self.model_xcep.inputs, outputs=self.model_xcep.layers[-2].output)

    def inference(self, image=None, text=''):

        emb = [self.model_use.get_word_vector(x) for x in text.split(' ')]
        avg_emb = np.mean(emb, axis=0)

        if image is None:
            feature = [0] * 2048
            final_feature = np.concatenate((feature, avg_emb))
        else:
            img = tf.keras.preprocessing.image.load_img(image, target_size=(299, 299))
            img = tf.keras.preprocessing.image.img_to_array(img)
            img = img[np.newaxis, ...]
            feature = self.model_xcep.predict(img)
            final_feature = np.concatenate((feature[0], avg_emb))
        # label_sample = 0
        # if row[1][2]=="Genuine":
        #     label_sample=1
        # final_feature = np.concatenate((final_feature,[label_sample]))
        feature = np.array([final_feature])
        # label = final_feature[-1]
        # print(feature)
        # print(feature.shape)
        res = self.model_loaded.predict_classes([feature])
        # print(res)
        return res