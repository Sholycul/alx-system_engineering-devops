# set up SSH configurations

# Ensure that password authentication is disabled
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

# Declare the identity file to be used by SSH client
file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}

