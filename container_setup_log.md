Commands to get a container up and running (with Docker installed, of course):
# Notice: If you are running this app from Docker, skip down to 'Setup from Docker'

# Getting started
## Starting the container
(From docker-machine)
* `docker pull ubuntu:14.04` # Get Ubuntu 14.04
* `docker run -ti ubuntu:14.04 bash` # Start a new container from the ubuntu:14.04 image
* `sudo apt-get install vim` OR `sudo apt-get install nano` # Getting a text editor
* `sudo apt-get install curl`

## Setting up Ubuntu
(now we're inside the container we just made)
* `sudo apt-get update` # Update the apt cache
* `sudo apt-get install git` # Install git
* `git --version` # To see if git installed correctly

## Setting up Ruby and RVM
following [this tutorial using RVM](http://railsapps.github.io/installrubyonrails-ubuntu.html)
(This command will probably throw an error, but it will recommend a fix)
* `\curl -L https://get.rvm.io | bash -s stable --ruby` # Installing RVM
* `source /usr/local/rvm/scripts/rvm`
* `gem update --system`
* `rvm gemset use global`
* `gem update`
(optional. This will not download the documentation for ruby gems. Should speed up downloads)
* `echo "gem: --no-document" >> ~/.gemrc`

### Installing NodeJS
* `sudo apt-get install nodejs`
(and set nodejs to path)

### Install Bundler
* `gem install bundler`
* `bundle --version`

### Install Nokogiri
* `gem install nokogiri`

## Finishing Ruby and Setting up Rails
* `rvm install ruby-2.3.1` # Install Ruby-2.3.1
* `rvm use ruby-2.3.1@rails5.0 --create`
* `gem install rails` # Installing rails
* `rails -v` # See if rails installed correctly

## Installing MongoDB for Engine
[following this guide](https://docs.mongodb.com/v3.2/tutorial/install-mongodb-on-ubuntu/)
* `sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927` # Import public key ???
* `echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list` # no idea
* `sudo apt-get update`
* `sudo apt-get install -y mongodb-org` # install mongodb

## Installing PhantomJS for Engine
more coming soon...

# Setting up Steam and Wagon
* `cd ~`
* `git clone git://github.com/locomotivecms/steam.git` # Clone Steam
* `git clone git://github.com/locomotivecms/wagon.git` # Clone Wagon
* `cd wagon`
* `bundle install`
* `bundle exec rake spec` # Run the built-in tests
* `bundle exec bin/wagon serve spec/fixtures/default` # Run a rails server

# Setting up Engine
* `git clone git@github.com:locomotivecms/engine.git`
* `cd engine`
* `bundle install`


# Setup from Docker
* Follow [this].(http://stackoverflow.com/questions/4911504/rvm-installed-by-ruby-not-working) You will put some lines in ~/.bashrc and /etc/bash.bashrc
* From inside the wagon directory, run `bundle install`
* `bundle exec rake spec` # Run the built-in tests
* `bundle exec bin/wagon serve spec/fixtures/default` # Run a rails server

