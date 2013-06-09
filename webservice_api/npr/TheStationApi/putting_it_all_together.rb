require "rest-client"
require "json"

events_url = "https://api.box.com/2.0/events"

response = RestClient.get(
   events_url,
   :params => {:limit => 1},
   # Put the OAuth header here
   :authorization => "Bearer " << "VLb46cZ7Lurjm6jJ3PMkM6EllSe4tfxa"
)

p JSON.parse(response.body)
