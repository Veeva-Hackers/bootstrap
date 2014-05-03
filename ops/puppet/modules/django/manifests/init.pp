class django {
    package { 'django':
        ensure => installed,
        provider => pip,
    }

    package { 'boto':
        ensure => installed,
        provider => pip,
    }

    package { 'djangorestframework':
        ensure => installed,
        provider => pip,
    }

    package { 'markdown':
        ensure => installed,
        provider => pip,
    }

    package { 'django-filter':
        ensure => installed,
        provider => pip,
    }

    package { 'django-storages':
        ensure => installed,
        provider => pip,
    }

    package { 'python-psycopg2':
        ensure => present,
    }

    package { 'postgresql':
        ensure => present,
    }

    package { 'yelpapi':
        ensure => installed,
        provider => pip,
    }
}
