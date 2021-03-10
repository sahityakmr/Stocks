# Stocks

Approach 1
UI 5 radio button:
    Form based on radio buttons
    form1 - field1, field2, field3
    form2 - field1, field2
    form3 - filed3, field4, field5
    form4 - filed3, field4, field5
    form5 - filed3, field4, field5, field6

    field0 = ""
    field1
    field2
    field3
    field4
    field5
    field6

    ReqObj:req_obj


backend consista of five diff apis
    serve_request(req_obj)
    _api1()
    _api2()
    _api3()
    _api4()
    _api5()



Approach 2
UI 5 radio button:
    Form based on radio buttons
    form1 - field1, field2, field3 : DividentRequest
    form2 - field1, field2 : RatioRequest
    form3 - filed3, field4, field5 
    form4 - filed3, field4, field5
    form5 - filed3, field4, field5, field6

    field0 = ""
    field1
    field2
    field3
    field4
    field5
    field6

    ReqObj:req_obj


backend consista of five diff apis : If we keep this as service
    ratio()
    api2()
    api3()
    api4()
    api5()


