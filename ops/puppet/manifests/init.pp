# In the "pre" stage, install pip, gunicorn, and update the OS.
# I'm using this whole "pre" stage thing because I can't figure out how to set
# "pip" as a proper dependency.
# I'm installing gunicorn here because this method of installing "pip" is from
# an existing module that I'm getting for free.
stage { "pre": before => Stage["main"] }
class pre {
    class { 'python':
		pip => true,
		gunicorn => true,
	}

	exec { 'apt-update':
		command => '/usr/bin/apt-get update',
	}
}
class { "pre": stage => "pre" }

# Project root path
$project_root = '/vagrant/'

# Include my own module for our Django stack.
include django

# Include external module for supervisor 
include supervisor
supervisor::service {
    'hello_world':
        ensure      => present,
        enable      => true,
        command		=> "${project_root}/ops/bash/start_gunicorn.sh"
        #hasrestart  => true,
        #hasstatus   => true,
        #require     => Class['config'];
}

package { 'dos2unix':
    ensure => present,
}

exec { 'dos2unix':
    command => "dos2unix ${project_root}ops/bash/start_gunicorn.sh",
    path => "/usr/bin/",
    require => Package['dos2unix'],
}

