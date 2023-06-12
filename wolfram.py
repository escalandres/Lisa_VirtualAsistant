import wolframalpha
app_id = "RGKTU7-VYTGGTHK2Y"
client = wolframalpha.Client(app_id)

try:
    person = "what is 2 + 2"
    wolfram_res = next(client.query(person).results).text
    print(wolfram_res)
except Exception as e:
    print("Error:", e)