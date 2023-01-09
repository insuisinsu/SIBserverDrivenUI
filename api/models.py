# api/models.py
# MongoDB의 Dovument들을 GraphQL에서 사용하기 위한 객체로 만드는 파일

import datetime

from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, IntField

from graphene_mongo import MongoengineObjectType

# MongoDB Model
# Document는 MongoDB에서 RDBMS의 database 역할
# Collection는 MongoDB에서 RDBMS의 table 역할
# 즉, RankModel은 'graphql-example' database에 있는 ranking' Table에 대한 객체
class RankModel(Document):
    meta = {'collection': 'ranking'}
    mode = StringField()
    name = StringField()
    score = IntField()
    isMobile = BooleanField()
    reg_dttm = StringField()
    upd_dttm = StringField()

# Schema Type
# Graphql 객체 생성
class RankType(MongoengineObjectType):
    # Graphql Model로 Document 객체를 설정
    class Meta:
        model = RankModel
    
    # 'resolve_필드명' 함수는 해당 필드가 출력될 때, 처리되는 로직
    #reg_dttm을 출력할 때 실행되는 로직 ( 날짜형식 변경 )
    def resolve_reg_dttm(parent, info, **kwargs):
        return datetime.datetime.strptime(parent.reg_dttm, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
    
     # upd_dttm을 출력할 때 실행되는 로직. ( 날짜형식 변경 )
    def resolve_upd_dttm(parent, info, **kwargs):
         return datetime.datetime.strptime(parent.upd_dttm, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")