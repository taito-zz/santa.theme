# -*- coding: utf-8 -*-
from santa.theme.browser.interfaces import IPloneSiteEventFeedViewlet
from santa.theme.browser.viewlet import PloneSiteEventFeedViewlet
from santa.theme.tests.base import IntegrationTestCase


class PloneSiteEventFeedViewletTestCase(IntegrationTestCase):
    """TestCase for PloneSiteEventFeedViewlet"""

    def test_subclass(self):
        from collective.base.viewlet import Viewlet as Base
        self.assertTrue(issubclass(PloneSiteEventFeedViewlet, Base))
        from collective.base.interfaces import IViewlet as Base
        self.assertTrue(issubclass(IPloneSiteEventFeedViewlet, Base))

    def create_event(self, **kwargs):
        return self.create_atcontent('Event', **kwargs)

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        instance = self.create_viewlet(PloneSiteEventFeedViewlet)
        self.assertTrue(verifyObject(IPloneSiteEventFeedViewlet, instance))

    def test_events(self):
        instance = self.create_viewlet(PloneSiteEventFeedViewlet)
        self.assertEqual(len(instance.events()), 0)

        from DateTime import DateTime
        now = DateTime()
        self.create_event(id='event1', title='Ävent1', description='Descriptiön of Ävent1', startDate=now - 1, endDate=now + 1)
        self.assertEqual(len(instance.events()), 1)

        self.create_event(id='event2', title='Ävent2', description='Descriptiön of Ävent2', startDate=now - 2, endDate=now - 1)
        self.assertEqual(len(instance.events()), 1)

        self.create_event(id='event3', title='Ävent3', description='Descriptiön of Ävent3', startDate=now + 1, endDate=now + 2)
        self.assertEqual(len(instance.events()), 2)

        self.create_event(id='event4', title='Ävent4', description='Descriptiön of Ävent4', startDate=now + 365, endDate=now + 366)
        self.assertEqual(len(instance.events()), 2)

    def test_year(self):
        from datetime import date
        instance = self.create_viewlet(PloneSiteEventFeedViewlet)
        self.assertEqual(instance.year(), date.today().year)
