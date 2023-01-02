from typing import Dict, Tuple, Type
from collections import namedtuple
from src.errors import HttpRequestError
import requests
from requests import Request

class HttpRequest:

    def __init__(self) -> None:
       self.get_response = namedtuple('get_response', 'status_code request response')


    def get_payload(self, page: int, url: str) -> Tuple[int, Type[Request], Dict]:

        req = requests.Request(
            method='GET',
            url=url,
            params={"page": page}
        )

        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if ((status_code >= 200) and (status_code <= 299)):
            return self.get_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()["detail"], status_code=status_code
            )

    def __send_http_request(self, req_prepared: Type[Request]) -> any:
        '''
            Prepare a session and send http request
            :param - req_prepared: Request Object with all params
            :response - Http response raw
        '''

        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response