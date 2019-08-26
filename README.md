# Google Foobar Challenge Summoner
**Project that aims to automatically summon the Foobar challenge using Google search.**

# Google Foobar Challenge Summoner

The aim of that project is to programmatically trigger the Google Foobar Challenge that is explained in detail https://www.freecodecamp.org/news/the-foobar-challenge-googles-hidden-test-for-developers-ed8027c1184/

In addition that will help us better recognise important and quality software developer content from mediocre one - supposing that the quality content triggers the Foobar Challenge more times.

The script is written in Python and uses Selenium to query content.
Currently the driver class SearchHarness has three steps:

LOGIN - login to your Google account
GET - find and store question Headers from Stack Overflow.
SEARCH - query the questions in Google Search.

# Login

That step is used to login on a Google account to have your future searches be recorded under ones name. Not sure if it is entirely necesserry yet it boosts confidence in the result.

To derive credentials the library configparser is used. To install it use:

```
pip install configparser
```

To add credential details, add a file named *config.properties* with your usename and password in the account section:

```
[Account]
username=MyUsername
password=MyPassword
```

# GET

Get seeks to find and store relevant software developer content that is good for triggering the Foobar Challenge on Google Search. For now these are Stack Overflow question headers derived from the Stack Overflow tags.

# SEARCH

That is the step that is used to optimistically trigger the Foobar Challenge. Foobar Challenge is triggered by searching releated software developer content on Google Search which will be the output from the **GET** step. A challenge here is to circumvent the Google Captcha bot query detection which is TBD.
