from django.test import TestCase
from member.models import *

# Create your tests here.

class MemberTestCase(TestCase):

	def test_create_new_base_member(self):
		m1 = Member.objects.create(username="test")
		self.assertEqual(m1.memberType, "Base")

	def test_create_new_gold_member(self):
		m1 = Member.objects.create(username="test", memberType="Gold")
		self.assertEqual(m1.memberType, "Gold")

class CommitteeTestCase(TestCase):

	def test_create_new_committee(self):
		c1 = Committee.objects.create(name="test committee", email="test@test.com")
		self.assertTrue(c1.members.count() == 0)

	def test_create_new_committee_with_chair(self):
		m1 = Member.objects.create(username="test")
		c1 = Committee.objects.create(name="test committee", email="test@test.com", chair=m1)
		self.assertTrue(c1.members.count() == 0)
		self.assertEqual(c1.chair, m1)
