import requests
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
competitionId = "cpl::Football_Competition::854b8253300c4811a11094bbe0da81ee"
url = "https://concacaf-api.dev.sdp.deltatre.digital/v1/cpl/football/competitions/{{competitionId}}?locale=en-us"
params = {
    "locale": "en-us"
}
response = requests.get(url, params=params)
assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
json_data = response.json()
assert "competitions" in json_data, "Missing 'competitions' field in response"
print("✅ API validation passed.")

schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "competitions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "competitionId": {
            "type": "string"
          },
          "providerId": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "officialName": {
            "type": "string"
          },
          "shortName": {
            "type": "string"
          },
          "acronymName": {
            "type": "string"
          }
        },
        "required": [
          "competitionId",
          "providerId",
          "name",
          "officialName",
          "shortName",
          "acronymName"
        ]
      }
    },
    "apiCallRequestTime": {
      "type": "string"
    }
  },
  "required": [
    "competitions",
    "apiCallRequestTime"
  ]
}

try:
    validate(instance=json_data, schema=schema)
    print("✅ Schema is valid")
except ValidationError as e:
    print(f"❌ Schema validation failed: {e.message}")





