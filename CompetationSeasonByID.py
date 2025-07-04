import requests
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
competitionId = "cpl::Football_Competition::854b8253300c4811a11094bbe0da81ee"
url = "https://concacaf-api.dev.sdp.deltatre.digital/v1/cpl/football/competitions/{{competitionId}}/seasons?locale=en-us"
params = {
    "locale": "en-us"
}
response = requests.get(url, params=params)
assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
json_data = response.json()
assert "seasons" in json_data, "Missing 'seasons' field in response"
print("✅ API validation passed.")

schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "seasons": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "seasonId": {
            "type": "string"
          },
          "startDateUtc": {},
          "endDateUtc": {},
          "seasonName": {
            "type": "string"
          },
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
          "seasonId",
          "startDateUtc",
          "endDateUtc",
          "seasonName",
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
    "seasons",
    "apiCallRequestTime"
  ]
}


try:
    validate(instance=json_data, schema=schema)
    print("✅ Schema is valid")
except ValidationError as e:
    print(f"❌ Schema validation failed: {e.message}")





