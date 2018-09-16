
def loader(module):
    m = __import__(module)
    return m.__exports__


