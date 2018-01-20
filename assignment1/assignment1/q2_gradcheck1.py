#!/usr/bin/env python

import numpy as np
import random


# First implement a gradient checker by filling in the following functions
def gradcheck_naive(f, x):
    """ Gradient check for a function f.

    Arguments:
    f -- a function that takes a single argument and outputs the
         cost and its gradients
    x -- the point (numpy array) to check the gradient at
    """
    rndstate = random.getstate()
    random.setstate(rndstate)
    fx, grad = f(x) # Evaluate function value at original point
    #grad = np.reshape(grad, newshape=  [1,10])
    #print fx, 'equals cost'
    h = 1e-4        # Do not change this!
    # Iterate over all indexes in x
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        ix = it.multi_index
        print it.multi_index
        # Try modifying x[ix] with h defined above to compute
        # numerical gradients. Make sure you call random.setstate(rndstate)
        # before calling f(x) each time. This will make it possible
        # to test cost functions with built in randomness later.
        
        delta = np.zeros(x.shape)
        
        delta[ix] = h
        #print delta, (x + delta)[55], x[55], ' this is to be tested', f(x + delta)[0], f(x)[0]
        random.setstate(rndstate)
        numgrad = (f(x + delta)[0] - fx)/h
        print numgrad, grad[ix], 'these are two gradients getting compared'
        

        # Compare gradients
        reldiff = abs(numgrad - grad[ix]) / max(1, abs(numgrad), abs(grad[ix]))
        if reldiff > 1e-3:
            print "Gradient check failed."
            print "First gradient error found at index %s" % str(ix)
            print "Your gradient: %f \t Numerical gradient: %f" % (
                grad[ix], numgrad)
            return

        it.iternext() # Step to next dimension

    print "Gradient check passed!"


def sanity_check():
    """
    Some basic sanity checks.
    """
    quad = lambda x: sigmoid(x), sigmoid(x)(1-sigmoid(x))
    print("Running sanity checks...")
    gradcheck_naive(quad, datao_h)      # scalar test
    #gradcheck_naive(quad, np.random.randn(3,))    # 1-D test
    #gradcheck_naive(quad, np.random.randn(4,5))   # 2-D test
    print ""


def your_sanity_checks():
    """
    Use this space add any additional sanity checks by running:
        python q2_gradcheck.py
    This function will not be called by the autograder, nor will
    your additional tests be graded.
    """
    print "Running your sanity checks..."
    ### YOUR CODE HERE
    ###raise NotImplementedError
    ### END YOUR CODE


if __name__ == "__main__":
    sanity_check()
    your_sanity_checks()