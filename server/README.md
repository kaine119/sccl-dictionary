# Dictionary server

This will have a few endpoints to:
- get dictionary entries
- post feedback form entries (#7)
- let a user login and have their token saved in their session (#13)
- post usage details for a user (#13)

To run the app, you'll need `ruby` (and `gem`, which should be installed with `ruby`), as well as `bundler` and (most likely) `rack`, which you can install with
```bash
gem install bundler
gem install rack
```

After that finishes, run **`bundle install`**, then run **`bundle exec rackup config.ru`** 
