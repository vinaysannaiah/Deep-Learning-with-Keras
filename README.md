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

## prg2-1layerNN_circles.py

Let us do the same single layer Neural Network for more challenging data such as 2 different classes of data spread in the form of 2 contours.
Please refer the figure prg2_circles_data.png to get an insight into the data.
Here we can see that the accuracy reduces drastically to ~50%, as the data is not linearly spaced and its not easy for a single layer NN to classify the data. single layer NN can draw a straight line to divide the data.
Please refer the figure prg2_circles_result.png to see the result.

## prg3-MultilayerNN_circles.py

Here in this program we add a new layer having 3 neurons to our previous NN. Our first hidden layer has 3 Neurons and uses tanh activation function. The output layer of this NN has a single neuron and uses sigmoid activation function. Here we can observe that our accuracy rises to 92%. By this approach we can observe that adding an extra layer would increase the accuracy by a great extent.
You can examine the program by adding a new layer of neurons and playing around with different activation functions. But if we add more number layers we get into another problem called over fitting.
Please refer the figure prg3_circles_result.png and observe how well our NN classifies the data.
