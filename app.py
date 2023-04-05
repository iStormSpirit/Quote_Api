from api import api, app
from api.resources.author import AuthorListResource, AuthorResource
from api.resources.quote import (QuoteListResource,
                                 QuoteListSortedAuthorNameResource,
                                 QuoteListSortedIdResource, QuoteResource,
                                 QuotesByAuthorsResource,
                                 QuotesChangeRateResource)

api.add_resource(AuthorListResource, "/author")
api.add_resource(AuthorResource, "/author/<int:id>", "/author")

api.add_resource(QuoteListResource, "/quotes")
api.add_resource(QuoteResource, "/quotes", "/author/<int:author_id>/quotes")
api.add_resource(QuotesChangeRateResource, "/quotes/<int:quote_id>/<type>")
api.add_resource(QuotesByAuthorsResource, "/author/<int:author_id>/quotes/<int:quote_id>")

api.add_resource(QuoteListSortedIdResource, "/quotes/idsorted")
api.add_resource(QuoteListSortedAuthorNameResource, "/quotes/authornamesorted")

if __name__ == '__main__':
    app.run(debug=False)
