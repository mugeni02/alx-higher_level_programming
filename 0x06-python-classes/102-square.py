#!/usr/bin/python3
""" creates class Square """


class Square:
    def __init__(self, size=0):
        """Initialize the Square instance with a given size.

        Args:
            size (int or float): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The size to set.

        Raises:
            TypeError: If the size is not a number (int or float).
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Override the equality comparator."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Override the inequality comparator."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Override the greater-than comparator."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Override the greater-than-or-equal-to comparator."""
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """Override the less-than comparator."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Override the less-than-or-equal-to comparator."""
        return self.__lt__(other) or self.__eq__(other)
