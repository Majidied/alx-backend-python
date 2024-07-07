#!/usr/bin/env python3
"""Test client"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """test_org method"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @parameterized.expand(
        [
            ("google", "repos_url"),
            ("abc", "repos_url"),
        ]
    )
    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, org_name, expected, mock_org):
        """test_public_repos_url method"""
        mock_org.return_value = {expected: f"https://api.github.com/users/{org_name}"}
        test_class = GithubOrgClient(org_name)
        self.assertEqual(test_class._public_repos_url, f"https://api.github.com/users/{org_name}")
