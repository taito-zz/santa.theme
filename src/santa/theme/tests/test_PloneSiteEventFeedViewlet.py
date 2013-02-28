# -*- coding: utf-8 -*-
from santa.theme.tests.base import IntegrationTestCase
from zope.publisher.browser import TestRequest
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


class PloneSiteEventFeedViewletTestCase(IntegrationTestCase):
    """TestCase for PloneSiteEventFeedViewlet"""

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_subclass(self):
        from santa.theme.browser.viewlet import BaseViewlet
        from santa.theme.browser.viewlet import PloneSiteEventFeedViewlet
        self.assertTrue(issubclass(PloneSiteEventFeedViewlet, BaseViewlet))

    def test_context(self):
        from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
        from santa.theme.browser.viewlet import PloneSiteEventFeedViewlet
        self.assertEqual(getattr(PloneSiteEventFeedViewlet, 'grokcore.component.directive.context'), IPloneSiteRoot)

    def test_template(self):
        from santa.theme.browser.viewlet import PloneSiteEventFeedViewlet
        self.assertEqual(getattr(PloneSiteEventFeedViewlet, 'grokcore.view.directive.template'), 'event-feed')

    def test_name(self):
        from santa.theme.browser.viewlet import PloneSiteEventFeedViewlet
        from santa.theme.browser.viewlet import PloneSiteViewletManager
        self.assertEqual(getattr(PloneSiteEventFeedViewlet, 'grokcore.viewlet.directive.viewletmanager'),
            PloneSiteViewletManager)

    def create_event(self, **kwargs):
        event = self.portal[self.portal.invokeFactory('Event', **kwargs)]
        event.reindexObject()
        return event

    def create_instance(self):
        from santa.theme.browser.viewlet import PloneSiteEventFeedViewlet
        from zope.annotation.interfaces import IAttributeAnnotatable
        from zope.interface import directlyProvides
        request = TestRequest()
        directlyProvides(request, IAttributeAnnotatable)
        return PloneSiteEventFeedViewlet(self.portal, request, manager=None, view=None)

    def test_events(self):
        instance = self.create_instance()
        self.assertEqual(len(instance.events), 0)

        from DateTime import DateTime
        now = DateTime()
        self.create_event(id='event1', title='Ävent1', description='Descriptiön of Ävent1', startDate=now - 1, endDate=now + 1)
        self.assertEqual(len(instance.events), 1)

        self.create_event(id='event2', title='Ävent2', description='Descriptiön of Ävent2', startDate=now - 2, endDate=now - 1)
        self.assertEqual(len(instance.events), 1)

        self.create_event(id='event3', title='Ävent3', description='Descriptiön of Ävent3', startDate=now + 1, endDate=now + 2)
        self.assertEqual(len(instance.events), 2)

        self.create_event(id='event4', title='Ävent4', description='Descriptiön of Ävent4', startDate=now + 365, endDate=now + 366)
        self.assertEqual(len(instance.events), 2)

    def test_year(self):
        from datetime import date
        instance = self.create_instance()
        self.assertEqual(instance.year, date.today().year)
