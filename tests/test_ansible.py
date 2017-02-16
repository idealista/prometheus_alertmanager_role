import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


def test_alertmanager_user(User, Group, AnsibleDefaults):
    assert User(AnsibleDefaults["alertmanager_user"]).exists
    assert Group(AnsibleDefaults["alertmanager_group"]).exists
    assert User(AnsibleDefaults["alertmanager_user"]).group == AnsibleDefaults["alertmanager_group"]


def test_alertmanager_conf(File, User, Group, AnsibleDefaults):
    conf_dir = File(AnsibleDefaults["alertmanager_conf_dir"])
    assert conf_dir.exists
    assert conf_dir.is_directory
    assert conf_dir.user == AnsibleDefaults["alertmanager_user"]
    assert conf_dir.group == AnsibleDefaults["alertmanager_group"]


def test_alertmanager_data(File, User, Group, AnsibleDefaults):
    conf_dir = File(AnsibleDefaults["alertmanager_data_dir"])
    assert conf_dir.exists
    assert conf_dir.is_directory
    assert conf_dir.user == AnsibleDefaults["alertmanager_user"]
    assert conf_dir.group == AnsibleDefaults["alertmanager_group"]


def test_alertmanager_log(File, User, Group, AnsibleDefaults):
    conf_dir = File(AnsibleDefaults["alertmanager_log_dir"])
    assert conf_dir.exists
    assert conf_dir.is_directory
    assert conf_dir.user == AnsibleDefaults["alertmanager_user"]
    assert conf_dir.group == AnsibleDefaults["alertmanager_group"]


def test_alertmanager_bin(File, Command, AnsibleDefaults):
    am = File(AnsibleDefaults["alertmanager_bin_dir"] + "/alertmanager")
    am_link = File("/usr/bin/alertmanager")
    assert am.exists
    assert am.is_file
    assert am.user == AnsibleDefaults["alertmanager_user"]
    assert am.group == AnsibleDefaults["alertmanager_group"]
    assert am_link.exists
    assert am_link.is_file
    assert am_link.user == "root"
    assert am_link.group == "root"
    am_version = Command("alertmanager -version")
    assert am_version.rc is 0
    assert "alertmanager, version " + AnsibleDefaults["alertmanager_version"] in am_version.stdout


def test_alertmanager_service(File, Service, Socket, AnsibleDefaults):
    assert File("/lib/systemd/system/alertmanager.service").exists
