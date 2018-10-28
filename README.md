# Dropbear LUKS

Ansible role to setup a **dropbear** SSH server in a **busybox** in the
**initramfs** so you can be able to connect remotely and enter the **LUKS**
password of your fully (except for */boot*) encrypted server.

Based on
[pbworks](https://www.pbworks.net/ubuntu-guide-dropbear-ssh-server-to-unlock-luks-encrypted-pc/)
and
[eugenemdavis](https://www.eugenemdavis.com/set-static-ip-initramfs.html).

## Requirements

You'll need an already configured **Debian** family server with an unencrypted
boot partition and the rest under LUKS encryption that you are able to unlock
by physically entering the LUKS password to the server.

## Role Variables

## Dependencies

None.

## Example Playbook

```yaml
- name: Setup dropbear SSH server in the initramfs
  hosts: all
  vars:
  roles:
    - role: dropbear_luks
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/)
.

```bash
molecule test
```

## License

GPLv3

## Author Information

m0wer [ at ] autistici.org
