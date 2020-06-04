
<p align="center">
  <a href="[https://github.com/MLH-Fellowship/0.5.1-howDoIDiscord](https://github.com/MLH-Fellowship/0.5.1-howDoIDiscord)">
    <img
      alt="Req"
      src="https://i.imgur.com/pPo1Aj6.png"
      width="600"
    />
  </a>
</p>

A discord bot interface for the popular [howdoi](https://github.com/gleitz/howdoi) python tool that serves instant coding answers via the command line.
## How does it work?
<p align="center">
    <img
      alt="Req"
      src="https://i.imgur.com/xwmT9jA.png"
      width="800"
    />
  </a>
</p>

## Unit Testing

Unit testing can be carried out by first starting the flask server with `python app.py` with `testing=true` set in the env. This will turn on the flask server to accept HTTP requests which is only used during testing. You'll also need [HTTPie](https://httpie.org/).

Once the flask server is running you can start the unit tests with `pytest` in the main directory and it will run through the tests that are in `test_app.py`

___

Built for a hackathon for the [innaugural MLH fellowship](https://fellowship.mlh.io/).
