from collective.base.interfaces import IViewlet
from zope.interface import Interface


# Browser layer

class ISantaThemeLayer(Interface):
    """Marker interface for browserlayer."""


# Viewlet

class IPloneSiteTwitterFeedViewlet(IViewlet):
    """Interface to display twitter feed for content type: Plone Site"""


class IPloneSiteEventFeedViewlet(IViewlet):
    """Interface to display event feed for content type: Plone Site"""

    def events():
        """Return list of dictionary

        :rtype: list
        """

    def year():
        """Return year

        :rtype: int
        """
