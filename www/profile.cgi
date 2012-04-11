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

if !session['access_token'] then
  cgi.out('text/javascript'){
    {
      :logged_in => false,
      :profile => {}
    }.to_json
  }
else
  Twitter.configure do |config|
    config.consumer_key = CONSUMER_KEY
    config.consumer_secret = CONSUMER_SECRET
    config.oauth_token = session['access_token']
    config.oauth_token_secret = session['access_secret']
  end
  client = Twitter::Client.new
  
  cgi.out('text/javascript'){
    {
     :logged_in => true,
     :profile => client.verify_credentials
    }.to_json
  }
end
