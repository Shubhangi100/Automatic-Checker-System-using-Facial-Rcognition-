## Automatic-Checker-System-using-Facial-Rcognition-
It is an Attendance system based on deep learning
### Facial Detection 
Using the viola jones algorithm and the haar cascade features the faces are detection in a video feed
### Data Augmentation 
The model is trained on 200 subjects with intially 14 images per subject. Later on various Data Augmentation Techniques were used as:
### 1. Flipping
The images were flipped to get the mirror images which increased the data twice fold
### 2. Illumination
The system is made illumination invariant so as to make it work in various light conditions
### 3. Random Cropping
The image is cropped so as to contain majority of facial data as during detection only faces are detected which in turn falicitates the recognition 
### Facial Recognition
Recognition is done with multi-layer Convolutional Neural Networks trained from scratch. Giving 89% test accuracy and 92.19% validation accuracy. Alongside Overfitting was avoided with the above mentioned Data Augmentation Techniques.
