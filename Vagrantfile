# -*- mode: ruby -*-
# vi: set ft=ruby :
#
#
# This file should be placed into parent directory of this
#
#


Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "894"
  end


  config.vm.define :devserver do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "devserver"
    config.vm.synced_folder "..", "/vagrant"

    node.vm.network :forwarded_port, guest: 22, host: 2200, id: 'ssh', host_ip: "127.0.0.1"
    node.vm.network :private_network, ip: "192.168.111.100"

      # web
      config.vm.network :forwarded_port, guest: 8000, host: 8000, host_ip: "127.0.0.1"
      config.vm.network :forwarded_port, guest:   80, host: 8080, host_ip: "127.0.0.1"
      config.vm.network :forwarded_port, guest:  443, host: 8443, host_ip: "127.0.0.1"
      # postgresql
      config.vm.network :forwarded_port, guest: 5432, host: 5432, host_ip: "127.0.0.1"

    # user's ~/.ssh pub key
    node.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
        echo #{ssh_pub_key} >> /root/.ssh/authorized_keys
      SHELL
    end
  
    # ansible playbook provision
    node.vm.provision :ansible do |ansible|
      ansible.playbook = File.expand_path("./ansible-django/playbooks/site.yml")
      ansible.inventory_path = "./inventory/vagrant_dev"
      ansible.sudo = true
      ansible.limit = "all"
    end
  
  end
  
end
