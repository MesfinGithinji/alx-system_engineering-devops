#execute the pkill command
exec { 'killmenow':
  command => '/bin/pkill',
}
