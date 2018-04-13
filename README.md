# credit-to-customer

### To run
From the root directory run

    source env/bin/activate
    cd src
    dev_appserver.py ./

### Sample requests with curl

    curl --request PUT --header "Content-Type: application/json" --data '["put@email.com", {"test": "testPut"}]' http://localhost:8080/test
