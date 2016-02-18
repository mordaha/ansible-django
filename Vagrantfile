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
     vb.memory = "394"
  end

  config.vm.network :forwarded_port, guest: 8000, host: 8000, host_ip: "127.0.0.1"
  config.vm.network :forwarded_port, guest: 3000, host: 3000, host_ip: "127.0.0.1"
  config.vm.network :forwarded_port, guest: 80,   host: 8080, host_ip: "127.0.0.1"
  config.vm.network :forwarded_port, guest: 5432, host: 5433, host_ip: "127.0.0.1"

  config.vm.define :devserver do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "devserver"
    node.vm.network :forwarded_port, guest: 22, host: 2200, id: 'ssh', host_ip: "127.0.0.1"
    node.vm.network :private_network, ip: "192.168.111.100"

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
      ansible.playbook = File.expand_path("./deployment/playbooks/site.yml")
      ansible.inventory_path = "./deployment/inventory/vagrant_dev"
      ansible.sudo = true
      ansible.limit = "all"
    end
  
  end
  
end
