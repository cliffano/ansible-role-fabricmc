<img align="right" src="https://raw.github.com/cliffano/ansible-role-fabricmc/main/avatar.jpg" alt="Avatar"/>

[![Build Status](https://github.com/cliffano/ansible-role-fabricmc/workflows/CI/badge.svg)](https://github.com/cliffano/ansible-role-fabricmc/actions?query=workflow%3ACI)
[![Security Status](https://snyk.io/test/github/cliffano/ansible-role-fabricmc/badge.svg)](https://snyk.io/test/github/cliffano/ansible-role-fabricmc)
<br/>

Ansible Role Fabric Minecraft Mod Loader
----------------------------------------

Ansible Role Fabric Minecraft Mod Loader is a Ansible role for provisioning Fabric mod loader for Minecraft .

Usage
-----

Use the role in your playbook:

    - hosts: all

      vars:
        ans_reverse: true
        ans_transformation: 'upper'

      roles:
        - cliffano.fabricmc