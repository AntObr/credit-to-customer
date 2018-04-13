import manager

mgr = manager.Manager('data.json')

leadingDigits="5407"
trailingDigits="3456"
startDate="1208"
endDate="1508"
cardType="MasterCard"

query = {
    "leadingDigits": leadingDigits,
    "trailingDigits": trailingDigits,
    "startDate": startDate,
    "endDate": endDate,
    "cardType": cardType
}

mgr.load()
result = mgr.search(query)

print(result)
