# VK Post Text Parser
A Python script that uses the `vk_api` module to parse the texts of posts from a VKontakte page or group into `.txt`.

## How to use?
1. You will need Python 3.11 to run the scirpt, which you can download, for example [here](https://www.python.org/downloads/).
2. Run the following command:
  ```bash
  pip install vk_api
  ```
3. Setup `config.json`.
4. Run `main.py`:
  ```bash
  python3 main.py
  ```
5. The result `output.txt` will appear in the same directory as `main.py`.

## Configuration file
The `config.json` configuration file is used to set the behavior of the program to suit the user's needs. It contains:
- `access_token`: your [access token](https://dev.vk.com/api/access-token/getting-started) to VK API methods;
- `domain`: id of the VKontakte page or group;
- `post_number`: number of posts to retrieve;
- `post_filter`: post filter, which includes:
  - `ad_allowed`: boolean of whether the post can be promotional;
  - `repost_allowed`: boolean of whether the post can be a repost;
  - `restricted_words`: a list of banned words;

## Contributing
This repository is open for contribution. So feel free to open an issue and make pull requests.
