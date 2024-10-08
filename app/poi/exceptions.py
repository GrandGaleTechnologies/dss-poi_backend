from app.common.exceptions import NotFound


class OffeseNotFound(NotFound):
    """
    Exception for 404 Offense Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("Offense Not Found", loc=loc)


class POINotFound(NotFound):
    """
    Exception for 404 POI Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("POI Not Found", loc=loc)


class POIOffenseNotFound(NotFound):
    """
    Exception for 404 POI Offense Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("POI Offense Not Found", loc=loc)


class IDDocumentNotFound(NotFound):
    """
    Exception for 404 ID Document Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("ID Document Not Found", loc=loc)


class GSMNumberNotFound(NotFound):
    """
    Exception for 404 GSM Number Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("GSM Number Not Found", loc=loc)


class ResidentialAddressNotFound(NotFound):
    """
    Exception for 404 Residential Address Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("Residential Address Not Found", loc=loc)


class KnownAssociateNotFound(NotFound):
    """
    Exception for 404 Known Associate Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("Known Associate Not Found", loc=loc)


class EmploymentHistoryNotFound(NotFound):
    """
    Exception for 404 Employment History Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("Employment History Not Found", loc=loc)


class EducationalBackgroundNotFound(NotFound):
    """
    Exception for 404 Educational Background Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("Educational Background Not Found", loc=loc)


class FrequentedSpotNotFound(NotFound):
    """
    Exception for 404 Frequented Spot Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("Frequented Spot Not Found", loc=loc)
