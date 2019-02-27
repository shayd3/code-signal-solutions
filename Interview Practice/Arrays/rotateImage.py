def rotateImage(a):
    #reversed() reverses elements in an array
    #zip()  take iterables, makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.
    return list(zip(*reversed(a)))