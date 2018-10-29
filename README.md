# ait.phusion.samba-mount

Installs samba utils and adds phusion startup script to mount shares configured in a envrionment variable.
## Requirements

Requires the init process provided by the [phusion/baseimage](https://hub.docker.com/r/phusion/baseimage/).

## Role Variables

Variables available as per cyberrange base client docker image:
- `default_user`: ubuntu  
   The default user made available by the baseimage
- `user`: ubuntu  
   The user to be used
- `img_home`: "/opt/unity-vnc"  
   Directory containing script and config file specific to the cyberrange base image
- `img_templates`: "/opt/unity-vnc/templates"  
   Directory that should be used to store templates, which are rendered on startup

## Environment Variables

- `SMB_SHARE_JSON`
    A list of dictionaries containing samba configurations. The following keys must be present:
    - `share`
        Remote samba share which should be mounted.
    - `local`
        The local directory the share should be mounted to.
    - `options`
        Options with which to run the mount.cifs command. Using this you can configure cerdentials etc.  

    Example:
    ```json
    [{
          "share": "//example.com/share",
          "local": "/mnt/share",
          "options": "user=example,password=example,uid=example,gid=example"
    }]
    ```
