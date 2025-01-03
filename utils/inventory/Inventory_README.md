# inventory_with_CSV
create inventory with csv file

1. The command to create an Ansible inventory file: ansible-playbook create_inventory_all.yml

	% ansible-playbook create_inventory_all.yml

	[WARNING]: No inventory was parsed, only implicit localhost is available

	[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

	PLAY [Create Ansible inventory from Cisco CSV file] ****************************************************************************

	TASK [Read data from CSV file] *************************************************************************************************
	ok: [localhost]

	TASK [Generate Ansible inventory file] *****************************************************************************************
	ok: [localhost]

	PLAY RECAP *********************************************************************************************************************
	localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

2. ansible_inventory.yml will be created

	ls -la ansible_inventory.yml
	-rw-r--r--  1 fwu  staff  2128 Jan 26 09:52 ansible_inventory.yml
