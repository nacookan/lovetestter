#!/usr/local/bin/ruby

require 'config'
require 'rubygems'
require 'oauth'
require 'cgi'
require 'cgi/session'

cgi = CGI.new
session = CGI::Session.new(cgi, { 'new_session' => true, 'tmpdir' => SESSION_DIR })

consumer = OAuth::Consumer.new(
  CONSUMER_KEY,
  CONSUMER_SECRET,
  :site => 'http://api.twitter.com'
)
option = { :oauth_callback => OAUTH_CALLBACK_URL }
request_token = consumer.get_request_token(option, {})

session['request_token'] = request_token.token
session['request_token_secret'] = request_token.secret

print cgi.header('Location' => request_token.authorize_url)

