"""
Relations
"""


class Relation:
    """
    A finitary relation on a finite set.

    Attributes:
        tuples (frozenset of tuple of int): The tuples belonging to the relation.
        universe_size (int): The number of elements in the universe, which is assumed to consist of an initial section
            of the nonnegative integers.
        arity (int): The length of each tuple in the relation. Can be inferred from `tuples` unless that iterable is
            empty.
    """

    def __init__(self, tuples, universe_size, arity=0):
        """

        Arguments:
            tuples (iterable of iterable of int): The tuples belonging to the relation.
            universe_size (int): The number of elements in the universe, which is assumed to consist of an initial
                section of the nonnegative integers.
            arity (int): The length of each tuple in the relation. Can be inferred from `tuples` unless that iterable is
                empty.
        """

        # Create a tuple of tuples of integers from the given iterable `tuples`.
        tuples = tuple(tuple(entry) for entry in tuples)
        # If `tuples` is empty then we have an empty relation and cannot infer its arity from its members.
        # If no value is provided for the arity, it defaults to 0.
        if len(tuples):
            # We assume that all entries in `tuples` have the same length. Take one of them to get the arity of the
            # relation.
            self._arity = len(tuples[0])
        else:
            self._arity = arity
        # Cast `tuples` to a frozenset and store it as the `tuples` attribute of the relation.
        self._tuples = frozenset(tuples)
        # Store the size of the universe.
        self._universe_size = universe_size

    @property
    def tuples(self):
        return self._tuples

    @property
    def universe_size(self):
        return self._universe_size

    @property
    def arity(self):
        return self._arity

    def __len__(self):
        """
        Give the number of tuples in the relation.

        Returns:
            int: The number of tuples in `self.tuples`.
        """

        return len(self.tuples)

    def __str__(self):
        """
        Display basic information about the relation.

        Returns:
            str: Information about the universe, arity, and size of the relation.
        """

        # When the universe size is large we use ellipsis rather than write out the whole universe.
        if self.universe_size > 10:
            universe = '{0,...,' + str(self.universe_size - 1) + '}'
        else:
            universe = '{' + ','.join(map(str, range(self.universe_size))) + '}'
        return 'A relation on {} of arity {} containing {} tuples'.format(universe, self.arity, len(self))

    def show(self):
        """
        Display the members of `self.tuples`.
        """

        for tup in self.tuples:
            print(tup)

    def comparison_check(self, other):
        """
        Determine whether another `Relation` object is of the correct type to be comparable with the relation in
        question.

        Returns:
            bool: True when the two relations have the same universe and arity, False otherwise.
        """

        return self.universe_size == other.universe_size and self.arity == other.arity

    def __hash__(self):
        """
        Find the hash value for the `Relation` object.

        Returns:
            int: The hash value of the `Relation` object.
        """

        return hash((self.tuples, self.universe_size, self.arity))

    def __eq__(self, other):
        """
        Check whether the relation is equal to another relation.

        Arguments:
            other (Relation): The other relation to which to compare this relation.

        Returns:
            bool: True when self.tuples is equal to other.tuples and False otherwise.
        """

        assert self.comparison_check(other)
        return self.tuples == other.tuples

    def __lt__(self, other):
        """
        Check whether the relation is properly contained in another relation.

        Args:
            other (Relation): The other relation to which to compare this relation.

        Returns:
            bool: True when self.tuples is a proper subset of other.tuples and False otherwise.
        """

        assert self.comparison_check(other)
        return self.tuples < other.tuples

    def __le__(self, other):
        """
        Check whether the relation is contained in another relation.

        Args:
            other (Relation): The other relation to which to compare this relation.

        Returns:
            bool: True when self.tuples is a subset of other.tuples and False otherwise.
        """

        assert self.comparison_check(other)
        return self.tuples <= other.tuples

    def __gt__(self, other):
        """
        Check whether the relation properly contains in another relation.

        Args:
            other (Relation): The other relation to which to compare this relation.

        Returns:
            bool: True when self.tuples is a proper superset of other.tuples and False otherwise.
        """

        assert self.comparison_check(other)
        return self.tuples > other.tuples

    def __ge__(self, other):
        """
        Check whether the relation contains in another relation.

        Args:
            other (Relation): The other relation to which to compare this relation.

        Returns:
            bool: True when self.tuples is a superset of other.tuples and False otherwise.
        """

        assert self.comparison_check(other)
        return self.tuples >= other.tuples