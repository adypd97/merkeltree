class TreeEmptyError(Exception):
    def __init__(self, *args):
        if args:
            self.error = args[0]
        else:
            self.error = None
    def __str__(self):
        if self.error:
            return 'TreeEmptyError, {0}'.format(self.error)
        else:
            return 'TreeEmptyError was raised'
