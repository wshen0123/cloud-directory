# cloud-directory
### Problem Solved

- Have a server behind your home router on DHCPed carrier network?
- Need to keep track of your home network IP for IoT devices?

Cloud-directory is a small utility for keeping track of DHCPed hosts.

### HOWTO

Deploy it on Google App Engine for free.

To check in IP from behind your network
`curl -d "" http://<app-name>.appspot.com/<hostname>/ip`

To get current IP
`curl http://<app-name>.appspot.com/<hostname>/ip`

You can set up cron.hourly job to check in your most current IP (though carrier typically don't change your IP allocation for weeks).
