""" Top level package for print_me portfolio. """

__app__name__ = "print_me :sparkles: portfolio"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DATA_ERROR,
    JSON_ERROR,
) = range(5)

ERRORS = {
    DIR_ERROR: "Directory error.",
    FILE_ERROR: "File error.",
    DATA_ERROR: "Data error.",
    JSON_ERROR: "JSON error.",
}