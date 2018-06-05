# Deep-Learning-with-Keras

This repository has some basic to intermediate level of using Deep Learning with Keras framework to solve the problems of classification and regression of data.

## prg1_one_layer_Neural_net.py

Here we shall classify the data from two different classes using a single layer Neural Network.
Initially we create the data using sklearn inbuilt method make_blobs.
This data is linearly spaced due to which a single layer NN works exceptionally well on this data in classifying it into two classes.
we create the data and split it into 70:30 train:test respectively
we train our model using the train data and test it using the test data.

we can visualize the data and the result in the prg1_data.png and prg1_result.png
The model gives us an accuracy of perfect 100% as the lone reason being the data can be clearly differentiated as it is linearly spaced.
