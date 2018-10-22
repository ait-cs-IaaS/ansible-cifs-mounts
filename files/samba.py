#!/usr/bin/env python
import os, json, subprocess, time
import os.path

smb_json = os.environ.get('SMB_SHARE_JSON', None)
if smb_json != None and smb_json != "":
  time.sleep(20)
  smb_conf = json.loads(smb_json)
  if smb_conf != None:
    for conf in smb_conf:
      share = conf.get('share')
      options = conf.get('options')
      local = conf.get('local')
      print("Attempting to mount share: %s with %s on directory %s" % (share,options,local))
      if not os.path.exists(local):
        os.makedirs(local)
      print(subprocess.check_output(['mount.cifs',share, local, '-o', options]))
      print("Done!")
