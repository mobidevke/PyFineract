class FineractException(Exception):
    """
    Error handling in PyFineract is done with exceptions. This class is the base of all exceptions raised by PyFineract
    (but :class:`fineract.exceptions.BadAttributeException`).
    Some other types of exceptions might be raised by underlying libraries, for example for network-related issues.
    """

    def __init__(self, status, data):
        Exception.__init__(self)
        self.__status = status
        self.__data = data
        self.args = [status, data]

    @property
    def status(self):
        """
        The status returned by the Fineract API
        """
        return self.__status

    @property
    def data(self):
        """
        The (decoded) data returned by the Fineract API
        """
        return self.__data

    def __str__(self):
        return str(self.status) + " " + str(self.data)


class BadCredentialsException(FineractException):
    """
    Exception raised in case of bad credentials (when Fineract API replies with a 401 or 403 HTML status)
    """


class ResourceNotFoundException(FineractException):
    """
    Exception raised when a non-existing object is requested (when Fineract API replies with a 404 HTML status)
    """


class BadArgsException(FineractException):
    """
    Exception raised when a non-existing object is requested (when Fineract API replies with a 400 HTML status)
    """
