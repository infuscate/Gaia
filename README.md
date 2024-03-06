# Gaia
## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## About

Gaia is a tool that allows you to mass create discord groupchats. Discord changing their rate limiting method causing this tool to no longer perform that well. I made it the best I could with the given situation. It'll retry after the ratelimitation is over so it's not spamming uneeded request.

## Features

 - Retry_After Delay
 - Can add up to 9 members (min is 2)
 - Automatically assign the groups different names

## Instalation

```bash
# Clone the Github repository
git clone https://github.com/infuscate/Gaia.git

# Access the directory and install the required libraries
cd Athena
pip install -r requirements.txt

# Run main.py
python main.py
```

## Usage
### Open config.json to add / remove ids, add / remove groupchat names and change your token
```json
{
    "token": "discord-token",

    "names":      ["hello", "lmao?", "topg"],
    "recipients": ["id1","id2"],

    "delay": 0.5
}
```

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software.
