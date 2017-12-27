require 'sinatra'
require 'mongo'
require 'json'
require 'sinatra/reloader' if development?
set :port, 3000

configure { set :server, :puma }

client = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'books')
Books = client[:books]

get '/' do
  "Books.api"
end

get '/Books' do
  data = Books.find.to_a
  content_type :json
  data.to_json
end

post '/Books' do
  data = JSON.parse request.body.read
  result = Books.insert_one(data);
  content_type :json
  result.to_json
end

put '/Books/:id' do
  data = JSON.parse request.body.read
  result = Books.find({ ID: params['id'].to_i }).replace_one(data);
  content_type :json
  data.to_json
end

delete '/Books/:id' do
  data = Books.find({ ID: params['id'].to_i }).delete_many
  content_type :json
  data.to_json
end
