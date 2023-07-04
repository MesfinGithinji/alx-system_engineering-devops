#!/usr/bin/env ruby
# A regex that returns SENDER,RECIEVER,FLAGS.
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
