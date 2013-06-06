from DateTime import DateTime
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.base.interfaces import IAdapter
from collective.base.viewlet import Viewlet
from datetime import date
from plone.memoize.view import memoize_contextless
from santa.theme.browser.interfaces import IPloneSiteEventFeedViewlet
from zope.interface import implements


class PloneSiteEventFeedViewlet(Viewlet):
    """Event feed viewlet for plone site"""
    implements(IPloneSiteEventFeedViewlet)
    index = ViewPageTemplateFile('viewlets/event-feed.pt')

    def events(self):
        """Return list of dictionary

        :rtype: list
        """
        res = []
        base = IAdapter(self.context)
        before_date = '{}/01/01'.format(self.year() + 1)
        for item in base.get_content_listing(IATEvent, sort_on='start', start={'query': [DateTime(before_date), ], 'range': 'max'}, end={'query': [DateTime(), ], 'range': 'min'}):
            res.append({
                'datetime': base.event_datetime(item),
                'description': item.Description(),
                'title': item.Title(),
                'url': item.getURL(),
            })
        return res

    @memoize_contextless
    def year(self):
        """Return year

        :rtype: int
        """
        return date.today().year
