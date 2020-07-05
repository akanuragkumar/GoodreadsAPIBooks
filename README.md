# GoodreadsAPIBooks
This is command-line app which provides book-search via GoodreadsAPI.

## Quickstart

To work in a sandboxed Python environment it is recommended to install the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Install dependencies

    ```bash
    $ cd /path/to/GoodreadsAPIBooks
    $ pip install -r requirements.txt
    ```
2. Export env for API key of Goodreads.

    ```bash
    $ export API_KEY='vOAW5NlDLXt00UcKuotxtg'
    ```

4. Run app from command-line with the book name to search as args. Example- 12177850-a-song-of-ice-and-fire

   ```bash
   $ python app.py python app.py 12177850-a-song-of-ice-and-fire
   ```

5. Run the Test-cases:

    ```bash
    # for running unit test case
    $ python test_unit.py 1764323.A_Name_to_Conjure_With
    # for running functional test case
    $ python test_functional.py 1764323.A_Name_to_Conjure_With
    ```
## Implementation
      1. Exception handling.
      2. Command line input.
      3. class GoodreadsAPIClient with member method get_book_details.
      4. Unit and functional test cases.
      5. Logging.

