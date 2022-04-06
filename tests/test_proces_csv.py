from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)


def test_process_csv():
    with open("./tests/_inputs/test.csv", "r") as f:
        csv_data = f.read()
    sources_config = [
        {
            "sourceId": "INT-GEO-0033",
            "enabled": True,
            "retryNumber": 1,
            "version": 1,
            "inputKeys": [
                {
                    "field": "location",
                    "required": False,
                    "atLeastOneRequired": True,
                    "structure": {
                        "location": {
                            "lat": "",
                            "lng": ""
                        }
                    }
                },
                {
                    "field": "address",
                    "required": False,
                    "atLeastOneRequired": True,
                    "structure": {
                        "address": {
                            "country": "",
                            "city": "",
                            "street1": "",
                            "street2": ""
                        }
                    }
                }
            ]
        },
        {
            "sourceId": "INT-DIG-0032",
            "enabled": True,
            "retryNumber": 1,
            "version": 1,
            "inputKeys": [
                {
                    "field": "personId",
                    "required": False,
                    "atLeastOneRequired": True,
                    "structure": {
                        "personId": ""
                    }
                },
                {
                    "field": "name",
                    "required": False,
                    "atLeastOneRequired": True,
                    "structure": {
                        "name": ""
                    }
                },
                {
                    "field": "email",
                    "required": False,
                    "atLeastOneRequired": True,
                    "structure": {
                        "email": ""
                    }
                },
                {
                    "field": "countryCode",
                    "required": True,
                    "atLeastOneRequired": True,
                    "structure": {
                        "countryCode": ""
                    }
                },
                {
                    "field": "dateToAnalyze",
                    "required": False,
                    "structure": {
                        "dateToAnalyze": ""
                    }
                }
            ]
        },
        {
            "sourceId": "INT-DIG-0036",
            "enabled": True,
            "retryNumber": 1,
            "version": 1,
            "inputKeys": [
                {
                    "field": "email",
                    "required": True,
                    "structure": {
                        "email": ""
                    }
                }
            ]
        }
    ]
    expected_payload = [
        {
            "personId": "1734556494",
            "email": "yo1@email.com",
            "countryCode": "ec",
            "location": {
                "lat": "1",
                "lng": "2"
            },
            "sourcesConfig": [
                {
                    "sourceId": "INT-GEO-0033",
                    "enabled": True,
                    "retryNumber": 1,
                    "version": 1
                },
                {
                    "sourceId": "INT-DIG-0032",
                    "enabled": True,
                    "retryNumber": 1,
                    "version": 1
                },
                {
                    "sourceId": "INT-DIG-0036",
                    "enabled": True,
                    "retryNumber": 1,
                    "version": 1
                }
            ]
        },
        {
            "personId": "1734556495",
            "email": None,
            "countryCode": "ec",
            "location": {
                "lat": "3",
                "lng": "4"
            },
            "sourcesConfig": [
                {
                    "sourceId": "INT-GEO-0033",
                    "enabled": True,
                    "retryNumber": 1,
                    "version": 1
                },
                {
                    "sourceId": "INT-DIG-0032",
                    "enabled": True,
                    "retryNumber": 1,
                    "version": 1
                }
            ]
        },
        {
            "personId": "1734556497",
            "email": "yo3@email.com",
            "countryCode": "ec",
            "location": {
                "lat": None,
                "lng": None
            },
            "sourcesConfig": [
                {
                    "sourceId": "INT-DIG-0032",
                    "enabled": True,
                    "retryNumber": 1,
                    "version": 1
                },
                {
                    "sourceId": "INT-DIG-0036",
                    "enabled": True,
                    "retryNumber": 1,
                    "version": 1
                }
            ]
        }
    ]
    response = client.post(
        "/challenge/process-batch-from-csv",
        json={
            "csv_data": csv_data,
            "sourcesConfig": sources_config
        }
    )
    assert response.json()["payload"] == expected_payload
