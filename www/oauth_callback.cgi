#!/usr/local/bin/ruby

require 'config'
require 'rubygems'
require 'oauth'
require 'cgi'
require 'cgi/session'

cgi = CGI.new
session = CGI::Session.new(cgi, { 'tmpdir' => SESSION_DIR })

oauth_token = cgi['oauth_token']
oauth_verifier = cgi['oauth_verifier']

consumer = OAuth::Consumer.new(
  CONSUMER_KEY,
  CONSUMER_SECRET,
  :site => 'http://api.twitter.com'
)
request_token = OAuth::RequestToken.new(
  consumer,
  session['request_token'],
  session['request_token_secret']
)

access_token = request_token.get_access_token({ :oauth_verifier => oauth_verifier })

session['access_token'] = access_token.token
session['access_secret'] = access_token.secret

print cgi.header('Location' => '/')
