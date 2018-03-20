#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2018, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}

DOCUMENTATION = """
---
module: get
short_description: Run command on remote host
description:
  - This module will connect to the remote network device and run commands
version_added: "2.6"
options:
  command:
    description:
      - The command to send to the device over.
    required: True
author:
  - Ansible Network Team
"""

EXAMPLES = """
- name: return the current device config
  get:
    command: show version
"""

RETURN = """
text:
  description: The device command output
  returned: always
  type: str
  sample: "hostname localhost\nip domain-name ansible.com"
"""
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection


def main():
    """main entry point for module execution
    """
    argument_spec = dict(
        command=dict(required=True),
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    command = module.params['command']

    connection = Connection(module._socket_path)
    output = connection.get(command=command)

    result = {
        'changed': False,
        'text': output
    }

    module.exit_json(**result)


if __name__ == '__main__':
    main()