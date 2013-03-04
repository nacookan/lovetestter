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

ids = cgi['ids'].split(/,/).map {|item| item.to_i}

cgi.out('text/javascript'){
  client.users(*ids).map{|u| u.attrs}.to_json
}

