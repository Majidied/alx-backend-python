#!/usr/bin/env python3
"""Test client"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from unittest.mock import MagicMock, patch, Mock, PropertyMock


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
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @parameterized.expand(
        [
            ("google", "repos_url"),
            ("abc", "repos_url"),
        ]
    )
    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, org_name, expected, mock_org):
        """test_public_repos_url method"""
        mock_org.return_value = {
            expected: f"https://api.github.com/users/{org_name}"}
        test_class = GithubOrgClient(org_name)
        self.assertEqual(
            test_class._public_repos_url,
            f"https://api.github.com/users/{org_name}"
        )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
            "repos_url": "https://api.github.com/users/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ],
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """Tests the `has_license` method."""
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.get_patcher = patch("client.get_json")
        cls.mock_get_json = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests the `public_repos` method."""
        test_payload = {
            "repos_url": "https://api.github.com/users/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ],
        }
        self.mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        self.mock_get_json.assert_called_once()
