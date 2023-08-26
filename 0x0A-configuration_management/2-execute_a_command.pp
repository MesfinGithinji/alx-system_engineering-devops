#execute the pkill command
exec { 'pkill -f killmenow':
  provider => 'shell'
}
