# Practice Quiz: Introduction to Puppet

1. A Puppet agent inspects /etc/conf.d, determines the OS to be Gentoo Linux, then activates the Portage package manager. What is the provider in this scenario?  

    [ ] /etc/conf.d    
    [x] Portage  
    [ ] Gentoo Linux  
    [ ] The Puppet agent

2. Which of the following examples show proper Puppet syntax?

    ```
    class AutoConfig {
      package { 'Executable':
        ensure => latest,
      }
      file { 'executable.cfg':
        source => 'puppet:///modules/executable/Autoconfig/    executable.cfg'
        replace => true,
      }
      service { 'executable.exe':
        enable  => true,
        ensure  => running,
      }
    }
    ```

3. What is the benefit of grouping resources into classes when using Puppet?

    [ ] Providers can be specified  
    [x] Configuration management is simplified  
    [ ] The title is changeable  
    [ ] Packages are not required

4. What defines which provider will be used for a particular resource?

    [x] Puppet assigns providers based on the resource type and data collected from the system.  
    [ ] A menu allows you to choose providers on a case-by-case basis.  
    [ ] The user is required to define providers in a config file.  
    [ ] Puppet uses an internet database to decide which provider to use.

5. In Puppet’s file resource type, which attribute overwrites content that already exists?

    [ ] Purge  
    [ ] Overwrite  
    [x] Replace  
    [ ] Save