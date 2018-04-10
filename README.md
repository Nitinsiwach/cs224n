# cs224n
Stanford cs224n assignments complete

Assignment 1:
 
q1_softmax.py - softmax numpy implementation and numerical gradient tests

q2_sigmoid.py - sigmoid activation and its gradient.

q2_gradcheck.py -  Numerical gradient tests

q2_neural.py - Numpy implementation of forward and backward pass for a neural network with a hidden sigmoid layer.\
Sanity checks for the same are available as well

q3_word2vec.py and q3_sgd.py - CBOW and skipgram implemented in numpy. training protocol using SGD update rule for the same
is implemented in q3_sgd.py

q3_run.py - Runs q3_sgd.py on Stanford sentiment treebank data

q4_sentiment.py - Sentiment analysis on Stanford sentiment treebank using bag of words feature representation of query

Assignment 2:

q1_softmax.py - Tensorflow implemented softmax and its gradient. Numerical gradient checks included

model.py - Tensorflow. Every model inherits from this class. 

q1_classifier.py - A single layered softmax classifier in Tensorflow. Creates synthetic data and fits the network to this data

q2_parser_transitions.py - A transition-based dependency parser transitions with features extracted as explained in 
https://cs.stanford.edu/~danqi/papers/emnlp2014.pdf (parser_utils.py contains this feature extractor)

q2 initialization.py - Xavier initialization implemented as explained in http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf
and its implementation tests

q2_parser_model.py - Neural network classiﬁer governing the dependency parser.trained and evaluated model on the 
Penn Treebank (annotated with Universal Dependencies). Update rule - ADAM

Assignment 3:

q1_window.py - A window based NER (Named entity recognition) classifier and unit tests implemented in Tensorflow evaluated 
on entity level F1 score

q2_rnn_cell.py - Tensorflow implementation of an RNN cell (convenience inbuilt tensorflow functions are not used here)

q3_gru_cell.py -  Tensorflow implementation of a GRU cell (convenience inbuilt tensorflow functions are not used here)

q3_gru.py - A dynamic RNN implemented in Tensorflow using the Recurrent cell as implemented in q3_gru_cell.py to learn the latching
behavior. data is synthetically generated here

q2_rnn.py - Tensorflow implemented vanilla RNN model. Convenience functions wont be used here. 
Used for training a classifier on NER. Takes in as input the cell to be used for recurrence (as implemented in q2_rnn_cell.py or q3_gru_cell.py)









            
     

