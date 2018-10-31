import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_initramfs_file(host):
    initramfs_file = host.file('/etc/initramfs-tools/initramfs.conf')

    assert initramfs_file.exists
    assert initramfs_file.user == 'root'
    assert initramfs_file.group == 'root'
    assert initramfs_file.contains('^BUSYBOX=y$')
    assert initramfs_file.contains(
            '^IP=172.16.100.12::172.16.100.1:255.255.255.0:test:eth0$')


def test_rsa_key_file(host):
    rsa_key_file = host.file('/etc/dropbear-initramfs/id_rsa')

    assert rsa_key_file.exists
    assert rsa_key_file.user == 'root'
    assert rsa_key_file.group == 'root'
    assert rsa_key_file.contains('-----BEGIN RSA PRIVATE KEY-----')
    assert rsa_key_file.contains('-----END RSA PRIVATE KEY-----')


def test_rsa_pub_key_file(host):
    rsa_pub_key_file = host.file('/etc/dropbear-initramfs/id_rsa.pub')

    assert rsa_pub_key_file.exists
    assert rsa_pub_key_file.user == 'root'
    assert rsa_pub_key_file.group == 'root'
    assert rsa_pub_key_file.contains('^ssh-rsa *')


def test_authorized_keys_file(host):
    authorized_keys_file = host.file('/etc/dropbear-initramfs/authorized_keys')

    assert authorized_keys_file.exists
    assert authorized_keys_file.user == 'root'
    assert authorized_keys_file.group == 'root'
    assert authorized_keys_file.contains('^ssh-rsa *')


def test_dropbear_defaults_file(host):
    dropbear_defaults_file = host.file('/etc/default/dropbear')

    assert dropbear_defaults_file.exists
    assert dropbear_defaults_file.user == 'root'
    assert dropbear_defaults_file.group == 'root'
    assert dropbear_defaults_file.contains('^NO_START=0*')


def test_crypt_unlock_file(host):
    crypt_unlock_file = host.file('/etc/initramfs-tools/hooks/crypt_unlock.sh')

    assert crypt_unlock_file.exists
    assert crypt_unlock_file.user == 'root'
    assert crypt_unlock_file.group == 'root'
    assert crypt_unlock_file.mode == 0o700
    assert crypt_unlock_file.contains('#!/bin/sh')


def test_dropbear_service(host):
    dropbear = host.service("dropbear")
    assert not dropbear.is_enabled


def test_grub_defaults_file(host):
    grub_defaults_file = host.file('/etc/default/grub')

    assert grub_defaults_file.exists
    assert grub_defaults_file.user == 'root'
    assert grub_defaults_file.group == 'root'
    assert grub_defaults_file.contains('^GRUB_CMDLINE_LINUX_DEFAULT="quiet"$')
