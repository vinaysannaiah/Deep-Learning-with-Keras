# create a simple neural network
#defines a network that can seperate data from two blobs of data from different classes


#we shall use the inbuilt module make_blobs from sklearn

from sklearn.datasets import make_circles
import numpy as np 
import matplotlib.pyplot as plt

# lets avoid the warning msgs
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Helper functions

#To plot the data on a figure

def plot_data(pl, X, y):
    #plot class where y == 0
    pl.plot(X[y==0,0],X[y == 0,1], 'ob', alpha = 0.5)
    #plot class where y == 1
    pl.plot(X[y==1,0],X[y == 1,1], 'xr', alpha = 0.5)
    pl.legend(['0', '1'])
    return pl

#Function to draw the decision boundaries

def plot_decision_boundary(model, X, y):

    amin, bmin = X.min(axis=0) - 0.1
    amax, bmax = X.max(axis=0) + 0.1
    hticks = np.linspace(amin, amax, num= 101)
    vticks = np.linspace(bmin, bmax, num= 101)

    aa, bb = np.meshgrid(hticks, vticks)
    ab = np.c_[aa.ravel(), bb.ravel()]

    # make prediction with the model and reshape the output so contourf can plot it
    c = model.predict(ab)
    Z = c.reshape(aa.shape)

    plt.figure(figsize=(12,8))
    #plot the contour
    plt.contourf(aa, bb, Z, cmap = 'bwr', alpha= 0.2)
    # plot the moons of data
    plot_data(plt, X, y)

    return plt

# Generate some data blobs. Data will be either 0 or 1 when no. of centers is equal to 2
# X is a [number of samples,2] sized array. X[sample] contains its x,y position of the sample in the space
# ex: X[1] = [1.342, -2.3], X[2] = [-4,342, 2,12]
# y is a [number of samples ] sized array . y[sample] contains the class index (i.e. 0 or 1 when there are 2 centres)
# ex: y[0] = 0, y[1] = 1

X, y = make_circles(n_samples= 1000, factor= 0.6, noise=0.1, random_state = 42)

pl = plot_data(plt,X, y)
pl.show()


#split the data into training and test datasets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

#Create the keras model
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Simple sequential model
model = Sequential()
#   Add a Dense Fully Connected Layer with 1 neuron.  Using input_shape = (2,) says the input will 
#       be arrays of the form (*,2).  The first dimension will be an unspecified 
#       number of batches (rows) of data.  The second dimension is 2 which are the X, Y positions of each data element.
#       The sigmoid activation function is used to return 0 or 1, signifying the data 
#       cluster the position is predicted to belong to.
# 4 layer NN with relu activation function
model.add(Dense(3, input_shape=(2,), activation = 'tanh')) 
# 1 layer output network
model.add(Dense(1, activation="sigmoid"))

# We define the model's learning process by calling the compile method
#   Compile the model.  Minimize crossentopy for a binary.  Maximize for accuracy
model.compile(optimizer = Adam(lr=0.05), loss = 'binary_crossentropy', metrics = ['accuracy'])

#   Fit the model with the data from make_blobs.  Make 100 cycles through the data.
#       Set verbose to 0 to supress progress messages 
model.fit(X_train, y_train, epochs = 100, verbose = 1)

# Get loss and accuracy on test data
eval_result = model.evaluate(X_test, y_test)

#   Print test accuracy
print("\n\nTest loss:", eval_result[0], "Test accuracy:", eval_result[1])

#   Plot the decision boundary
plot_decision_boundary(model, X, y).show()


