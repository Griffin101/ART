import numpy as np

def sigmoid(x):
    return 1/( 1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self,input_size,hidden_size,output_size):
        self.weights_input_hidden = np.random.uniform(-1,1,(input_size,hidden_size))
        self.weights_hidden_output = np.random.uniform(-1,1,(hidden_size,output_size))

    def forward(self,input):
        self.hidden_input = np.dot(input, self.weights_input_hidden)
        self.hidden_output= sigmoid(self.hidden_input)
        self.output_input = np.dot(self.hidden_output,self.weights_hidden_output)
        self.predicted_output = sigmoid(self.output_input)
        return self.predicted_output

    def backward(self,input,target, learning_rate):
        error = target - self.predicted_output
        delta_output = error * sigmoid_derivative(self.predicted_output)
        error_hidden = delta_output.dot(self.weights_hidden_output.T)
        delta_hidden = error_hidden * sigmoid_derivative(self.hidden_output)

        self.weights_input_hidden += np.outer(input,delta_hidden)*learning_rate
        self.weights_hidden_output += np.outer(self.hidden_output,delta_output)* learning_rate

    def train(self,training_data, target_data, epochs, learning_rate):
        for epoch in range(epochs):
            for i in range(len(training_data)):
                input = training_data[i]
                target = target_data[i]
                self.forward(input)
                self.backward(input,target,learning_rate)

    def predict(self,input):
        return self.forward(input)
    
training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target_data = np.array([[0],[1],[1],[0]])

input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1
epoch = 10000

nn = NeuralNetwork(input_size,hidden_size,output_size)
nn.train(training_data,target_data,epoch,learning_rate)

for i in range(len(training_data)):
    input = training_data[i]
    prediction = nn.predict(input)
    print(f'Input: {input}, Predicted Output: {prediction}')