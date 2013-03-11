from DateTime import DateTime
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from collective.base.interfaces import IAdapter
from abita.basetheme.browser.viewlet import PloneSiteViewletManager
from five import grok
from plone.memoize.view import memoize_contextless
from santa.theme.browser.interfaces import ISantaThemeLayer
from datetime import date


grok.templatedir('viewlets')


class BaseViewlet(grok.Viewlet):
    """Base viewlet"""
    grok.baseclass()
    grok.layer(ISantaThemeLayer)
    grok.require('zope2.View')


class PloneSiteEventFeedViewlet(BaseViewlet):
    """Event feed viewlet for plone site"""
    grok.context(IPloneSiteRoot)
    grok.name('santa.theme.plonesite.eventfeed')
    grok.template('event-feed')
    grok.viewletmanager(PloneSiteViewletManager)

    @property
    def events(self):
        res = []
        base = IAdapter(self.context)
        before_date = '{}/01/01'.format(self.year + 1)
        for item in base.get_content_listing(IATEvent, sort_on='start', start={'query': [DateTime(before_date), ], 'range': 'max'}, end={'query': [DateTime(), ], 'range': 'min'}):
            res.append({
                'datetime': base.event_datetime(item),
                'description': item.Description(),
                'title': item.Title(),
                'url': item.getURL(),
            })
        return res

    @property
    @memoize_contextless
    def year(self):
        return date.today().year
