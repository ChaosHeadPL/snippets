import requests
import logging

logger = logging()


def get_json(url):
    try:
        data = requests.get(url, timeout=30)
        return data.json

    except ValueError as err:
        raise ValueError
        logger.error(f"ERROR, {url} returned incorrect type of data. JSON required!")
        logger.error(err)
        
        return {"status": f"ERROR, {url} returned incorrect type of data. JSON required!"}

    except TimeoutError as err:
        logger.error(f"ERROR, {url} Timeout!")
        logger.error(err)
        return {"status": f"ERROR, {url} Timeout!"}

    except Exception as err:
        logger.error(err)
        logger.error(f"ERROR, {url} Timeout!")
        return {"status": f"ERROR, {url} Timeout!"}