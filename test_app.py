import pytest
import requests
import json
import urllib.parse
import subprocess

def callHowDoI(testQuery):
    # x = requests.post("http://localhost:5000/test", params={"testquery": testQuery})
    cmd = "http -f POST http://localhost:5000/test?testquery={}".format(urllib.parse.quote(testQuery))
    res = subprocess.check_output(cmd, shell=True)
    # get rid of the b' on the front of the string
    res = res.decode('utf-8')
    jsonRes = json.loads(res)
    return jsonRes["status"]


def test_func():
    testQueries = [
        {"query":"howdoi get gmail","shouldFail": False},
        {"query":"howdoi learn java","shouldFail": False},
        {"query":"howdoi compile c code","shouldFail": False},
        {"query":"howdii run faster","shouldFail": True},
        {"query":"howdoi exit vim","shouldFail": False},
        {"query":"when is half life 3 coming out","shouldFail": True},
        {"query":"howdoi install gentoo","shouldFail": False},
        {"query":"h``owdoi love vim","shouldFail": True},
        {"query":"-ho[wdoi love vim","shouldFail": True}
        ]

    for test in testQueries:
        response = callHowDoI(test["query"])
        if test["shouldFail"]:
            assert response == "error"
        else:
            assert response == "success"
   
