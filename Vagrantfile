Vagrant.configure("2") do |config|

  # PiGUI dev box
  config.vm.define :pi do | pi |
    config.vm.provider "virtualbox" do | vb |
      vb.memory = 1024
      vb.name = "Raspberry PI"
      vb.gui = true
      vb.customize [ "modifyvm", :id, "--audio", "pulse", "--audiocontroller", "ac97", "--audiocodec", "stac9700" ]
    end
    pi.vm.host_name = "pi.localdomain"
    pi.vm.box = "debian/wheezy64"
    pi.vm.provision :shell, :path => 'bin/pi.sh'
  end
end
