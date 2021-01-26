class ntp {
  package { 'ntp':
    ensure => latest,
  }
  file {'etc/ntp.conf':
    source  => '/home/user/ntp.conf',
    replace => true,
    require => Package['ntp'],
    notify  => Service['ntp'],
  }
  service { 'ntp':
    ensure  => running,
    enable  => true,
    require => File['/etc/ntp.conf'],
  }
}

include ntp
