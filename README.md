Ansible for Django (django+gunicorn+nginx+postgresql+redis)
===========


Includes:
 * postgresql database (optional with postgis)
 * nginx server with ssl (optional with secure_link)
 * redis for cache/sessions
 * vagrant dev server


Django project structure:
```
project/
  deployment/ansible-django <-- this repo submodule or symlink
  deployment/inventory <-- your inventory (copy ansible-django/inventory-saple for vagrant dev-server)
  deployment/Vagrantfile -> symlink to -> ansible-django/Vagrantfile
  public/ <-- media/static
  src/ <-- django project
```

Django must use settings variables from environment (use https://github.com/jpadilla/django-dotenv for development)
Sample settings layout in ```src/``` of this repo

Then run:

```
$ cd deployment
$ vagrant up
```

New vagrant dev-server should be installed

To redeploy, run

```
$ ansible-playbook -i inventory/vagrant_dev ansible-django/playbooks/site.yml
```

Make your own ```inventory/your_production_inventory_file``` and deploy to production

Put sensible information (ssl-keys) into ```deployment/inventory/(all|whatever)/private.yml```

# LICENSE

MIT
