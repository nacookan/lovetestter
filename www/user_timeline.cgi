#!/usr/local/bin/ruby

require 'config'
require 'rubygems'
require 'twitter'
require 'json'
require 'cgi'

cgi = CGI.new

id = cgi['id']

begin
cgi.out('text/javascript'){
  Twitter::Client.new.user_timeline(id.to_i).to_json
}
rescue
puts "Content-type: text/plain\n\n"
puts $!
end
