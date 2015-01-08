from django.test import TestCase
from member.models import *

# Create your tests here.

class MemberTestCase(TestCase):

	def test_create_new_base_member(self):
		m1 = Member.objects.create(username="test", email="test@test.com")
		self.assertTrue(Member.objects.all().count() == 1)
		self.assertEqual(Member.objects.get(pk=m1.pk).memberType, "Base")

	def test_create_new_gold_member(self):
		m1 = Member.objects.create(username="test", email="test@test.com", memberType="Gold")
		self.assertTrue(Member.objects.all().count() == 1)
		self.assertEqual(Member.objects.get(pk=m1.pk).memberType, "Gold")

class CommitteeTestCase(TestCase):

	def test_create_new_committee(self):
		testName = "test committee"
		testEmail = "test@test.com"
		c1 = Committee.objects.create(name=testName, email=testEmail)
		self.assertTrue(Committee.objects.all().count() == 1)
		self.assertTrue(Committee.objects.filter(name=testName, email=testEmail).count() == 1)
		self.assertEqual(Committee.objects.get(pk=c1.pk), c1)
		self.assertTrue(c1.members.count() == 0)

	def test_create_new_committee_with_chair(self):
		m1 = Member.objects.create(username="test", email="test@test.com")
		c1 = Committee.objects.create(name="test committee", email="test@test.com", chair=m1)
		self.assertEqual(Committee.objects.get(pk=c1.pk), c1)
		self.assertTrue(c1.members.count() == 0)
		self.assertEqual(c1.chair, m1)

class CommitteeMembershipTestCase(TestCase):

	def setUp(self):
		Member.objects.create(username="test1", email="test@test.com")
		Member.objects.create(username="test2", email="test@test.com")
		Committee.objects.create(name="test committee", email="test@test.com")
		Committee.objects.create(name="test committee 2", email="test@test.com")

	def test_create_committee_membership(self):
		m1 = Member.objects.get(username="test1")
		c1 = Committee.objects.get(name="test committee")
		CommitteeMembership.objects.create(member=m1, committee=c1)
		self.assertTrue(m1.committees.count() == 1)
		self.assertEqual(m1.committees.first(), c1)
		self.assertTrue(c1.members.count() == 1)
		self.assertEqual(c1.members.first(), m1)

	def test_multiple_members_in_one_committee(self):
		m1 = Member.objects.get(username="test1")
		m2 = Member.objects.get(username="test2")
		c1 = Committee.objects.get(name="test committee")
		CommitteeMembership.objects.create(member=m1, committee=c1)
		CommitteeMembership.objects.create(member=m2, committee=c1)
		self.assertTrue(m1.committees.count() == 1)
		self.assertEqual(m1.committees.first(), c1)
		self.assertTrue(m2.committees.count() == 1)
		self.assertEqual(m2.committees.first(), c1)
		self.assertTrue(c1.members.count() == 2)
		self.assertIn(m1, c1.members.all())
		self.assertIn(m2, c1.members.all())

	def test_one_member_in_multiple_committees(self):
		m1 = Member.objects.get(username="test1")
		c1 = Committee.objects.get(name="test committee")
		c2 = Committee.objects.get(name="test committee 2")
		CommitteeMembership.objects.create(member=m1, committee=c1)
		CommitteeMembership.objects.create(member=m1, committee=c2)
		self.assertTrue(m1.committees.count() == 2)
		self.assertIn(c1, m1.committees.all())
		self.assertIn(c2, m1.committees.all())
		self.assertTrue(c1.members.count() == 1)
		self.assertEqual(c1.members.first(), m1)

class EventTestCase(TestCase):

	def test_create_simple_event(self):
		e1 = Event.objects.create(name="testEvent")
		self.assertTrue(Event.objects.all().count() == 1)

	def test_create_detailed_event(self):
		e1 = Event.objects.create(name="testEvent",loc="123 Happy Pl")
		self.assertTrue(Event.objects.all().count() == 1)
		self.assertEqual(Event.objects.get(name="testEvent",loc="123 Happy Pl"), e1)

class EventLoginTestCase(TestCase):

	def setUp(self):
		Event.objects.create(name="testEvent1")
		Event.objects.create(name="testEvent2",loc="123 Happy Pl")
		Member.objects.create(username="test1", email="test@test.com")
		Member.objects.create(username="test2", email="test@test.com")

	def test_create_event_login(self):
		m1 = Member.objects.get(username="test1")
		e1 = Event.objects.get(name="testEvent1")
		EventLogin.objects.create(event=e1, attendee=m1)
		self.assertTrue(m1.events.count() == 1)
		self.assertEqual(m1.events.first(), e1)
		self.assertTrue(e1.attendees.count() == 1)
		self.assertEqual(e1.attendees.first(), m1)

	def test_one_member_attends_multiple_events(self):
		m1 = Member.objects.get(username="test1")
		e1 = Event.objects.get(name="testEvent1")
		e2 = Event.objects.get(name="testEvent2")
		EventLogin.objects.create(event=e1, attendee=m1)
		EventLogin.objects.create(event=e2, attendee=m1)
		self.assertTrue(m1.events.count() == 2)
		self.assertIn(e1, m1.events.all())
		self.assertIn(e2, m1.events.all())
		self.assertTrue(e1.attendees.count() == 1)
		self.assertEqual(e1.attendees.first(), m1)
		self.assertTrue(e2.attendees.count() == 1)
		self.assertEqual(e2.attendees.first(), m1)

	def test_multiple_members_attend_one_event(self):
		m1 = Member.objects.get(username="test1")
		m2 = Member.objects.get(username="test2")
		e1 = Event.objects.get(name="testEvent1")
		EventLogin.objects.create(event=e1, attendee=m1)
		EventLogin.objects.create(event=e1, attendee=m2)
		self.assertTrue(m1.events.count() == 1)
		self.assertEqual(m1.events.first(), e1)
		self.assertTrue(m2.events.count() == 1)
		self.assertEqual(m2.events.first(), e1)
		self.assertTrue(e1.attendees.count() == 2)
		self.assertIn(m1, e1.attendees.all())
		self.assertIn(m2, e1.attendees.all())
