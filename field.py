
class CaseInsensitiveFieldMixin:
    """[summary]
    Mixin to make django fields case insensitive
    """

    def get_prep_value(self, value):

        return str(value).lower()

    def to_python(self, value):

        value = super().to_python(value)

        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):

            return value.lower()

        return value
