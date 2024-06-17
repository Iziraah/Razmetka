import requests

# Параметры запроса
amount = 10000
amount_type = "receive_amount"
payee_account = "201576188211"
payee_currency = 643          #amount:amount_type:payee_account:payee_currency:shop_currency:shop_id:shop_payment_id+secret
# shop_amount = 10000       #shop_id, "0@-mCfU|?2}{|%kB6", payway, account, amount
shop_currency = 643  #{amount}:{currency}:{payway}:{shop_id}:{shop_order_id}{secret_key}
shop_id = 6216  
#10000:receive_amount:201576357422:643:643:6216:55ac443d-958b-40e3-8956-e04e725613244555L\ITkcm6.GL`NP3(
shop_payment_id = "55ac443d-958b-40e3-8956-e04e725613244555"
manual_sign = "ef8b5158cb2e1c2e8b7cd067b9943c31c9a6ab257fc01635be960de0626d2c34"  #




# Формируем параметры запроса
params = {
    "amount": amount,
    "amount_type": amount_type,
    "payee_account": payee_account,
    "payee_currency": payee_currency,
    "shop_currency": shop_currency,
    # "shop_amount": shop_amount,
    "shop_id": shop_id,
    "shop_payment_id": shop_payment_id,
    "sign": manual_sign
}

# URL для создания перевода
url = "https://core.piastrix.com/transfer/create"
print(params)
# Выполняем запрос
response = requests.post(url, json=params)


print(response.status_code)
print(response.json())