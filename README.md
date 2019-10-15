# cifs-mounts

Installs samba mount utils and configures cifs mounts.

## Role Variables

| Variable name                      | Type              | Default                   | Description                                                                                                                                          |
| ---------------------------------- | ----------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| cifs_packages                      | list              | cifs-utils, smbclient     | The packages required for samba mounting and client activities                                                                                       |
| cifs_mounts                        | list[dict]        | []                        | A list of cifs mounts to configure                                                                                                                   |
| &nbsp;&nbsp;∟.path                 | file path         |                           | The mount point on the host machine                                                                                                                  |
| &nbsp;&nbsp;∟.cifs_path            | samba path        |                           | The samba share to mount                                                                                                                             |
| &nbsp;&nbsp;∟.opts                 | list[opt strings] |                           | The cifs mount options (see [mount.cifs](https://linux.die.net/man/8/mount.cifs)).*                                                                  |
| &nbsp;&nbsp;∟.dump                 | int               | option omitted if not set | See [ansible mount](https://docs.ansible.com/ansible/latest/modules/mount_module.html) for details.                                                  |
| &nbsp;&nbsp;∟.passno               | int               | option omitted if not set | See [ansible mount](https://docs.ansible.com/ansible/latest/modules/mount_module.html) for details.                                                  |
| &nbsp;&nbsp;∟.state                | string            | present                   | The mount state (see [ansible mount](https://docs.ansible.com/ansible/latest/modules/mount_module.html))                                             |
| &nbsp;&nbsp;∟.credentials          | dict              |                           | Special dictionary to define the credentials file. Allows files to be created by giving username/password or copied given src and destination path.* |
| &nbsp;&nbsp;∟.credentials.username     | string            |                           | User, if the credentials file should be created                                                                                                      |
| &nbsp;&nbsp;∟.credentials.password | string            |                           | Password, if the credentials file should be created                                                                                                  |
| &nbsp;&nbsp;∟.credentials.domain   | string            |                           | The samba domain, if the credentials file should be created (optional)                                                                               |
| &nbsp;&nbsp;∟.credentials.owner    | string            |                           | The file owner, if the credentials file should be created (optional)                                                                                 |
| &nbsp;&nbsp;∟.credentials.mode     | string            | 0600                      | The file permissions, if the credentials file should be created (optional)                                                                           |
| &nbsp;&nbsp;∟.credentials.path     | file path         |                           | The destination path, if the credentials file is to be copied or created on the ansible host. Also used for the credentials option.                  |
| &nbsp;&nbsp;∟.credentials.src      | file path         |                           | The source path, if the credentials file is to be copied to the ansible host                                                                         |
***Note that the `credentials` option can be set through the `.credentials` variable if the credentials file should be automatically created or copied to the host.**

## Examples

Immediately mount a single share as guest with rw permissions

```yaml
- hosts: "{{ test_host | default('localhost') }}"
  roles:
    - role: cifs-mounts
      vars:
        cifs_mounts:
          - path: /mnt/test
            cifs_path: //example/test
            opts:
            - guest
            - rw
            state: mounted
```

Add two mount entries in fstab, without immediately mounting, one using inline credentials and the other one with a credentials file created by the role.

```yaml
- hosts: "{{ test_host | default('localhost') }}"
  roles:
    - role: cifs-mounts
      vars:
        cifs_mounts:
          - path: /mnt/test
            cifs_path: //example/test
            opts:
            - username=test
            - password=test
            state: present
          - path: /mnt/test2
            cifs_path: //example/test2
            credentials:
              username: test2
              password: test2
              path: /home/test/cifs.credentials
            state: present
```
