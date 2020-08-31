# Dropbear LUKS

Ansible role to setup a **dropbear** SSH server in a **busybox** in the
**initramfs** so you can be able to connect remotely and enter the **LUKS**
password of your fully (except for */boot*) encrypted server. If you specify
a `static_ip`, it will be set up, otherwise the default DHCP option will be
used.

Based on
[pbworks](https://www.pbworks.net/ubuntu-guide-dropbear-ssh-server-to-unlock-luks-encrypted-pc/)
and
[eugenemdavis](https://www.eugenemdavis.com/set-static-ip-initramfs.html).

**Note**: It only supports RSA SSH keys for now.

Uses the *crypt_unlock.sh* from
[gusennan](https://gist.github.com/gusennan/712d6e81f5cf9489bd9f)

## Compatibility

This role should work in any distro from the **Debian** family. It is tested
on debian buster.

## Requirements

You'll need an already configured **Debian** family server with an unencrypted
boot partition and the rest under LUKS encryption that you are able to unlock
by physically entering the LUKS password to the server.

## Role Variables

* `ssh_pub_key`: Local path to your public SSH key
* `static_ip`: Static IP for the **initramfs**. If you leave it undefined,
DHCP will be used. But if it's defined, the following variables must be
defined too.
* `remote_ip`: Allowed remote IP address to recieve connections from. Empty by
default (incoming connections aren't restricted to an specific IP address).
* `gateway`: Gateway IP address.
* `netmask`: Netmask.
* `hostname`: Hostname.
* `network_interface`: Main network interface to setup the static IP on.
* `ssh_port`: If defined, the **dropbear** SSH port will be set to its value.

## Dependencies

None.

## Example Playbook

```yaml
- name: Setup dropbear SSH server in the initramfs
  hosts: all
  roles:
    - role: dropbear_luks
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/)
. You also need to have a valid SSH public key in *~/.ssh/id_rsa.pub*. If you
don't have one, you can create it with: `ssh-keygen -C test -f ~/.ssh/id_rsa`.

```bash
molecule test
```

## License

GPLv3

## Author Information

 * m0wer: m0wer (at) autistici (dot) org
