# For addtional configuration
# https://docs.locust.io/en/stable/configuration.html#all-available-configuration-options
locustfile = mparticle.py
headless = true
host = https://c1i55mxsd6.execute-api.us-west-2.amazonaws.com
users = 1
# The rate per second in which users are spawned.
spawn-rate = 1
run-time = 5s 
csv = mparticle
csv-full-history = true
html = results.html
only-summary = false
