#!/usr/local/bin/ruby

require 'config'
require 'rubygems'
require 'oauth'
require 'twitter'
require 'json'
require 'cgi'
require 'cgi/session'

cgi = CGI.new
session = CGI::Session.new(cgi, { 'tmpdir' => SESSION_DIR })

Twitter.configure do |config|
  config.consumer_key = CONSUMER_KEY
  config.consumer_secret = CONSUMER_SECRET
  config.oauth_token = session['access_token']
  config.oauth_token_secret = session['access_secret']
end
client = Twitter::Client.new

id = cgi['id']

begin
cgi.out('text/javascript'){
  client.user_timeline(id.to_i).map{|t| t.attrs}.to_json
}
rescue
puts "Content-type: text/plain\n\n"
puts $!
end
