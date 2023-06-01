# FinnhubProducer

URL: https://github.com/RSKriegs/finnhub-streaming-data-pipeline/blob/main/FinnhubProducer/src/FinnhubProducer.py

The `FinnhubProducer.py` script is a Python application that connects to the Finnhub.io websocket, retrieves real-time trading data, and ingests it into a Kafka broker. Here's a detailed breakdown of the script:

1. **Importing Libraries**: The script begins by importing necessary Python libraries such as `os`, `ast`, `json`, and `websocket`. It also imports utility functions from `utils.functions`.

2. **FinnhubProducer Class**: The `FinnhubProducer` class is defined, which is responsible for connecting to the Finnhub websocket, retrieving data, and ingesting it into Kafka.

   - **Initialization**: In the `__init__` method, the class initializes the Finnhub client, Kafka producer, Avro schema, and tickers list. It also sets up a websocket connection to Finnhub and starts the websocket.

   - **on_message**: This method is triggered when a new message is received from the Finnhub websocket. The message is loaded as a JSON object, encoded into Avro format, and sent to a Kafka topic.

   - **on_error**: This method is triggered when an error occurs with the websocket. It simply prints the error.

   - **on_close**: This method is triggered when the websocket is closed. It prints a message indicating that the websocket has been closed.

   - **on_open**: This method is triggered when the websocket is opened. It subscribes to each ticker in the tickers list. If the `validate` flag is set, it validates the ticker before subscribing.

3. **Main Execution**: If the script is run as the main program, it creates an instance of the `FinnhubProducer` class.

The purpose of this script is to ingest real-time trading data from Finnhub into a Kafka broker. This data can then be processed by other components of the data pipeline.

**Pros of this solution**:

- The use of websockets allows for real-time data retrieval.
- The use of Kafka allows for efficient ingestion of data into the data pipeline.
- The use of Avro ensures that the data is in a standardized format.

**Cons of this solution**:

- The script is dependent on specific technologies (Finnhub, Kafka), which might limit flexibility.
- The script does not handle potential errors that could occur during data ingestion, such as network errors or Kafka broker failures.
- The script does not provide a way to unsubscribe from tickers, which could lead to unnecessary data ingestion if a ticker is no longer of interest.