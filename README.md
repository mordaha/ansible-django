Ansible scripts to deploy django project
===========

Django project structure:

```
./
  deployment/ <-- this repo submodule
  public/ <-- django collectstatic destination
  src/ <-- django project
  Vagrantfile <--- copied (or ln -s) vagrantfile from this repo
```
Django must use settings variables from environment (use https://github.com/jpadilla/django-dotenv for development)
Sample settings layout in ```src/``` of this repo

Then run:

```
$ vagrant up
```

New vagrant dev-server should be installed

To redeploy, run

```
$ ansible-playbook -i deployment/inventory/vagrant_dev deployment/playbooks/site.yml
```

Write your own ```deployment/inventory/your_production_inventory_file``` and deploy to production 


Put sensible information (ssl-keys) into ```deployment/inventory/all/private.yml```

Run to deploy:

```
$ ansible-playbook -i deployment/inventory/your_production_inventory_file deployment/playbooks/site.yml
```


# LICENSE

MIT

