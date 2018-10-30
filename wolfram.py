>>>import wolframalpha
>>> input =raw_input("Question")
Question what is client
>>> app_id = "HHEEU5-4PVTTVX3PL"
>>> Client = wolframalpha.Client(app_id)
>>> res = Client.query(input)
>>> answer = next(res.results).text
>>> print answer
