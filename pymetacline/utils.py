import glob


def get_example_file(extension=None):
    """
    Get the path to the example datasets available in pymetacline.

    :param ext: Extension. Filter dataset by extensions. 

    :Example:

    >>> from pymetacline.utils import get_example_file
    >>> a = get_example_file()
    >>> assert a[0].endswith('gtf')
    >>> a= get_example_file(ext="bam")
    >>> assert a[0].endswith('bam')
    >>> a= get_example_file(ext="bw")
    >>> assert a[0].endswith('bw')

    """

    file_path = glob.glob(os.path.join(os.path.dirname(pygtftk.__file__),
                                       'data',
                                       datasetname,
                                       "*" + ext))

    return file_path
