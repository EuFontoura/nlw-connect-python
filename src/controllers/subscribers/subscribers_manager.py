from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpReponse
from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscriberManager:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.subscribers_repo = subscribers_repo

    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpReponse:
        link = http_request.param["link"]
        event_id = http_request.param["event_id"]
        subs = self.subscribers_repo.select_subscribers_by_link(link, event_id)
        return self.__format_subs_by_link(subs)
    
        def get_event_ranking(self, http_request: HttpRequest) -> HttpReponse:
            event_id = http_request.param["event_id"]
            event_ranking = self.subscribers_repo.get_ranking(event_id)
            return self.__format_event_ranking(event_ranking)

        def __format_subs_by_link(self, subs: list) -> HttpReponse:
            formatted_subscriber = []
            for sub in subs:
                formatted_subscriber.append(
                    {
                        "nome": sub.nome,
                        "email": sub.email,
                    }
                )
            return HttpReponse(
                body={
                    "data": {
                        "Type": "Subscriber",
                        "count": len(formatted_subscriber),
                        "subscribers": formatted_subscriber,
                    }
                }
            )
        def __format_event_ranking(self, event_ranking: list) -> HttpReponse:
            formatted_event_ranking = []
            for position in event_ranking:
                formatted_event_ranking.append(
                    {
                        "link": position.link,
                        "total_subscribers": position.total,
                    }
                )
            return HttpReponse(
                body={
                    "data": {
                        "Type": "Ranking",
                        "count": len(formatted_event_ranking),
                        "ranking": formatted_event_ranking,
                    }
                }
            )