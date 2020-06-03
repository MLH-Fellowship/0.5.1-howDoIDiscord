import pytest
import requests

def callHowDoI(testQuery):
    x = requests.post("http://localhost:5000/test", params={"testquery": testQuery})
    return x.json()["status"]

def test_func():
    testQueries = [
        {"query":"howdoi get gmail","shouldFail": False},
        {"query":"howdoi learn java","shouldFail": False},
        {"query":"howdoi compile c code","shouldFail": False},
        {"query":"howdii run faster","shouldFail": True},
        {"query":"howdoi exit vim","shouldFail": False},
        {"query":"howdo i love vim","shouldFail": True},
        ]

    for test in testQueries:
        response = callHowDoI(test["query"])
        if test["shouldFail"]:
            assert response == "error"
        else:
            assert response == "success"
   
    