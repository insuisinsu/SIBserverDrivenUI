# api/__init__.py
# Flask Web Application 설정 파일

from flask import Flask
from flask_graphql import GraphQLView   # Flask에서 GraphQL을 제공하기 위한 GraphQLView 모듈
from api.schema import schema   # 내가 작성한 GraphQL Schema

def create_app():
    # Flask Application 생성
    app = Flask(__name__)

    # /graphql EndPoint 설정
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True   # gql 테스트 페이지 제공
        )
    )
    
    return app