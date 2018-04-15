# credit-to-customer

### To run
From the root directory run

    source env/bin/activate
    cd src
    dev_appserver.py ./

### Sample requests with curl

    curl --request PUT --header "Content-Type: application/json" --data '["put@email.com", {"test": "testPut"}]' http://localhost:8080/test
    curl --request GET --header "Content-Type: application/json" localhost:8080/test?leadingDigits=5407&trailingDigits=3456&startDate=1208&endDate=1508&cardType=MasterCard

### End-to-End testing scenarios:

###### Scenario One
1. Customer card details are read into system.
2. Partial card details sent through `GET` request.
3. `GET` returns email addresses associated with those partial details.
4. Customer email exists within the return.

###### Scenario Two
1. Customer card details are read into system.
2. Partial card details sent through `GET` request.
3. `GET` returns email addresses associated with those partial details.
4. Customer email does not exist within the return.
5. Customer email and the partial card details are added tot he database with a `PUT` request.
