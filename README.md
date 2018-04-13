# credit-to-customer

### To run
From the root directory run

    source env/bin/activate
    cd src
    dev_appserver.py app.yaml
    
### Sample requests with curl

    curl --request PUT --header "Content-Type: application/json" --data '{"content": "test"}' http://localhost:8080/_ah/api/echo/v1/echo
    curl --request GET --header "Content-Type: application/json" http://localhost:8080/_ah/api/echo/v1/echo/getEmails?trailingDigits=1&leadingDigits=2
