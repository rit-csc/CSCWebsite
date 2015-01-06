from django.test import TestCase
from member.models import *

# Create your tests here.

class MemberTestCase(TestCase):

	def test_create_new_base_member(self):
		m1 = Member.objects.create(username="test")
		self.assertTrue(Member.objects.all().count() == 1)
		self.assertEqual(Member.objects.get(pk=m1.pk).memberType, "Base")

	def test_create_new_gold_member(self):
		m1 = Member.objects.create(username="test", memberType="Gold")
		self.assertTrue(Member.objects.all().count() == 1)
		self.assertEqual(Member.objects.get(pk=m1.pk).memberType, "Gold")

class CommitteeTestCase(TestCase):

	def test_create_new_committee(self):
		testName = "test committee"
		testEmail = "test@test.com"
		c1 = Committee.objects.create(name=testName, email=testEmail)
		self.assertTrue(Committee.objects.all().count() == 1)
		self.assertEqual(Committee.objects.filter(name=testName, email=testEmail).count(), 1)
		self.assertEqual(Committee.objects.get(pk=c1.pk), c1)
		self.assertTrue(c1.members.count() == 0)

	def test_create_new_committee_with_chair(self):
		m1 = Member.objects.create(username="test")
		c1 = Committee.objects.create(name="test committee", email="test@test.com", chair=m1)
		self.assertTrue(c1.members.count() == 0)
		self.assertEqual(c1.chair, m1)

class CommitteeMembershipTestCase(TestCase):

	def setUp(self):
		Member.objects.create(username="test")
		Committee.objects.create(name="test committee", email="test@test.com")

	def test_create_committee_membership(self):
		m1 = Member.objects.get(username="test")
		c1 = Committee.objects.get(name="test committee")
		CommitteeMembership.objects.create(member=m1, committee=c1)
		self.assertTrue(m1.committees.count() == 1)
		self.assertEqual(m1.committees.first(), c1)
		self.assertTrue(c1.members.count() == 1)
		self.assertEqual(c1.members.first(), m1)
