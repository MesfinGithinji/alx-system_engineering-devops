#!/usr/bin/env ruby
# A regex that must be matching only capital letters.
puts ARGV[0].scan(/[A-Z]/).join
